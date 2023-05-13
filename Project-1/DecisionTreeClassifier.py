import json
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report
import preprocess

# JSON dosyasından verileri okunuyor
with open('articles.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Verileri hazırlanıyor
X = []
y = []
for item in data:
    category = item['category']
    text = item['text']
    preprocessed_text = preprocess.preprocess_text(text)
    X.append(preprocessed_text)
    y.append(category)

# Veriler eğitim ve test verileri olarak ayırılıyor
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, random_state=42)

# Kelime dağarcığı oluşturuluyor
vectorizer = CountVectorizer()
X_train_vectorized = vectorizer.fit_transform(X_train)
X_test_vectorized = vectorizer.transform(X_test)

# Karar ağacı modeli oluşturuluyor
clf = DecisionTreeClassifier(criterion='gini')

# Karar ağacı modeli eğitiliyor
clf.fit(X_train_vectorized, y_train)

# Test verileri ile model değerlendiriliyor ve accuracy ile diğer başarı metrikleri ekrana yazdırılıyor
y_pred = clf.predict(X_test_vectorized)
print('\033[91mAccuracy:\033[0m', accuracy_score(y_test, y_pred))
print(classification_report(y_test, y_pred))