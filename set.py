# sets are defined using curly braces
#sets are unordered, unchangeable, unindexed
#sets do not have duplicates
#true and 1 are also considered the same
#sets will allow different data types

shoppingSet = {"bread", "sugar", "salt"}
print(shoppingSet)

#getting length of set
#len()
print(len(shoppingSet))


#accessing items in a loop
#use a loop
#for loop:
for x in shoppingSet:
    print(x)
#checking
check="bread"
print(check in shoppingSet)

#updating a set adding, removing
shoppingSet.add("Flour")
print(shoppingSet)
juiceFlavours= {"Mango", "passion","Apple"}
shoppingSet.update(juiceFlavours)
print(shoppingSet)
simpleList = ['oranges', 'soap', 'spoons']
simpleTuple = ("forks", "spades")
shoppingSet.update(simpleList)
shoppingSet.update(simpleTuple)
print(shoppingSet)


#remove
shoppingSet.remove("spades")
shoppingSet.discard("forks")
print(shoppingSet)
x= shoppingSet.pop()
print(x)

# joining tuples
set3 = {1, 3, 4 ,5 ,5}
set4= shoppingSet.union(set3)
# union creates a new set

# intersection_update
x= {"apple", "microsoft"}
y={"java", "kotlin", 'apple'}
x.intersection_update(y)
print(x)
z= x.intersection(y)
print(z)

x= {"apple", "microsoft","java", True, False}
y={"java", "kotlin", 'apple', 1,2,3,0,4,5}
k= x.symmetric_difference(y)
print(k)
