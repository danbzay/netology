from psycopg2 import connect
import sys
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

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
            CREATE TABLE IF NOT EXISTS clients_emails (
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
            INSERT INTO clients_phone_numbers (id, email) VALUES (%s, %s);
        """, ((str(cid), _ ) for _ in phone_numbers))
        con.commit()

def change_client_name(con, cid, name=None, surname=None) 
    with con.cursor() as cur:
        cur.execute('UPDATE clients SET'
             + ('name = $(name)s,' if name else '')
             + ('surname = $(surname)s,' if surname else '')
             + 'WHERE id = %(cid)s;', 
        {'name': name, 'surname': surname, 'cid': cid})
        cur.execute(query)

def delete_phone_number(con, cid, phone_number):
    with con.cursor() as cur:
        cur.execute("""
            DELETE FROM clients_phone_nubmers 
            WHERE tel = $(phone_number)s AND id = %(cid)s;
        """, {'phone_number': phone_number, 'cid': cid})
        cur.execute(query)

def delete_client(con, cid):
    with con.cursor() as cur:
        cur.execute("""
            DELETE FROM clients_emails WHERE id = %(cid)s;
            DELETE FROM clients_phone_nubmers WHERE id = %(cid)s;
            DELETE FROM clients WHERE id = %(cid)s;
        """, {'cid': cid})
        cur.execute(query)
    pass

def find_clients(con, name=None, surname=None, 
        emails=None, phone_numbers=None):
    with con.cursor() as cur:
        cids = cur.fetchall("""
            SELECT id FROM clients 
            JOIN cients_emails USING(id)
            JOIN cients_phone_numbers USING(id)
            
