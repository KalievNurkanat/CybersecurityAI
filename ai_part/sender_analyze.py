from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from data.sender import malicious_senders, safe_senders

keywords = [
    "login",
    "verify",
    "secure",
    "bank",
    "paypal",
    "password",
    "confirm",
]


def extract_sender_features(url):
    return [
        len(url),
        sum(c.isdigit() for c in url),
        url.count("-"),
        int(any(k in url for k in keywords)),
        int(url.endswith(".ru")),
        int(url.endswith(".xyz")),
        int(url.endswith(".click")),
    ]

all_senders = malicious_senders + safe_senders

X_sender = [extract_sender_features(url) for url, _ in all_senders]
y_sender = [label for _, label in all_senders]



X_train, X_test, y_train, y_test = train_test_split(
    X_sender,
    y_sender,
    test_size=0.2,
    random_state=42
)

sender_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

sender_model.fit(X_train, y_train)
