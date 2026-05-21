import base64
import requests
import re

def get_latest_email(access_token):
    gmail_response = requests.get(
        "https://gmail.googleapis.com/gmail/v1/users/me/messages",
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    messages = gmail_response.json().get("messages", [])

    if not messages:
        return None

    message_id = messages[0]["id"]

    message_response = requests.get(
        f"https://gmail.googleapis.com/gmail/v1/users/me/messages/{message_id}",
        params={"format": "full"},
        headers={
            "Authorization": f"Bearer {access_token}"
        }
    )

    message_data = message_response.json()
    payload = message_data.get("payload", {})
    headers = payload.get("headers", [])

    sender = None
    subject = None

    for header in headers:
        if header.get("name") == "From":
            sender = header.get("value")

        if header.get("name") == "Subject":
            subject = header.get("value")
    
    body = ""
    parts = payload.get("parts", [])

    for part in parts:
        if part.get("mimeType") == "text/plain":
            data = part["body"].get("data")
            if data:
                body = base64.urlsafe_b64decode(
                    data
                ).decode("utf-8")
                break

    url = re.findall(r'https?://\S+', body)
    text = re.findall(r'[^\W\d_]+', body)
    clean_text = ' '.join(text)
    url = url[0] if url else ""

    return {
        "sender": sender,
        "subject": subject,
        "url": url,
        "text": clean_text
    }