from fastapi import FastAPI, Request, HTTPException
from dotenv import load_dotenv
from linebot.v3 import WebhookParser
from linebot.v3.exceptions import InvalidSignatureError
from linebot.v3.webhooks import MessageEvent, TextMessageContent
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    ReplyMessageRequest,
    TextMessage
)
import os

load_dotenv()

app = FastAPI()

parser = WebhookParser(
    os.getenv("LINE_CHANNEL_SECRET")
)

configuration = Configuration(
    access_token=os.getenv("LINE_CHANNEL_ACCESS_TOKEN")
)

@app.get("/")
def root():
    return {"status": "Line Secretary is running! 🤖"}

@app.post("/webhook")
async def webhook(request: Request):

    signature = request.headers.get(
        "X-Line-Signature", ""
    )

    body = await request.body()
    body_text = body.decode("utf-8")

    try:
        events = parser.parse(
            body_text,
            signature
        )

    except InvalidSignatureError:
        raise HTTPException(
            status_code=400,
            detail="Invalid signature"
        )

    for event in events:

        if (
            isinstance(event, MessageEvent)
            and isinstance(
                event.message,
                TextMessageContent
            )
        ):

            with ApiClient(configuration) as api_client:

                line_bot_api = MessagingApi(
                    api_client
                )

                line_bot_api.reply_message(
                    ReplyMessageRequest(
                        reply_token=event.reply_token,
                        messages=[
                            TextMessage(
                                text="สวัสดีครับ ผมคือเลขาของคุณ 🤖"
                            )
                        ]
                    )
                )

    return {"status": "ok"}