from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql
import requests

TELEBOT_URL = 'https://api.telegram.org/bot'
TELEBOT_TEST = 'https://api.telegram.org/bot{}/getMe'
RANDOM_WORD_API_URL = 'https://random-word-api.herokuapp.com/word?lang=en'
YANDEX_DICT_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup'
YANDEX_DICT_TEST = 'https://dictionary.yandex.net/api/v1/dicservice.json/lookup?key={}&lang=en-ru&text=test'


class EnglishCardsDB:

    def __init__(self, user='postgres', password='postgres', 
                 host='localhost', database='english_cards'):

        """ Если базы данных не существует, создаем новую, 
        в ней создаем таблицы, в ней сохраняем дефолтный набор данных, 
        к ней подключаемся. """ 

        self.create_database(user, database, host, password)
        self.con = connect(dbname=database, user=user, 
                password=password, host=host)
        self.create_tables()
        self.set_token('yandex_dict', YANDEX_DICT_TEST)
        self.set_default_words('test')
        self.set_token('telegram', TELEBOT_TEST)

    def create_database(self, user, database, host, password):
        con = connect(user=user, host=host, password=password)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        with con.cursor() as cur:
            cur.execute("""
               SELECT EXISTS (SELECT 1 FROM pg_database WHERE datname=%s);
               """, (database,))
            if not cur.fetchone()[0]:
                query = sql.SQL("CREATE DATABASE {};").format(
                        sql.Identifier(database))
                print(query)
                cur.execute(query)
        con.close()

    def create_tables(self):
        with self.con.cursor() as cur:
            cur.execute("""
                CREATE TABLE IF NOT EXISTS tokens (
                    api_name VARCHAR(35) PRIMARY KEY,
                    token VARCHAR(100), 
                    api_url TEXT,
                    api_test_request TEXT
                );
                CREATE TABLE IF NOT EXISTS words (
                    id SERIAL PRIMARY KEY,
                    en VARCHAR(35),
                    en_example TEXT,
                    ru VARCHAR(35),
                    ru_example TEXT
                );
                CREATE TABLE IF NOT EXISTS teleusers (
                    uid BIGINT PRIMARY KEY
                );
                CREATE TABLE IF NOT EXISTS themes (
                    id SERIAL PRIMARY KEY,
                    name VARCHAR(35) DEFAULT 'all'
                );
                CREATE TABLE IF NOT EXISTS teleusers_words (
                    uid BIGINT REFERENCES teleusers(uid),
                    wid SERIAL REFERENCES words(id),
                    learned BOOLEAN DEFAULT FALSE,
                    tid SERIAL REFERENCES themes(id), 
                    PRIMARY KEY (uid, wid, tid)
                );
            """)
            self.con.commit()
            cur.execute("""INSERT INTO themes VALUES (1,'all')
                ON CONFLICT (id) DO UPDATE SET name = 'all'
                WHERE themes.id = 1;""")
            self.con.commit()

    def set_token(self, api_name, api_test_request, token=''):
        with self.con.cursor() as cur:
            # если в базе действительный токен, выходим
            cur.execute('SELECT token FROM tokens WHERE api_name = %s',
                    (api_name,))
            r = requests.get(api_test_request.format(cur.fetchone()[0])) 
            if r.status_code == 200:
                return
            # запрашиваем ввод токена пока не получим правильный
            while True:
                r = requests.get(api_test_request.format(token))
                if r.status_code == 200:
                    cur.execute("""
                        INSERT INTO tokens VALUES (%(api_name)s, %(token)s) 
                        ON CONFLICT (api_name) DO UPDATE SET token = %(token)s 
                        WHERE tokens.api_name = %(api_name)s;""", 
                        {'api_name': api_name, 'token': token}) 
                    self.con.commit() 
                    return token 
                else: 
                    token = input(f"""
                        При запросе {api_test_request.format(token)}
                        получен ответ: {r.reason}. Введите действительный 
                        токен.\n""")

    def get_one(self, query):
        with self.con.cursor() as cur:
            cur.execute(query)
            return cur.fetchone()
    
    def get_all(self, query):
        with self.con.cursor() as cur:
            cur.execute(query)
            return cur.fetchall()

    def execute(self, query):
        with self.con.cursor() as cur:
            cur.execute(query)
            self.con.commit()

    def set_default_words(self, words = (), count=10, reset=False):
        # дополняем до count дефолтный список случайными словами и words
        # дефолтность определяется причастностью слов к пользователю 0 
        if reset:
            self.execute('DELETE FROM teleusers WHERE uid = 0;') 
            db_words = ()
        else:
            db_words = self.get_all(
                'SELECT FROM teleusers WHERE teleusers.uid = 0;') 
        if len(db_words) >= count:
            self.execute(sql.SQL(
                'DELETE FROM teleusers WHERE uid = 0 LIMIT {};').format(
                    len(db_words)-count))
            return
        else:
            if isinstance(words, str):
                words = tuple(words.split())
            else:
                words = words[:count-len(db_words)]
        yandex_token = self.get_one(
             "SELECT token FROM tokens WHERE api_name = 'yandex_dict';")[0]
        for w in words:
            r1 = requests.get(YANDEX_DICT_URL + '?key=' + yandex_token 
                    + '&lang=en-ru&text=' + w).json()
            r2 = requests.get(YANDEX_DICT_URL + '?key=' + yandex_token 
                    + '&lang=en-en&text=' + w).json()
            r3 = requests.get(YANDEX_DICT_URL + '?key=' + yandex_token 
                    + '&lang=ru-ru&text=тест').json()
            print(r1,r2,r3)
        """
        if len(db_words) + len(words) < count:
            while True:
                r = requests.get(RANDOM_WORD_API_URL + '&number=' 
                    + str(count - len(words) - len(db_words)))
                words += tuple(r.json())
                r = requests.get(YANDEX_DICT_URL + '?key=' + yandex_token 
                        + '&lang=en-ru&text=' + w).json() #['def']['tr']
                db_words += (w, r['ex']['text'], r['text'], r['ex']['text']) 
            self.execute(sql.SQL(
                'INSERT INTO words(en, en_example, ru, ru_example) VALUES ({});'
                ).format(sql.SQL('),(').join(
                    sql.SQL(',').join(
                        sql.Literal(__) for __ in _ for _ in words))))
            print(words)
            """



