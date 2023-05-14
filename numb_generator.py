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
print(f"Выводим нечетные числа  >>> {nums}")
#Четные числа
print(f"Выводим нечетные числа  >>> {nums_2}")
