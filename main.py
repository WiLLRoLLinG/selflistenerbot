from pyrogram import Client, filters
import time
import logging

# تنظیمات اتصال به تلگرام
api_id = '3540117'
api_hash = '756860e1fcd4e47ab7a181b57cbba792'
session_name = 'self_bot'

# شروع کلاینت Pyrogram
app = Client(session_name, api_id=api_id, api_hash=api_hash)

# ثبت گزارشات (Logging)
logging.basicConfig(level=logging.INFO)

# هندلر برای پیام‌های جدید در یک چت خاص
@app.on_message(filters.chat('@GmailBot') & filters.text)

def check_and_forward(client, message):
    
    try:
        # بررسی پیام برای محتوای خاص
        if ('Sahil Bloom' in message.text or
    'James Clear' in message.text or
    'Tim Ferriss' in message.text):
            # فوروارد پیام به کانال هدف
            client.forward_messages('@bullsherandkososhit', message.chat.id, message.message_id)
            
    except Exception as e:
        logging.error(f"Error occurred: {e}")

# اجرای ربات
while True:
    try:
        app.run()
    except Exception as e:
        # در صورت خطا، ربات مجدداً تلاش می‌کند
        logging.error(f"App crashed, restarting... {e}")
        time.sleep(5)  # مکث قبل از تلاش دوباره
