from flask import Flask, jsonify
import pymysql

app = Flask(__name__)

# =======================
# DB Config Info
# =======================
HOST = "localhost"
USER = "root"
PASSWORD = "root"
DB_NAME = "company_db"
TABLE_NAME = "employees"

# ======================
# Get All Employees
# ======================
@app.route('/employees', methods=['GET'])
def get_users():
    try:
        # Connect to DB
        connection = pymysql.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME,
            cursorclass=pymysql.cursors.DictCursor      # rows as dict
        )

        with connection.cursor() as cursor:
            cursor.execute(f"SELECT * FROM {TABLE_NAME} LIMIT 10;")
            employees = cursor.fetchall()

        # Return only the employees data
        return jsonify(employees)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

    finally:
        if 'connection' in locals():
            connection.close()

# =========================
# Health Check
# =========================
@app.route('/')
def index():
    return "Localhost API running"

# =========================
# Entry Point
# =========================
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)