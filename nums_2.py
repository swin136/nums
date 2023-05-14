nums = [12, 1, 5, 6, 7, 15]


print(f"Исходный масссив {list(nums)}")

print(f"Часть массива {nums[2:]}")
print(f"Последний элемент {nums[-1]}")


nums2 = sorted(nums, reverse = True)
print(f"Отсортированный массив {list(nums2)}")
print(f"Часть массива {list(nums2[2:5])}")



nums[0] = "Пример текста"
print(f"Измененный масссив {list(nums)}")
