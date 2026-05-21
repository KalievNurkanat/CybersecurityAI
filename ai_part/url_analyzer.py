from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from data.urls import malicious_urls, safe_urls

keywords = [
    "login",
    "verify",
    "secure",
    "bank",
    "paypal",
    "password",
    "confirm",
]


def extract_url_features(url):
    return [
        len(url),
        sum(c.isdigit() for c in url),
        url.count("-"),
        int(any(k in url for k in keywords)),
        int(url.endswith(".ru")),
        int(url.endswith(".xyz")),
        int(url.endswith(".click")),
    ]

all_urls = malicious_urls + safe_urls

X_url = [extract_url_features(url) for url, _ in all_urls]
y_url = [label for _, label in all_urls]



X_train, X_test, y_train, y_test = train_test_split(
    X_url,
    y_url,
    test_size=0.2,
    random_state=42
)

url_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

url_model.fit(X_train, y_train)


