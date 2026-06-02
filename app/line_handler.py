from linebot.v3.messaging import (
    ApiClient, Configuration, MessagingApi,
    ReplyMessageRequest, TextMessage
)
import os

def get_line_api() -> MessagingApi:
    configuration = Configuration(
        access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
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