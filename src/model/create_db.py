import sqlite3
import pandas as pd
from pathlib import Path

# Armazenando referância para raiz do projeto
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]


def create_db(path_db):
    con = sqlite3.connect(path_db.resolve())
    cur = con.cursor()
    table_name = 'tbl_user'
    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    sql_command = f'''CREATE TABLE {table_name} (
        "usr_id"	INTEGER PRIMARY KEY,
        "name"   TEXT,
        "email"	TEXT,
        "cpf"	TEXT
    )'''
    cur.execute(sql_command)
    table_name = 'tbl_bank'
    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    sql_command = f'''CREATE TABLE {table_name} (
        "bank_id"	INTEGER PRIMARY KEY,
        "usr_id"   INTEGER,
        "bank"	TEXT,
        "account"	TEXT,
        "info_available"	TEXT
    )'''
    cur.execute(sql_command)
    table_name = 'tbl_transaction'
    cur.execute(f'DROP TABLE IF EXISTS {table_name}')
    sql_command = f'''CREATE TABLE {table_name} (
        "transaction_id"	INTEGER PRIMARY KEY,
        "bank_id"   INTEGER,
        "amount"	TEXT,
        "date"	TEXT,
        "description"	TEXT
    )'''
    cur.execute(sql_command)
    con.commit()
    con.close()

def load_table_user(path_db, path_csv):
    list_of_dicts = []
    data = pd.read_csv(path_csv.resolve(), encoding="utf-8")
    list_of_dicts = list(data[['id', 'name', 'email', 'cpf']].dropna().head(2000).itertuples(index=False, name=None))
    con = sqlite3.connect(path_db.resolve())
    sql_command = "INSERT INTO tbl_user(usr_id, name, email, cpf) VALUES (?, ?, ?, ?)"
    con.executemany(sql_command, list_of_dicts)
    con.commit()
    con.close()

def load_table_bank(path_db, path_csv):
    list_of_dicts = []
    data = pd.read_csv(path_csv.resolve(), encoding="utf-8")
    list_of_dicts = list(data[['bank_id', 'usr_id', 'bank', 'account', 'info_available']].dropna().head(2000).itertuples(index=False, name=None))
    con = sqlite3.connect(path_db.resolve())
    sql_command = "INSERT INTO tbl_bank(bank_id, usr_id, bank, account, info_available) VALUES (?, ?, ?, ?, ?)"
    con.executemany(sql_command, list_of_dicts)
    con.commit()
    con.close()

def load_table_transaction(path_db, path_csv):
    list_of_dicts = []
    data = pd.read_csv(path_csv.resolve(), encoding="utf-8")
    list_of_dicts = list(data[['transaction_id', 'bank_id', 'amount', 'date', 'description']].dropna().head(2000).itertuples(index=False, name=None))
    con = sqlite3.connect(path_db.resolve())
    sql_command = "INSERT INTO tbl_transaction(transaction_id, bank_id, amount, date, description) VALUES (?, ?, ?, ?, ?)"
    con.executemany(sql_command, list_of_dicts)
    con.commit()
    con.close()

def main():
    rel_arquivo_db =  Path('base.db')
    caminho_arquivo_db = src_folder / rel_arquivo_db

    rel_arquivo_csv =  Path('csv_users.csv')
    caminho_arquivo_csv = src_folder / rel_arquivo_csv

    create_db(caminho_arquivo_db)
    load_table_user(caminho_arquivo_db, caminho_arquivo_csv)

    rel_arquivo_csv =  Path('table_bankinfo.csv')
    caminho_arquivo_csv = src_folder / rel_arquivo_csv

    load_table_bank(caminho_arquivo_db, caminho_arquivo_csv)

    rel_arquivo_csv =  Path('table_transactions.csv')
    caminho_arquivo_csv = src_folder / rel_arquivo_csv

    load_table_transaction(caminho_arquivo_db, caminho_arquivo_csv)

