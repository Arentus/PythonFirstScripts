def suma(a):
    return a + a
iterable = [2,3,4,5,6,7,8,9]

el_sumados = [suma(el) for el in iterable]

print(el_sumados)

words = "Porque aveces el guacamole es mejor que la guasacaca".split()

print(words)

print([len(word) for word in words])

from math import factorial

f = [len(str(factorial(x))) for x in range(20)]

print(f)
