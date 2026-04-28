from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

@app.route("/")
def home():
    return "App DevOps funcionando"

@app.route("/health")
def health():
    return jsonify({"status": "ok"})

@app.route("/users")
def users():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            name TEXT
        );
    """)

    cur.execute("INSERT INTO users (name) VALUES (%s);", ("Killua",))
    conn.commit()

    cur.execute("SELECT id, name FROM users;")
    rows = cur.fetchall()

    cur.close()
    conn.close()

    return jsonify([{"id": row[0], "name": row[1]} for row in rows])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
