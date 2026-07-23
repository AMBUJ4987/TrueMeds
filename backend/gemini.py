import os
import json

from dotenv import load_dotenv
from google import genai


load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def extract_fields(ocr_text):

    prompt = f"""
You are an expert at reading medicine packaging.

Extract the following information from the OCR text.

Return ONLY valid JSON.

Fields:
- drug_name
- manufacturer
- batch_number
- manufacturing_date
- expiry_date
- strength

If unavailable, return null.

OCR TEXT:

{ocr_text}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()

    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)


if __name__ == "__main__":

    sample = """
mg SCHEDULERE SORPTION

B.No.BM325171

Metronidazole IP

400 mg

J.B. Chemicals

EXP JUN29
"""

    print(extract_fields(sample))