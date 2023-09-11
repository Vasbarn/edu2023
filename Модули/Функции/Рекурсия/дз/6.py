import random


def Hoar(nums):
    if len(nums) <= 1:
        return nums
    else:
        q, a, b, c = nums[-1], [], [], []
        for n in nums:
            if n < q:
                a.append(n)
            elif n > q:
                b.append(n)
            else:
                c.append(n)
        return Hoar(a) + c + Hoar(b)


a, b, n = map(int, input('a b n: ').split())
A = [random.randint(a, b) for i in range(n)]
print('Исходный массив\n', *A)
print('Отсортированный массив\n', *Hoar(A))