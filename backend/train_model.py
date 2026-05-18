import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import PassiveAggressiveClassifier

fake = pd.read_csv('../dataset/Fake.csv')
true = pd.read_csv('../dataset/True.csv')

fake['label'] = 0
true['label'] = 1

news = pd.concat([fake, true])

x = news['text']
y = news['label']

x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

vectorizer = TfidfVectorizer(stop_words='english')

xv_train = vectorizer.fit_transform(x_train)

model = PassiveAggressiveClassifier(max_iter=50)

model.fit(xv_train, y_train)

pickle.dump(model, open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))

print("Model Trained Successfully")