# li = [ ["moahmmad" , "asif"], ["john",23] ]
# dict1 = dict(li)
# for keys in dict1.items():
#     print(keys)

li =[1,2,3,"mohamad","john",22,34,54,22]
for items in li:
    if str(items).isnumeric() and items >= 10:
        print(items)