from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
import os

app = Flask(__name__)
app.secret_key = 'your_super_secret_key_here' 

# ฟังก์ชันสำหรับเชื่อมต่อฐานข้อมูล
def get_db_connection():
    connection = mysql.connector.connect(
        host=os.environ.get('DB_HOST', 'db'),
        user=os.environ.get('DB_USER', 'root'),
        password=os.environ.get('DB_PASSWORD', '1234'),
        database=os.environ.get('DB_NAME', 'login_system')
    )
    return connection

@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/login', methods=['GET'])
def show_login_form():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def handle_login():
    # --- เริ่มส่วนดักจับ Error ---
    try:
        username_input = request.form.get('username')
        password_input = request.form.get('password')

        # ลองเชื่อมต่อฐานข้อมูล
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # ลองค้นหาข้อมูล
        query = "SELECT * FROM users WHERE username = %s AND password = %s"
        cursor.execute(query, (username_input, password_input))
        user = cursor.fetchone()

        # ปิดการเชื่อมต่อ
        cursor.close()
        conn.close()
        
        # ตรวจสอบผลลัพธ์
        if user:
            flash(f'ยินดีต้อนรับคุณ {user["username"]}', 'success')
            return redirect(url_for('home')) 
        else:
            flash('ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง', 'error')
            return redirect(url_for('show_login_form'))

    except Exception as e:
        # ถ้าพังตรงไหน ให้แสดง Error ออกมาทางหน้าจอแทนจอขาว
        print(f"Error Occurred: {e}") # ปริ้นท์ลง Console ด้วย
        flash(f'เกิดข้อผิดพลาดของระบบ: {str(e)}', 'error')
        return redirect(url_for('show_login_form'))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)