# an iterator is any object that contains a countable number of values
#iterator any object that can be traversed: looped
#any object that implements the iterator protocol, iter__() and
#iterables: lists strings tuples sets dictionaries are built from iterators
#iter() method enables objects to be traversed
mytuple=("1", "2", 3)
myIterable= iter(mytuple)
print(next(myIterable))
print(next(myIterable))
print(next(myIterable))
x= "joseph"
myIterable =iter(x)
print(next(myIterable))


#create an iterator that returns numbers, starting with 1 and adding one
#classes and objects

