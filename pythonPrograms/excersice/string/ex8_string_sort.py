a = ['a','d','c','b']
print(len(a))
for i in range(1, len(a)):
    for j in range(1, len(a)):
        if a[i] > a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp

print(a)
