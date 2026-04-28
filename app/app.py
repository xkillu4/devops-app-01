from flask import Flask, jsonify, request
import psycopg2
import os
import time

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("POSTGRES_HOST", "db"),
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD")
    )

def init_db():
    retries = 10

    while retries > 0:
        try:
            conn = get_db_connection()
            cur = conn.cursor()

            cur.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id SERIAL PRIMARY KEY,
                    name TEXT
                );
            """)

            conn.commit()
            cur.close()
            conn.close()

            print("Database initialized successfully")
            return

        except Exception as e:
            retries -= 1
            print(f"Database not ready yet. Retries left: {retries}. Error: {e}")
            time.sleep(3)

    raise Exception("Could not connect to the database after several retries")

@app.route("/", methods=["GET"])
def home():
    return "App DevOps funcionando"

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "ok"})

@app.route("/users", methods=["GET"])
def get_users():
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("SELECT id, name FROM users;")
        rows = cur.fetchall()

        cur.close()
        conn.close()

        return jsonify([{"id": row[0], "name": row[1]} for row in rows])

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route("/users", methods=["POST"])
def add_user():
    try:
        data = request.get_json()

        if not data or "name" not in data:
            return jsonify({"error": "Name is required"}), 400

        conn = get_db_connection()
        cur = conn.cursor()

        cur.execute("INSERT INTO users (name) VALUES (%s);", (data["name"],))
        conn.commit()

        cur.close()
        conn.close()

        return jsonify({"message": "User created", "name": data["name"]}), 201

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000)
