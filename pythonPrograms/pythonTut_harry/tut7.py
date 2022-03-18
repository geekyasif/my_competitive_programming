# String and its functions

# string slicing
# name = "Mohammad12Asif"
name = 'helloasif'
print(name[5:10])
print(name[5:10:2])
print(name[-5:-10])

# find the length of a string
print(len(name))

# isalnum() function is use to check only number in string  without spaces( true if all characters in the string are alphanumeric)
print(name.isalnum())

# isalphanum functiin checks only alphacharacters in a string without spaces
print(name.isalpha())

# to count certain charcter in a string
print(name.count('l'))

# to convert first charcters in capital letter
print(name.capitalize())
print(name.lower())
print(name.upper())
print(name.find("as"))
print(name.replace("asif","haris"))
