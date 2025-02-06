myList = ["apple","ball","cat"]
print(myList)
print(myList[1])
print(myList.index('apple'))
print(myList[0:2])
print(myList.pop(0))

myList.append("apple")
print(myList)
myList.sort()
print(myList)

myList[0:1] = ['aws','databricks']
# myList[0:1] = [] //it will remove the apple
print(myList)

myList.insert(0,"apple")
print(myList)


x= [1,2,3,4]
y= [5,6,7,8]
x.extend(y)
print(x)

x.remove(1)
print(x)