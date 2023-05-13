import json
import numpy as np
import preprocess
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

# JSON verileri okunuyor
with open("articles.json", encoding="utf-8") as f:
    data = json.load(f)

# Veriler DataFrame'e yükleniyor
df = pd.DataFrame(data)

# Veriler ön işlemden geçiriliyor
df["text"] = df["text"].apply(preprocess.preprocess_text)

# Veriler vektörize ediliyor
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(df["text"])

# Features
feature_names = vectorizer.get_feature_names_out()

# Karar ağacı modeli eğitiliyor
clf = DecisionTreeClassifier()
clf.fit(X, df["category"])

# Kullanıcıdan metin girdisi alınıyor
text = input("\033[91mMetin girin: \033[0m")

# Metin ön işlemden geçiriliyor
preprocessed_text = preprocess.preprocess_text(text)

# Karar Ağacı modeli kullanarak kullanıcıdan alınan veri vektörize ediliyor
X_test = vectorizer.transform([preprocessed_text])

# Alınan girdinin kategorisi karar ağacı ile tahmin ediliyor
predicted_category = clf.predict(X_test)[0]

# Modelin feature'ları ekrana yazdırılıyor
print("\033[91mÖzellikler : \033[0m",feature_names)

# Tahmin edilen kategori ekrana yazdırılıyor
print("\033[91mTahmin edilen kategori: \033[0m\033[92m", predicted_category,"\033[0m")