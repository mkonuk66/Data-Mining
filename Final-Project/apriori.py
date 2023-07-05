########################################################################################################################
#                                        Veri Madenciliği Dönem Sonu Projesi                                           #
#                                              Mehmet Emin KONUK                                                       #
########################################################################################################################
import pandas as pd
from itertools import combinations


def generate_candidates(itemset, k):
    # Aday öğe kümelerini oluşturma
    candidates = []
    for i in range(len(itemset)):
        for j in range(i + 1, len(itemset)):
            # Birleştirme adımı
            candidate = sorted(list(set(itemset[i]) | set(itemset[j])))
            if len(candidate) == k:
                candidates.append(candidate)
    return candidates


def prune(itemset, candidates):
    # Aday öğe kümelerini, alt kümeleri kontrol ederek temizleme
    pruned_set = []
    for candidate in candidates:
        # Alt kümelerini kontrol etme adımı
        is_valid = True
        for subset in combinations(candidate, len(candidate) - 1):
            if list(subset) not in itemset:
                is_valid = False
                break
        if is_valid:
            pruned_set.append(candidate)
    return pruned_set


def calculate_support(transaction, itemset):
    # Bir öğe kümesinin veri setindeki destek sayısını hesaplama
    count = 0
    for t in transaction:
        if set(itemset).issubset(t):
            count += 1
    return count


def apriori(transactions, min_support):
    # Apriori algoritması kullanarak sık öğe kümelerini hesaplama
    min_support = min_support * len(transactions)
    itemset = [[item] for sublist in transactions for item in sublist]
    itemset = list(set(map(tuple, itemset)))
    itemset = [list(item) for item in itemset]

    k = 2
    frequent_itemsets = []
    while itemset:
        candidates = generate_candidates(itemset, k)
        pruned_candidates = prune(itemset, candidates)

        frequent_itemsets_k = []
        for candidate in pruned_candidates:
            support = calculate_support(transactions, candidate)
            if support >= min_support:
                frequent_itemsets_k.append((candidate, support))

        frequent_itemsets.extend(frequent_itemsets_k)
        itemset = [item for item, _ in frequent_itemsets_k]
        k += 1

    return frequent_itemsets


def calculate_association_rules(frequent_itemsets, transactions, min_confidence):
    # Birliktelik kurallarını ortaya çıkarma
    association_rules = []
    for itemset, support in frequent_itemsets:
        if len(itemset) > 1:
            subsets = powerset(itemset)
            for subset in subsets:
                antecedent = list(subset)
                consequent = list(set(itemset) - set(subset))
                antecedent_support = calculate_support(
                    transactions, antecedent)
                confidence = support / antecedent_support
                if confidence >= min_confidence:
                    association_rules.append(
                        (antecedent, consequent, confidence))
    return association_rules


def powerset(s):
    # Alt Küme oluşturma
    power_set = []
    for i in range(1, len(s)):
        subsets = combinations(s, i)
        power_set.extend(subsets)
    return power_set


print("\033[91m############################################################################\033[0m")
print("Veriler okunuyor...")
print("\033[90m----------------------------------------------------------------------------\033[0m")
df = pd.read_excel("fişler.xlsx")
print("Veriler okundu. Toplam veri sayısı:\033[96m", len(df), "\033[0m")
print("\033[90m----------------------------------------------------------------------------\033[0m")
print("Veriler birleştiriliyor...")
print("\033[90m----------------------------------------------------------------------------\033[0m")
transactions = df.groupby("FISNO")["URUN"].apply(list).tolist()
print("Veriler birleştirildi. Toplam fiş sayısı:\033[96m", len(
    transactions), "\033[0m")
min_support = 0.5
min_confidence = 0.75
print("\033[90m----------------------------------------------------------------------------\033[0m")
frequent_itemsets = apriori(transactions, min_support)
association_rules = calculate_association_rules(
    frequent_itemsets, transactions, min_confidence)
count = 0
for antecedent, consequent, confidence in association_rules:
    count += 1
    print(f"Kural {count} : \033[91m{antecedent}\033[0m ürünü alındıysa \033[91m{consequent[0]}\033[0m ürününün alınma ihtimali \033[92m %{confidence*100:.2f} \033[0m")
print("\033[91m############################################################################\033[0m")
