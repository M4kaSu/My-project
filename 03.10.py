# Завдання 1

nums = (1, 2, 3, 2, 4, 1, 5, 6, 3)
unique_nums = set(nums)

print("Кількість унікальних чисел:", len(unique_nums))

result = tuple(sorted(unique_nums))
print("Відсортований кортеж без дублікатів:", result)

# Завдання 2

A = {"Олег", "Марія", "Іван", "Софія"}
B = {"Іван", "Андрій", "Марія", "Катерина"}
C = {"Олег", "Катерина", "Петро"}

all_three = A & B & C

two_groups = (A & B) | (A & C) | (B & C)

one_group = (A | B | C) - two_groups

print("У всіх трьох групах:", all_three)
print("Хоча б у двох групах:", two_groups)
print("Тільки в одній групі:", one_group)

# Завдання 3

text = "Python is simple and powerful. Python is popular and simple."

words = text.replace(".", "").split()

unique_words = set(words)
print("Кількість унікальних слів:", len(unique_words))

one_time = [w for w in unique_words if words.count(w) == 1]
print("Слова, що зустрічаються один раз:", one_time)

# Завдання 4

products = [
    ("Молоко", 25),
    ("Хліб", 15),
    ("Масло", 60),
    ("Хліб", 15),
    ("Яблука", 40),
    ("Молоко", 25),
    ("Сир", 80)
]

unique_products = set(products)
names = {name for name, price in unique_products}
expensive = max(unique_products, key=lambda x: x[1])

print("Унікальні товари:", unique_products)
print("Унікальні назви:", names)
print("Найдорожчий товар:", expensive)

# Завдання 5

points = ((1, 2), (3, 4), (5, 6), (1, 2), (3, 4), (7, 8))
unique_points = set(points)

print("Кількість унікальних точок:", len(unique_points))
print("Унікальні точки:", sorted(unique_points))

# Завдання 6

word1 = "програмування"
word2 = "мова"

set1 = set(word1)
set2 = set(word2)

common = set1 & set2
unique = set1 ^ set2
all_letters = set1 | set2

print("Спільні літери:", common)
print("Тільки в одному слові:", unique)
print("Усі літери разом:", all_letters)
