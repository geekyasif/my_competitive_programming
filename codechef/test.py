def swap(obj):
    temp = obj['a']
    obj['a'] = obj['b']
    obj['b']  = temp

    print(f"Inside the fucntion {obj}")
    return obj



obj = {
    "a" : 5,
    "b" : 6
}

print(f"Before swap {obj}")
swap(obj)

# print(obj)
print(f"Outside the fucntion {obj}")