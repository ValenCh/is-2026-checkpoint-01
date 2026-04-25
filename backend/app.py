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
        
        # Query con JOIN y STRING_AGG para evitar filas duplicadas cuando un miembro tiene más de 1 feature
        query = '''
            SELECT 
                m.id,
                m.nombre,
                m.apellido,
                m.legajo,
                m.estado,
                COALESCE(STRING_AGG(f.feature, ' / '), 'Sin asignar') AS feature,
                COALESCE(STRING_AGG(f.servicio, ' / '), 'Sin asignar') AS servicio
            FROM members m
            LEFT JOIN features f ON m.id = f.member_id
            GROUP BY m.id, m.nombre, m.apellido, m.legajo, m.estado
            ORDER BY m.id ASC;
        '''
        
        cur.execute(query)
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