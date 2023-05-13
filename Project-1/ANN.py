from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import json
import json
import numpy as np
import pandas as pd
import preprocess

# JSON dosyasını veriler okunuyor
with open("articles.json", encoding="utf-8") as f:
    data = json.load(f)
    df = pd.DataFrame(data)

# Veriler hazırlanıyor
    X = []
    y = []
    for item in data:
        X.append(preprocess.preprocess_text(item["text"]))
        y.append(item["category"])

# Kelime dağarcığı oluşturuluyor
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Veriler eğitim ve test verileri olarak ayırılıyor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Yapay sinir ağı modeli oluşturuluyor
clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)

# Model eğitiliyor
clf.fit(X_train, y_train)

# Test verileri ile modeli değerlendiriliyor ve Accuracy ile diğer başarı metrikleri ekrana yazdırılıyor
y_pred = clf.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("\033[91mAccuracy:\033[0m", accuracy)
print(classification_report(y_test, y_pred))