import sqlite3
import pandas as pd

conn = sqlite3.connect("C:/SQLite/internship.db")
df = pd.read_sql_query("SELECT * FROM students", conn)
print(df)