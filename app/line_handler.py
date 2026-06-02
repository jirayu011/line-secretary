from linebot.v3.messaging import (
    ApiClient, Configuration, MessagingApi,
    ReplyMessageRequest, TextMessage
)
import os

def get_line_api() -> MessagingApi:
    configuration = Configuration(
        access_token=os.getenv("okrqAYHi7k5oZXfHaNgZlLySDum9PDmvo0UgEu17FDS42xPHXLQ4TsTvyqtFKLWawwRiAdRpfOwJsOyHESjdNkKYU/ddxBl60FibuU43U0ghjEltPanC4GLf2erUJxEiI+1Nee90IzUHTT/ieIf3rAdB04t89/1O/w1cDnyilFU=")
    )
    api_client = ApiClient(configuration)
    return MessagingApi(api_client)

def reply_text(reply_token: str, text: str):
    """ตอบกลับข้อความหา LINE user"""
    line_api = get_line_api()
    line_api.reply_message(
        ReplyMessageRequest(
            reply_token=reply_token,
            messages=[TextMessage(text=text)]
        )
    )