import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report

emails = {
    'text': [
        'Win a free iPhone now click here',
        'Meeting scheduled for tomorrow',
        'Limited offer buy now',
        'Project deadline is next week',
        'Congratulations you won a lottery',
        'Let us discuss the report',
        'Cheap meds available online',
        'Team lunch at 1 pm'
    ],
    'length': [35, 30, 28, 32, 40, 27, 33, 25],
    'links': [1, 0, 1, 0, 1, 0, 1, 0],
    'sender': ['unknown', 'company', 'unknown', 'company', 'unknown', 'company', 'unknown', 'company'],
    'label': [1, 0, 1, 0, 1, 0, 1, 0]
}
df = pd.DataFrame(emails)
vectorizer = TfidfVectorizer()
text_features = vectorizer.fit_transform(df['text']).toarray()
sender_encoded = pd.get_dummies(df['sender'], drop_first=True)
X = pd.concat([pd.DataFrame(text_features), df[['length', 'links']], sender_encoded], axis=1)
y = df['label']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)
model = LogisticRegression()
model.fit(X_train, y_train)
pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, pred))
print(classification_report(y_test, pred))
new_mail = ['Free money waiting for you click now']
new_text = vectorizer.transform(new_mail).toarray()
new_extra = pd.DataFrame([[38, 1, 1]])
new_input = pd.concat([pd.DataFrame(new_text), new_extra], axis=1)
print("Spam Prediction:", model.predict(new_input)[0])
