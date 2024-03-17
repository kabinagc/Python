a =[]
# b = list()
# print(type(a))
# print(type(b))             a.extend(b)

for i in range(1, 21):
    if i % 2 == 0:
        a.append(i)
b = [1,2,3]
a = a +b
print(a)

# print(a[1])
# print(a[-1])
# print(a[::-1])
# print(a[2:4])
a.remove(10)
print(a)

a = [1, True,"hello",(1,2,3)]
b = {1,2, "apple", True}
print(b)

