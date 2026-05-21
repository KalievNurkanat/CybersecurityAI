from ai_part.text_analyzer import text_model
from ai_part.url_analyzer import extract_url_features, url_model
from ai_part.sender_analyze import extract_sender_features, sender_model

def text_risk(text_score): 
    text_score = text_score * 100
    if text_score > 65:
        return "Подозрительный слова в сообщении: просят личные данные, торопят"
    else:
        return "Сообщение не вызывает подозрений"
    
def url_risk(url_score):
    url_score = url_score * 100
    if url_score > 60:
        return "Подозрительная ссылка. Ссылка отличается от оригинального: имеются подозрительные символы"
    else:
        return "Ссылка не вызывает подозрений"
    
def sender_risk(sender_score):
    sender_score = sender_score * 100
    if sender_score > 60:
        return "Подозрительная отправитель. Почта отличается от оригинального: имеются подозрительные символы"
    else:
        return "Отправитель не вызывает подозрений"

def analyze_request(text, url, sender):
    text_score = text_model.predict_proba([text])[0][1]
    url_features = extract_url_features(url)
    url_score = url_model.predict_proba([url_features])[0][1]
    sender_features = extract_sender_features(sender)
    sender_score = sender_model.predict_proba([sender_features])[0][1]
   

    final_score = (
        text_score * 0.4 +
        url_score * 0.3 +
        sender_score * 0.3
    )

    reasons = {
        "Отправитель": sender_risk(sender_score),
        "Сообщение": text_risk(text_score),
        "Ссылка": url_risk(url_score)
    }

    return {
        "text_risk": f"{round(text_score * 100, 2)} %",
        "url_risk": f"{round(url_score * 100, 2)} %",
        "sender_risk": f"{round(sender_score * 100, 2)} %",
        "total_risk_score": f"{int(final_score * 100)} %",
        "is_phishing": final_score > 0.6,
        "data": reasons 
    }
