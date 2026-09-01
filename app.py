import sqlite3
from flask import Flask, request

app = Flask(name)

@app.route('/user')
def get_user():
    user_id = request.args.get('id')
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    # ⚠️ Vulnerable: SQL injection
    query = "SELECT  FROM users WHERE id = '" + user_id + "'"
    cursor.execute(query)

    result = cursor.fetchall()
    conn.close()
    return str(result)

if name == 'main':
    app.run()
