FROM python:3.9-slim

WORKDIR /app

# 1. COPY requirements.txt ก่อนติดตั้ง
COPY requirements.txt .

# 2. ติดตั้ง dependencies ของระบบปฏิบัติการ (สำหรับ MySQL Connector)
RUN apt-get update && \
    apt-get install -y default-libmysqlclient-dev gcc && \
    rm -rf /var/lib/apt/lists/*

# 3. ติดตั้ง Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# 4. COPY ไฟล์โค้ดและ HTML ที่เหลือ
COPY app.py .
COPY templates/ templates/
#COPY home.html . 
COPY init.sql . 

EXPOSE 5000
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0"]