from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from data.texts import text_data, safe_text_data

all_text_data = text_data + safe_text_data

texts = [x[0] for x in all_text_data]
labels = [x[1] for x in all_text_data]

X_train, X_test, y_train, y_test = train_test_split(
    texts,
    labels,
    test_size=0.2,
    random_state=42
)

text_model = Pipeline([
    ("tfidf", TfidfVectorizer()),
    ("clf", LogisticRegression())
])

text_model.fit(X_train, y_train)


