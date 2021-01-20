lista1 = [1,4,7,23,50,-100,-2,0,-30]
print(lista1)
lista2 = sorted(lista1)
print(lista2)
lista3=lista1
lista3.sort(reverse=True)
lista1 = [1,4,7,23,50,-100,-2,0,-30]
print(lista3)
print(len(lista1))
print(max(lista1))
print(min(lista1))
print(lista1 + [-111])
lista1.insert(2, -222)
print(lista1)