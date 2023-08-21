nums = [int(num) for num in input("Введите список: ").split()]
print(nums)
for i in range(len(nums) - 1, -1, -1):
    if nums[i] % 2 == 0:
        print(nums[i], end=' ')