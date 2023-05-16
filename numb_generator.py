"""
Пример работы с гнераторами чисел
А также с комментариями

"""

import random


def get_random_word(words):
    return str(random.choice(words)).lower()


MAX_NUM = 6

# Генерируем нечетные числа
nums = [2*k+1 for k in range (MAX_NUM)]

# Обычные числа
nums_annual = [k for k in range (MAX_NUM)]

# Генерируем четные числа
nums_2 = [2*k for k in range (1, MAX_NUM+1)]



#Обычные числа
#Нечетные числа
print(f"Выводим обычные числа  >>> {nums_annual}")

#Нечетные числа
print(f"Выводим нечетные  числа  >>> {nums}")
#Четные числа
print(f"Выводим нечетные числа  >>> {nums_2}")


i = random.randint(120, 200)

nums = [random.randint(1, 49), random.randint(50, 99), random.randint(100, 149), random.randint(150, 199),
            random.randint(200, 249), random.randint(250, 299)]


print(f"Случайное число {i}")

print(f"Список случайных чисел >>> {nums}")

nums = list(range(30, 41))
print(f"Ещё список чисел >>> {nums}")


# Список городов

city_list = ["New York", "Los Angeles", "Chicago", "Houston", "Philadelphia", "Los Swinus", "Baltimor", "Barad-Dur", "Minas Tirit", "Minas Morgul"]
print("Выбор случайного города из списка - ", random.choice(city_list))
print("Выбор случайного города из списка - ", random.choice(city_list))
print("Выбор случайного города из списка - ", random.choice(city_list))
print("Выбор случайного города из списка - ", random.choice(city_list))


word_list = ["bird", "tree", "freedom", "random", 
              "magic", "power", "glory", "seed", "beauty",
              "flower", "reeder", "writer", "save", "spirit",
              "heart", "friend", "queen", "innuendo", "rapsody",
              "trip", "type", "python", "pascal", "ruby", "Welcome",
              "morning", "day", "moon", "west", "north", "east", "south",
              "god", "kingthom", "swap", "linux", "pray", "Sault", "unix", 
              "FreeBSD", "OpenBSD", "FreeNas", "Debian", "pillow", "capital", "tower", "user"]



for number in range(8):
    print(f"Случайное слово № {number+1} из списка >>> {get_random_word(word_list)} <<<")
    

print(">>>>>>>>")
input("Нажми Enter для начала работы >>> ")
print(">>>>>>>>")



