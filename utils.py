import re

def detect_sensitive_data(text):
    findings = []

    if not text:
        return findings

    email_pattern = r"[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+"
    phone_pattern = r"\b\d{10}\b"
    api_key_pattern = r"(?i)api[_-]?key\s*=\s*['\"]?[A-Za-z0-9]{16,}['\"]?"

    if re.search(email_pattern, text):
        findings.append("Possible Email Detected")

    if re.search(phone_pattern, text):
        findings.append("Possible Phone Number Detected")

    if re.search(api_key_pattern, text):
        findings.append("Possible API Key Detected")

    return findings