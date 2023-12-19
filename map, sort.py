x = [1, 2, 3, 4, 5, 0]
y = {"B": 3,
     "A" : 1,
     "C": 2}
print(y.items())
print(sorted(y.items(), reverse= True, key= lambda z: z[0]))

def stepen(x: int)-> int:
     return x**3

def chetnost(x: int)-> bool:
     if x%2 == 0:
          return True


new_x = list(map(stepen, x))
print(new_x)

new_new_x = list(filter(chetnost, new_x))
print(new_new_x)

