import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import sklearn.metrics as metrics

class NeuralNetwork:
    # Constructor fonksiyon, nesne oluşturulduğunda çalışır.
    def __init__(self, input_size, hidden_size, output_size):
        # Giriş boyutu (input_size), gizli katman boyutu (hidden_size) ve çıkış boyutu (output_size) gibi özellikleri tanımlar.
        self.input_size = input_size
        self.hidden_size = hidden_size
        self.output_size = output_size

        # Ağırlıkları ve biasları rastgele değerlerle başlatır.
        self.weights1 = np.random.randn(self.input_size, self.hidden_size)
        self.bias1 = np.zeros((1, self.hidden_size))
        self.weights2 = np.random.randn(self.hidden_size, self.output_size)
        self.bias2 = np.zeros((1, self.output_size))

    # İleri yayılım işlemi. Ağın giriş verisini alır ve çıkışı hesaplar.
    def forward(self, X):
        # İlk katman (giriş -> gizli) hesaplanır.
        self.z1 = np.dot(X, self.weights1) + self.bias1
        self.a1 = self.sigmoid(self.z1)
        # İkinci katman (gizli -> çıkış) hesaplanır.
        self.z2 = np.dot(self.a1, self.weights2) + self.bias2
        self.a2 = self.sigmoid(self.z2)
        # Son çıkışı döndürür.
        return self.a2

    # Sigmoid aktivasyon fonksiyonu. Verilen değerin sigmoid fonksiyonunu uygular.
    def sigmoid(self, x):
        return 1 / (1 + np.exp(-x))

    # Sigmoid aktivasyon fonksiyonunun türevidir.
    def sigmoid_derivative(self, x):
        return x * (1 - x)

    # Geri yayılım işlemi. Ağırlıkları günceller.
    def backward(self, X, y, learning_rate):
        m = X.shape[0]  # Eğitim örneklerinin sayısı

        # Çıkış katmanındaki hata hesaplanır.
        delta2 = (self.a2 - y) * self.sigmoid_derivative(self.a2)
        dweights2 = np.dot(self.a1.T, delta2)  # Ağırlıklar güncellenir.
        dbias2 = np.sum(delta2, axis=0, keepdims=True)  # Bias güncellenir.

        # Gizli katmandaki hata hesaplanır.
        delta1 = np.dot(delta2, self.weights2.T) * \
            self.sigmoid_derivative(self.a1)
        dweights1 = np.dot(X.T, delta1)  # Ağırlıklar güncellenir.
        dbias1 = np.sum(delta1, axis=0, keepdims=True)  # Bias güncellenir.

        # Ağırlıkları günceller.
        self.weights2 -= learning_rate * (dweights2 / m)
        self.bias2 -= learning_rate * (dbias2 / m)
        self.weights1 -= learning_rate * (dweights1 / m)
        self.bias1 -= learning_rate * (dbias1 / m)

    # Ağı eğitmek için geri yayılım algoritmasını kullanır.
    def train(self, X, y, epochs, learning_rate):
        # Belirtilen sayıda epoch boyunca eğitim yapılır.
        for epoch in range(epochs):
            output = self.forward(X)  # İleri yayılım işlemi yapılır.
            # Geri yayılım işlemi yapılır.
            self.backward(X, y, learning_rate)

            if epoch % 1000 == 0:  # Her 1000 epoch'ta bir ekrana loss değeri yazdırılır.
                loss = np.mean(np.square(output - y))  # Hata hesaplanır.
                # Hata ekrana yazdırılır.
                print(f"Epoch: {epoch}, Loss: {loss}")

    # Verilen giriş verisi için tahmin yapar.
    def predict(self, X):
        return self.forward(X)  # İleri yayılım işlemi yapılır.

# Verileri okur.
def read_data(filename):
    data = pd.read_csv(filename)
    data = data.dropna()
    return data['Close'].values

# Verileri oluşturur.
def create_dataset(data, window_size):
    # Verileri normalize eder.
    data_normalized = (data - np.min(data)) / (np.max(data) - np.min(data))
    X, y = [], []
    # Verileri pencere boyutuna göre ayırır.
    for i in range(len(data_normalized) - window_size):
        X.append(data_normalized[i:i+window_size])
        y.append([data_normalized[i+window_size]])
    return np.array(X), np.array(y)


# Verileri oku
filename = 'thy.csv'
data = read_data(filename)

# Verileri normalize et
normalized_data = (data - np.min(data)) / (np.max(data) - np.min(data))

# Eğitim ve test verilerini ayır
train_size = int(len(normalized_data) * 0.66)
train_data = normalized_data[:train_size]
test_data = normalized_data[train_size:]

# Girdi ve çıktı verilerini oluştur
window_size = 50
X_train, y_train = create_dataset(train_data, window_size)
X_test, y_test = create_dataset(test_data, window_size)

# Yapay sinir ağı modelini oluştur
input_size = window_size
hidden_size = 8
output_size = 1
model = NeuralNetwork(input_size, hidden_size, output_size)

# Modeli eğit
epochs = 10000
learning_rate = 0.1
model.train(X_train, y_train, epochs, learning_rate)

# Eğitim ve test tahminlerini yap
train_predictions = model.predict(X_train)
test_predictions = model.predict(X_test)

# Eğitim ve test verilerini gerçek ölçeğe dönüştür
train_data_denormalized = (
    train_predictions * (np.max(data) - np.min(data))) + np.min(data)
test_data_denormalized = (
    test_predictions * (np.max(data) - np.min(data))) + np.min(data)

# Grafikleri çiz
plt.figure(figsize=(12, 6))
plt.title("Eğitim ve Tahminler - Hisse Fiyatı")
plt.plot(data, label='Gerçek Veri')
plt.plot(range(window_size, window_size + len(train_predictions)),
         train_data_denormalized, label='Eğitim Verileri')
plt.plot(range(train_size + window_size, train_size + window_size +
          len(test_predictions)), test_data_denormalized, label='Test Verileri')
plt.legend()
plt.show()

# Bir sonraki gün için tahmin yap
last_window = np.array([data[-window_size:]])
next_day_input = (last_window - np.min(data)) / (np.max(data) - np.min(data))
next_day_prediction = model.predict(next_day_input)
next_day_price = next_day_prediction * \
    (np.max(data) - np.min(data)) + np.min(data)

# Eğitim ve test verileri için hata ve r2 skorlarını hesapla
train_loss = metrics.mean_squared_error(y_train, train_predictions)
train_f1_score = metrics.r2_score(y_train, np.round(train_predictions))
test_loss = metrics.mean_squared_error(y_test, test_predictions)
test_f1_score = metrics.r2_score(
    y_test, np.round(test_predictions))

# Tahmin edilen fiyatı ekrana yazdır
print("Bir sonraki gün için tahmin edilen hisse fiyatı:",
      np.round(next_day_price[0][0], decimals=2))
# Test verileri için hata ve r2 skorlarını ekrana yazdır
print("Test Verileri - Validasyon Hatası:", np.round(test_loss, decimals=5))
print("Test Verileri - R2 Skoru:", np.round(test_f1_score, decimals=2))
