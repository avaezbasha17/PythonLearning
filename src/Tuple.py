myTuple = ('apple',)
# the line code is consider as string because no comma is added at last
myList = ('apple')
print(type(myTuple))

# Tuple are unchangeable  value you can't change the value once's it is assigned
myTuple = ('apple','banana','orange')
myTuple[1] = 'strawberry'

# Accessing the Tuple
myTuple = ('apple','banana','orange','strawberry')
print(myTuple[-2])
print(myTuple[1:2])
print(myTuple[2:])
print(myTuple[:2])

# Update in Tuple
myTuple = ('apple','banana','orange','strawberry')
temp = list(myTuple)
temp[1] = 'blueberry'
myTuple = tuple(temp)
print(myTuple)

# Unpack in Tuple
myTuple = ('apple','banana','orange','strawberry')
(a,b,c,d) = myTuple
print(a)
print(b)
print(c)
print(d)

(a,*b,c) = myTuple
print(a)
print(b); ''' return in form of list '''
print(c)

# Looping through the Tuples
myTuple = ('apple','banana','orange','strawberry')
for i in myTuple:
    print(i)
print('----------------')
for i in range(len(myTuple)):
    print(myTuple[i])
print('----------------')
for i in range(0,2):
    print(myTuple[i])

# Concatenate the tuples
myTuples1 = (1,2,3,4)
myTuples2 = (5,6,7,8)
resultTuple = myTuples1 + myTuples2
print(resultTuple)

# Methods in Tuple
myTuple = (1,3,2,2,4,2,1,3,5)
countTuple = myTuple.count(2)
print(countTuple)

