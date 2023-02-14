#lists are ordered items, changeabel and allow duplicate values
# lists items are indexed: start counting from 0
# lists items can be accessed, added, removed and changed.


#accessing list items
#list items are accessed by referring to their indexed numbers
shoppingBasket = ["flour", "milk", "sugar", "kales", "kales"]
print(shoppingBasket[0])
print(shoppingBasket[-1])
print(shoppingBasket[2:5])
print(shoppingBasket[:4])
print(shoppingBasket[2:])
print(shoppingBasket[-4:-2])


x= input("check basket for this item")
if x in shoppingBasket:
    print("yes"+x+"in basket")
else:
    print("no" +x+" in basket")

print(shoppingBasket)
shoppingBasket[1:4] = ['apples', 'oranges', 'juice']
print(shoppingBasket)
shoppingBasket.insert(0, "Spinach")
print(shoppingBasket)
shoppingBasket.append("cereals")
print(shoppingBasket)

juiceFlavours= ['strawberry', 'mango', 'passion']
toolShopping= ['hammers', 'screws', 'screw drivers']
shoppingBasket.extend(toolShopping)
print(shoppingBasket)


#you can also add other iterables : lists sets tuples and dictionaries

tupleExample= ('kiwi','gel')
shoppingBasket.extend(tupleExample)
print(shoppingBasket)
shoppingBasket.remove("Bread")
print(shoppingBasket)
shoppingBasket.pop(1)
shoppingBasket.pop()
print(shoppingBasket)
del shoppingBasket[2]
print(shoppingBasket)
shoppingBasket.clear()
print(shoppingBasket)