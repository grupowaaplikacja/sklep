#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sqlite3, hashlib
connection=sqlite3.connect('database.db')
cursor=connection.cursor()

cursor.execute('''create table if not exists user_account(id integer primary key asc, email text unique not null, userpass text not null, f_name text not null, l_name text, phone text, role integer default 1)''')
cursor.execute('''create table if not exists product_info(id integer primary key asc, p_name text, p_desc text, p_price integer, p_stock integer)''')
cursor.execute('''create table if not exists user_address(id integer references user_account(id), f_address text, s_address text)''')
cursor.execute("insert into user_account values(null, 'admin@localhost.com', '"+hashlib.sha256(b'password').hexdigest()+"','Admin','Admin', '000000000',0)")
connection.commit()
connection.close()

connection=sqlite3.connect('database2.db')
cursor=connection.cursor()

cursor.execute('''create table if not exists user_account(id integer primary key asc, email text unique not null, userpass text not null, f_name text not null, l_name text, phone text, f_address text default null, s_address text default null, role integer default 1)''')
cursor.execute('''create table if not exists product_info(id integer primary key asc, p_name text, p_desc text, p_price integer, p_stock integer)''')
cursor.execute("insert into user_account values(null, 'admin@localhost.com', '"+hashlib.sha256(b'password').hexdigest()+"','Admin','Admin', '000000000','','',0)")
connection.commit()
connection.close()

# dodac tabele zawierajaca informacje o wszystkich zamowieniach
