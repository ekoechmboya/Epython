count = 0
while count <= 6:
    print(count)
    count +=1


start =0
while start <7:

    print(start)
    if start ==3:
        break
    start+=1



start=0
while start<6:
    start+=1
    if start ==3:
        continue
    print(start)


start = 1
while start < 7:
    print(start)
    start+=1
else:
    print("start is no longer less than 6")






#lFor looop
#popular for iterating loppping over sequences collections: lists, tuples, dictionaries, sets and strings
# allows excecution of a set of statements on each item in the collection or squence
# lists
fruits = [ "apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "apple":
        print("i have reached apple")
    else:
        print(x)





#range function
for x in range(6):
    print(x)
for x in range(3,9):
    print(x)


for x in range(2,10,3):
    print('last loop '+ str(x))
    print(x)


loopone = ['red', 'mango', 'joseph']
looptwo = []