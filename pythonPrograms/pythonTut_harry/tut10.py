# if else condition
# a = 4
# b =2
# if a > b:
#     print("a is greater")
# else:
#     print("B is greater")
#
# if a == 4:
#     print(a)
# elif b == 2:
#     print(b)
# else:
#     print("nothing")

# ************************ not in *********************
li = [1,2,3,4,5]
if 6 not in li:
    print("correct")
else:
    print("flASE")



dict = {
    "success" : "kameyabi",
    "good": "acha",
    "bad": "ganda",
}

# ***************************** not **************
print("Enter a word to find the meaning")
n = input()
# m =dict.get(n)
# print(m)
if not dict.get(n):
    print("No word " + n + " is found")
else:
    print("Meaning of " + n + " is - ", dict.get(n))

