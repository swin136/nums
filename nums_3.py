"""
Пример работы со списками из книги 
"Программирование на Python в примерах и задачах"
"""

nums = [5, 10, 1, 60, 25 , 3]

# Отображение содержимого списка
print(f"Список из чисел: {nums}")
print(f"Срез списка >>> {nums[2:6]} <<<")
print(f"Список из чисел (2-й варинат): {list(nums)}")

# Длина списка
print(f"Длина списка: {len(nums)}")

# Первый элемент
print(f"Первый элемент списка: {nums[0]}")
# Последний элемент
print(f"Последний элемент списка: {nums[-1]}")
print(f"Последний элемент списка (2-й вариант) >>> {nums[len(nums) -1]}")
# Наибольшее значение
print(f"наибольшее значение списка: {max(nums)}")
# Наименьшее значение
print(f"наибольшее значение списка: {min(nums)}")
# Сумма элементов списка
print(f"наибольшее значение списка: {sum(nums)}")

# Работаем с сортировкой списка
print("\nСортировка списка")
# Список в обратном порядке
print(f"Список в обратном порядке >>> {list(reversed(nums))}")

#Сотрировка списка по  возрастанию значений
print(f"По возрастанию значений >>> {sorted(nums)}")
#Сотрировка списка по убыванию значений
print(f"По возрастанию значений >>> {sorted(nums, reverse = True)}")

print(f"Исходный список {list(nums)}")
print("\n")


# Изменение элемента списка
nums[1] = "Текст"
# Отбражение содержимого списка
print(f"Список после внесения изменений >>> {nums}")
# Получение среза
print(f"Получение среза списка >>> {nums[1: len(nums) - 1]}")
#Замена части элементов списка
nums[1:-1] = ["A", "B"]
print(f"После замены элементов >>> {nums}")


# Список чисел от 5 до 10
print("\nНовый список")
nums = list(range(5,12))
print(f"Список чисел от 5 до 10 >>> {nums}")






