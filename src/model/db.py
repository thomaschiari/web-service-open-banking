import sqlite3
from pathlib import Path


# Operações basicas
FILE = Path(__file__).resolve()
src_folder = FILE.parents[0]
rel_arquivo_db = Path('base.db')
db = Path(src_folder / rel_arquivo_db).resolve()

def select_query(sql_command):
    con = sqlite3.connect(db.resolve())
    cur = con.cursor()
    cur.execute(sql_command)
    rows = cur.fetchall()
    con.close()
    return rows