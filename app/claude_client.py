import anthropic
import os

client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

SYSTEM_PROMPT = """
คุณคือ "เลขา" ผู้ช่วยส่วนตัวบน LINE ที่ช่วยจัดการรายรับรายจ่าย
พูดจาเป็นกันเอง กระชับ ตอบเป็นภาษาไทย
ตอนนี้อยู่ใน Phase 1 ยังไม่มีระบบบันทึกข้อมูล — ให้บอกผู้ใช้ว่า
"รับทราบแล้วนะ ระบบบันทึกกำลังจะมาเร็ว ๆ นี้เลย!" 
แต่คุยได้ปกติในทุกเรื่องทั่วไปก่อน
"""

def chat(user_message: str, user_id: str) -> str:
    """ส่งข้อความให้ Claude และรับคำตอบกลับ"""
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=1000,
        system=SYSTEM_PROMPT,
        messages=[
            {"role": "user", "content": user_message}
        ]
    )
    return response.content[0].text