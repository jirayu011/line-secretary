import google.generativeai as genai
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

SYSTEM_PROMPT = """
คุณคือ "เลขา" ผู้ช่วยส่วนตัวบน LINE ที่ช่วยจัดการรายรับรายจ่าย
พูดจาเป็นกันเอง กระชับ ตอบเป็นภาษาไทย
ตอนนี้อยู่ใน Phase 1 ยังไม่มีระบบบันทึกข้อมูล
"""

def chat(user_message: str, user_id: str) -> str:
    prompt = f"""
{SYSTEM_PROMPT}

ผู้ใช้:
{user_message}
"""

    response = model.generate_content(prompt)

    return response.text