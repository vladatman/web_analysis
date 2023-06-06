import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


data = pd.read_csv('website_classification.csv')


le = LabelEncoder()
data['Category'] = le.fit_transform(data['Category'])

X = data['cleaned_website_text']
y = data['Category']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

vectorizer = TfidfVectorizer()
X_train = vectorizer.fit_transform(X_train)
X_test = vectorizer.transform(X_test)

model = MultinomialNB()
model.fit(X_train, y_train)

predictions = model.predict(X_test)
print("Accuracy: ", accuracy_score(y_test, predictions))
new_data = ["ukr.net"]

new_data = vectorizer.transform(new_data)

predictions = model.predict(new_data)

predicted_categories = le.inverse_transform(predictions)

print(predicted_categories)
