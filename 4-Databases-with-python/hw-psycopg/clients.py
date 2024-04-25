from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from psycopg2 import sql

con = None

def create_database(user, dbname, host, password):
    con = connect(user=user, host=host, password=password)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    with con.cursor() as cur:
        cur.execute("""
           SELECT EXISTS (SELECT 1 FROM pg_database WHERE datname=%s);
           """, (dbname,))
        if not cur.fetchone()[0]:
            cur.execute('CREATE DATABASE %s;', (dbname,))
    con.close()

def create_tables(con):
    with con.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS clients (
                id serial primary key,
                name varchar(35),
                surname varchar(35)
            );
            CREATE TABLE IF NOT EXISTS clients_ememails (
                id serial references clients(id),
                email varchar(255)
            );
            CREATE TABLE IF NOT EXISTS clients_phone_numbers (
                id serial references clients(id),
                tel varchar(15)
            );
        """)
        con.commit()

def add_client(con, name, surname, emails=None, phone_numbers=None):
    with con.cursor() as cur:
        cur.execute("""
            INSERT INTO clients (name, surname) 
            VALUES (%(name)s, %(surname)s)
            RETURNING id
        """, {'name': name, 'surname': surname}
        )
        cid =  cur.fetchone()[0]
        con.commit()
        if emails:
            add_emails(con, cid=cid, emails=emails)
        if phone_numbers:
            add_phone_numbers(con, cid, phone_numbers)
        return cid

def add_emails(con, cid, emails):
    with con.cursor() as cur:
        cur.executemany("""
            INSERT INTO clients_emails (id, email) VALUES (%s, %s);
        """, ((str(cid), _ ) for _ in emails))
        con.commit()

def add_phone_numbers(con, cid, phone_numbers):
    with con.cursor() as cur:
        cur.executemany("""
            INSERT INTO clients_phone_numbers (id, tel) VALUES (%s, %s);
        """, ((str(cid), _ ) for _ in phone_numbers))
        con.commit()

def change_client_name(con, cid, name=None, surname=None): 
    with con.cursor() as cur:
        query = sql.SQL("UPDATE clients SET {} WHERE id = {};").format(
            sql.SQL(',').join((
                sql.SQL("name = {}" if name else '').format(sql.Literal(name)),
                sql.SQL("surname = {}" if surname else '').format(
                    sql.Literal(surname)))),
            sql.Literal(cid))
        cur.execute(query)
        con.commit()

def delete_email(con, cid, phone_number):
    with con.cursor() as cur:
        cur.execute("""
            DELETE FROM clients_emails 
            WHERE email = $(emails)s AND id = %(cid)s;
        """, {'phone_number': phone_number, 'cid': cid})
        cur.execute(query)
        con.commit()

def delete_phone_number(con, cid, phone_number):
    with con.cursor() as cur:
        cur.execute("""
            DELETE FROM clients_phone_numbers 
            WHERE tel = %(phone_number)s AND id = %(cid)s;
        """, {'phone_number': phone_number, 'cid': cid})
        con.commit()

def delete_client(con, cid):
    with con.cursor() as cur:
        cur.execute("""
            DELETE FROM clients_emails WHERE id = %(cid)s;
            DELETE FROM clients_phone_numbers WHERE id = %(cid)s;
            DELETE FROM clients WHERE id = %(cid)s;
        """, {'cid': cid})
        con.commit()
    pass

def find_clients(con, name=None, surname=None, 
        emails=None, phone_numbers=None):
    with con.cursor() as cur:
        query = sql.SQL("""
            SELECT DISTINCT id FROM clients 
            JOIN clients_emails USING(id)
            JOIN clients_phone_numbers USING(id)
            WHERE {};""").format(
                sql.SQL(' AND ').join((
                    (sql.SQL("name LIKE {}").format(sql.Literal(name)) 
                        if name else sql.SQL('True')),
                    (sql.SQL("surname LIKE {}").format(sql.Literal(surname)) 
                        if surname else sql.SQL('True')),
                    (sql.SQL("email IN ({})").format(sql.SQL(',').join(
                            sql.Literal(_) for _ in emails))
                        if emails else sql.SQL('True')),
                    (sql.SQL("tel IN ({})").format(sql.SQL(',').join(
                            sql.Literal(_) for _ in phone_numbers)) 
                        if phone_numbers else sql.SQL('True')))))
        cur.execute(query)   
        return cur.fetchall()
    pass


def clear_clients(con):
    with con.cursor() as cur:
        cur.execute("""
           DELETE FROM clients_emails;
           DELETE FROM clients_phone_numbers;
           DELETE FROM clients;
        """)
        con.commit()

def show_table(con, table):
    with con.cursor() as cur:
        cur.execute(sql.SQL('table {};').format(sql.Identifier(table)))
        print('table ' + table + ':\n'+'\n'.join(str(_) for _ in cur.fetchall()))

create_database(user='postgres', dbname='clients',
                host='localhost', password='postgres')
con = connect(user='postgres', database='clients', 
              host = 'localhost', password='postgres')

print('\n create_tables(con):\n')
create_tables(con)
clear_clients(con)
show_table(con, 'clients')
show_table(con, 'clients_emails')
show_table(con, 'clients_phone_numbers')

print('\n add clients:\n')
cid = add_client(con, 'NAME1', 'SUR3', ('e11', 'e12'),('8-098-7532', '12345'))
add_client(con, 'NAME2', 'SUR2', ('e13', 'e22'),('8-5345-7532', '43345'))
add_client(con, 'NAME3', 'SUR1', ('e7',), ('812-7532', '12'))
show_table(con, 'clients')
show_table(con, 'clients_emails')
show_table(con, 'clients_phone_numbers')

print("\n add_phone_numbers(con, cid, ('8-098-7532', '12345'):")
add_phone_numbers(con, cid, ('8-123-23532', '54432345'))
show_table(con, 'clients_phone_numbers')

print("\n change_client_name(con, cid, name='mew NAME', surname='new SURNAME'):")
change_client_name(con, cid, name='mew NAME', surname='new SURNAME')
show_table(con, 'clients')

print("\n delete_phone_number(con, cid, '8-098-7532):")
delete_phone_number(con, cid, '8-098-7532')
show_table(con, 'clients_phone_numbers')
        
print("\n delete_client(con, cid):")
delete_client(con, cid)
show_table(con, 'clients')
show_table(con, 'clients_emails')
show_table(con, 'clients_phone_numbers')

print("\n find('NA%2','%SUR%',('e22',),('43345', '43456')): \n" 
        + str(find_clients(con, 'NA%2','%SUR%',('e22',),('43345', '43456'))))
print("\n find(con, emails=('e%2', 'e1%'))): \n" 
        + str(find_clients(con, emails=('e22', 'e7'))))
print("\n find(con, name=('new NAME')): \n" 
        + str(find_clients(con, name=('new NAME'))))


con.close()

