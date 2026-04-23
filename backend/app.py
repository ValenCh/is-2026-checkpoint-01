import os
from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
# CORS necesario para que el frontend (puerto 8080) consulte al backend (puerto 5000)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ['DB_HOST'],
        port=os.environ['DB_PORT'],
        database=os.environ['DB_NAME'],
        user=os.environ['DB_USER'],
        password=os.environ['DB_PASS']
    )

@app.route('/api/health')
def health():
    return jsonify({"status": "active"}), 200

@app.route('/api/team')
def team():
    try:
        conn = get_db_connection()
        cur = conn.cursor(cursor_factory=RealDictCursor)
        cur.execute('SELECT * FROM members ORDER BY id ASC;')
        members = cur.fetchall()
        cur.close()
        conn.close()
        return jsonify(members)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/api/info')
def info():
    return jsonify({
        "service": "TeamBoard API",
        "version": "1.0",
        "language": "Python 3.12"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)