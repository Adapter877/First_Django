# Dockerfile
FROM python:3.11-slim

# ตั้งค่าพื้นฐาน
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# ตั้ง working directory ใน container
WORKDIR /app

# คัดลอก requirements และติดตั้ง dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# คัดลอกไฟล์ทั้งหมดของโปรเจกต์เข้า container
COPY . .

# เปิดพอร์ต 8000 สำหรับเข้าถึง Django
EXPOSE 8000

# รัน Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
