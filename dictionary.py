#definition of what a dictionary is
#iterable used to store items in key and value pairs
#features: ordered python3.7 and aboove
# changeable, allow duplicate
# dictionary values can be different data types
#syntax:

shoppingDictionary = {
    "item1": "bread",
    "item2": "milk",
    "item3": "flour"

}
print(len(shoppingDictionary))

#accessing items in dictionaries

#done by referencing the key name inside square brackets

x= shoppingDictionary.get("item3")
print(x)
print(shoppingDictionary["item1"])

y= shoppingDictionary.keys()
print(y)

print(shoppingDictionary.values())
print(shoppingDictionary.items())

check = "item2"
if check in shoppingDictionary:
    print("yes "+ x +" is in shoppingdictionay")
else:
    print("no, the item is not found")


#modification
shoppingDictionary["item1"]="salt"
print(shoppingDictionary["item1"])

#update method

shoppingDictionary.update({"item2": "unga"})
print(shoppingDictionary["item2"])

#adding items
#referencing
shoppingDictionary["item5"]="cheetah"
print(shoppingDictionary["item5"])

#update method

shoppingDictionary.update({"item4": "lions"})
print(shoppingDictionary["item4"])


#deleting
shoppingDictionary.pop("item4")
print(shoppingDictionary.values())


print(shoppingDictionary.values())

del shoppingDictionary["item1"]
print(shoppingDictionary.values())

#shoppingDictionary.clear()
#print(shoppingDictionary.values())


#copying
copyDictionary = shoppingDictionary.copy()
dictDictionary = dict(shoppingDictionary)
print(copyDictionary.values())
print(dictDictionary.values())

myFamily = {
    "child1":{
        "name": "joseph",
        "age": "26"
    },
    "child2": {
        "name": "Mary",
        "age": "26"
    },
    "child3": {
        "name": {
            "firstname": "joseph",
            "lastname": "mbugua"
        },
        "age": "26"
    },
}


# access to nested dictionaries
# say we wanted name info on child two
# reference child 2 using the key and then get the details you want using the key
print(myFamily["child2"]["name"])
print(myFamily["child3"]["name"]["firstname"])


#exerecise