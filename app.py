import mysql.connector
import time
import os #env variable oluşturmak için

env = os.getenv("APP_ENV", "dev") # 1.si yoksa 2.yi kullan 

message = f"Bu kayıt {env.upper()} ortamından geldi"

for _ in range(10):
    try:
        db = mysql.connector.connect(
            host="db", # compose service name
            user="root",
            password="root",
            database="logs"
        )
        break
    except:
        time.sleep(3)

cursor = db.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS records (
    id INT AUTO_INCREMENT PRIMARY KEY,
    text VARCHAR(255)
)
""")

cursor.execute(
    "INSERT INTO records (text) VALUES (%s)",
    (message,)
)

db.commit()
print(message)
db.close()