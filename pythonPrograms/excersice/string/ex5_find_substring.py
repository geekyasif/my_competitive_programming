a = "shaasifbaj"
b = "asif"
count = 0

for i in range(0,len(a)):
    if a[i] == b[count]:
        count += 1
    else:
        count = 0

if count == len(b):
    print("Found")



