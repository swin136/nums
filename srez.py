# Пракитика срезов списка

nums = [5, 50, 1, 60, 25 , 3, 121, 34, 7, 8, 11]


print(f"Исходный список {list(nums)}")
# Длина списка
print(f"Длина списка: {len(nums)}")

# Первый элемент
print(f"Первый элемент списка >>> {nums[0]} <<<")
# Последний элемент
print(f"Последний элемент списка >>> {nums[-1]} <<<")
print(f"Последний элемент списка >>> {nums[len(nums) - 1]} <<<")

i = 2
j = len(nums) 
print(f"\nИсходный список {list(nums)}")
print(f"Срез {j} элементов списка списка >>> {nums[i:j]} <<<")
#print(f"Срез элементов списка списка >>> {nums[0:-1]} <<<")



symbs  = list("Python")

print(f"Новый список >>> {symbs}")

symbs[1:4] = ["1",  "1", "1" ]

print(f"Новый список >>> {symbs}")

