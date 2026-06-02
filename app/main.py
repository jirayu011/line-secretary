from fastapi import FastAPI, Request, HTTPException
from linebot.v3 import WebhookParser
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
import os
from dotenv import load_dotenv
from app.line_handler import reply_text
from app.claude_client import chat

load_dotenv()

app = FastAPI()
parser = WebhookParser(os.getenv("LINE_CHANNEL_SECRET"))

@app.get("/")
def root():
    return {"status": "Line Secretary is running! 🤖"}

@app.post("/webhook")
async def webhook(request: Request):
    # ตรวจสอบว่า request มาจาก LINE จริง
    signature = request.headers.get("X-Line-Signature", "")
    body = await request.body()
    body_text = body.decode("utf-8")

    try:
        events = parser.parse(body_text, signature)
    except InvalidSignatureError:
        raise HTTPException(status_code=400, detail="Invalid signature")

    for event in events:
        # รับเฉพาะข้อความ text
        if isinstance(event, MessageEvent) and isinstance(event.message, TextMessageContent):
            user_id = event.source.user_id
            user_message = event.message.text

            # ส่งให้ Claude แล้วตอบกลับ
            reply = chat(user_message, user_id)
            reply_text(event.reply_token, reply)

    return {"status": "ok"}