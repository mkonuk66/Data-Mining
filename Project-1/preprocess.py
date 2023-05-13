import string
import re
def preprocess_text(text):
    # Türkçe harfleri İngilizce karşılıklarına çevir
    turkish_chars = "çğıöşüÇĞİÖŞÜ"
    english_chars = "cgiosuCGIOSU"
    translator = str.maketrans(turkish_chars, english_chars)
    text = text.translate(translator)

    # Küçük harflere çevir
    text = text.lower()

    # Noktalama işaretlerini kaldır
    text = text.translate(str.maketrans("", "", string.punctuation))

    # Stopwords'leri çıkar
    stopwords = [ "a", "acaba", "altılı", "ama", "ancak", "artık", "aslında", "az", "açıkça", "açıkca", "aşağıdaki","ayrıca","adeta",
                "b", "bana", "bazı", "belki", "ben", "benden", "beni", "benim", "bile", "birçok", "biri","birkaç",
                     "birşey", "birşeyi", "biz", "bize", "bizden", "bizi", "bizim", "bu", "buna","bunda", "bundan", "bunu", "bunun", "burada", "böyle", "böylece", "bütün",
                "c", "ciddi",
                "ç", "çok", "çoğu", "çoktan",
                "d", "da", "daha", "dahi", "de", "defa", "diye", "dolayı",
                "e", "edecek", "eden", "ederek", "edilecek", "ediliyor", "edilmesi", "ediyor", "eğer", "elli", "en", "etmesi", "etti", "ettiği", "ettiğini",
                "f", "fakat", "falan", "filan",
                "g", "gibi", "göre", "gene", "gerçi", "gerek",
                "ğ",
                "h", "halen", "hangi", "hani", "hatta", "hem","henüz", "hep", "hepsi", "her", "herhangi", "herkesin", "hiç", "hiçbir",
                "ı",
                "i", "için", "ile", "ilgili", "ise", "işte", "itibaren","itibariyle",
                "j",
                "k", "kaç", "kadar", "kendi", "kendilerine", "kendini", "kendisi", "kendisine", "kendisini", "kez", "ki", "kim", "kimden", "kime", "kimi", "kimse",
                "l", "lakin", "lütfen",
                "m", "milyar", "milyon", "mu", "mü", "mı", "mi",
                "n", "nasıl", "ne", "neden", "nedenle", "nerde", "nerede", "nereye", "niye", "niçin",
                "o", "olan", "olarak", "oldu", "olduğu", "olduğunu", "olmadı", "olmadığı", "olmak", "olması", "olmayan", "olmaz", "olsa",
                     "olsun", "olup", "olur", "olursa", "oluyor", "ona", "ondan", "onlar", "onlardan", "onları", "onların", "onu", "onun", "oysa",
                "ö", "öyle", "öbür","önce","öncelikle","önceki","öylece","ötesinde",
                "p", "pek", "peki",
                "r", "rağmen",
                "s", "sadece", "sanki", "sen", "senden", "seni", "senin", "siz", "sizden", "sizi", "sizin",
                "ş", "şey", "şeyden", "şeyi", "şeyler", "şu", "şuna", "şunda", "şundan", "şunlar", "şunu",   "şimdi", "şöyle",
                "t", "tarafından", "trilyon", "tamam", "tamamen","tarafından", "trilyon", "tabi", "tüm", "tümü",
                "u",
                "ü", "üzere","üstelik",
                "v", "var", "vardı", "ve", "veya",
                "y", "ya", "ya da", "yani", "yapacak", "yapılan","yapılması", "yapıyor", "yapmak", "yaptı", "yaptığı", "yaptığını", "yaptıkları",
                     "yerine", "yine", "yirmi", "yoksa", "yüz",
                "z",  "zaten", "zira",
                "x",
                "q",]
    words = text.split()
    words = [word for word in words if word not in stopwords]

    # İşlenmiş metni döndür
    processed_text = " ".join(words)
    return processed_text