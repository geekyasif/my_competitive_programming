# list = []
# def identitymatrix(x):
#     for i in range(3):
#         for j in range(3):
#             k = i*j
#             list.append(k)
#
#
#
# identitymatrix(3)
# print(list)
# def subsetproduct(lst, k):
#     list2 = []
#     for i in lst:
#         for j in lst:
#             prod = i * j
#             if prod <= k:
#                 list2.append(prod)
#
#     return max(list2)
# print(subsetproduct([1,2,3,4,5,6],20))
# import string
#
# def count_unique(text):
#     str = ''
#     for i in text.lower():
#         if i not in string.punctuation:
#             str += i
#
#     list1 = [j for j in str.split(' ')]
#     list2 = []
#     for k in list1:
#         if k not in list2:
#             list2.append(k)
#     return len(list2)
#
# print(count_unique('ha ha ha'))
s = "the the the quick quick brown brown brown brown fox jumps jumps over"
dict = {}
for i in s.split(' '):
    p = s.count(i)
    dict[i] = p
    
print(dict.items(3))