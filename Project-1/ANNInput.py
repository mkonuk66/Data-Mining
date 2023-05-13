from sklearn.feature_extraction.text import CountVectorizer
from sklearn.neural_network import MLPClassifier
import json
import preprocess

# JSON dosyasından veriler okunuyor
with open('articles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Veriler hazırlanıyor
    X = []
    y = []
    for item in data:
        X.append(item["text"])
        y.append(item["category"])

# Veriler vektörize ediliyor
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Features
feature_names = vectorizer.get_feature_names_out()

# Yapay sinir ağı modeli oluşturuluyor
clf = MLPClassifier(hidden_layer_sizes=(100,), max_iter=500)

# Yapay sinir ağı modeli eğitiliyor
clf.fit(X, y)

# Kullanıcıdan bir metin isteniyor
text = input("\033[91mMetin girin: \033[0m")

# Kullanıcı metni ön işlemden geçiriliyor
text = preprocess.preprocess_text(text)

# Girilen metnin vektörize edilerek kategorisi tahmin ediliyor
X_test = vectorizer.transform([text])
category = clf.predict(X_test)[0]

# Modelin Feature'lar yazdırılıyor
print("\033[91mÖzellikler:\033[0m", feature_names)

# Tahmin edilen kategori yazdırılıyor
print("\033[91mMetnin kategorisi:\033[0m\033[92m", category, "\033[0m")
