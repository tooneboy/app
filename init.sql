-- สร้างตารางผู้ใช้
CREATE TABLE IF NOT EXISTS users ( 
    id INT AUTO_INCREMENT PRIMARY KEY, 
    username VARCHAR(255) NOT NULL, 
    password VARCHAR(255) NOT NULL
);

-- เพิ่มข้อมูลผู้ใช้สำหรับทดสอบ
INSERT INTO users (username, password) VALUES ('admin@example.com', '1234');
INSERT INTO users (username, password) VALUES ('student@example.com', 'abcd');