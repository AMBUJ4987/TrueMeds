from ocr import extract_text
from parser import parse
from matcher import match_drug

ocr = extract_text("demo.jpg")

parsed = parse(ocr["ocr_text"])

match = match_drug(parsed["drug_name"])

print(match)