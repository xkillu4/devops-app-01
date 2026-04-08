from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="db",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route("/")
def home():
    return "App DevOps funcionando"

@app.route("/users")
    def users():
        conn = get_db_connection()
        cur = conn.cursor()

#crear tabla si no existe
cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT
    );
"""")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
