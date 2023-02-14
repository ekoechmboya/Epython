
shoppingTuple = ("flour", "milk", "sugar", "kales", "kales")
tuple1 = (1,2,3,45,5)
tuple2 = ("string", 1, True, False,"another string")
type(tuple1)
print(shoppingTuple)
print(shoppingTuple[0])
print(shoppingTuple[-1])
print(shoppingTuple[2:5])
print(shoppingTuple[2:])
print(shoppingTuple[:3])
print(shoppingTuple[-4:-1])

search = "milk"
if search in shoppingTuple:
    print("yes"+search+"is in tuple")
else:
    print("no"+search+"is not in tuple")








tempList= list(shoppingTuple)
tempList[0]= "maziwa"
shoppingTuple=tuple(tempList)
print(shoppingTuple)


tempList.append("wheat")
shoppingTuple=tuple(tempList)
print(shoppingTuple)

tuple3=("oranges",)
shoppingTuple+=tuple3
print(shoppingTuple)
tempList=list(shoppingTuple)
tempList.remove("oranges")
del tempList[0]
shoppingTuple=tuple(tempList)
print(shoppingTuple)

# a whole tuple can be deleted


# unpacking a tuple

(sugar, salt, bread, sugar, flour)= shoppingTuple
print(sugar)
print(salt)
print(bread)
print(sugar)
print(flour)
(sugar, salt, *bread)= shoppingTuple
print(bread)
(*sugar, salt, flour)


duplicateTuple = shoppingTuple*2
print(duplicateTuple)


# 1. Print the first item in the fruits tuple
fruits=("apple", "banana", "oranges")
print(fruits[0])
# 2. print number of items in the fruits tuple
print(len(fruits))
# 3. I want to access oranges without referencing its index position
print(fruits[-1])
fruits = ("apple", "banana", "oranges" )
x= fruits.count("apple")
# shows number of times