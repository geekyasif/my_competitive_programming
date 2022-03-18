

dict = {
    "success" : "kameyabi",
    "good": "acha",
    "bad": "ganda",
}

print("Enter a word to find the meaning")
n = input()
# m =dict.get(n)
# print(m)
if not dict.get(n):
    print("No word " + n + " is found")
else:
    print("Meaning of " + n + " is - ", dict.get(n))