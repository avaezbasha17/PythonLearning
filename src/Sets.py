mySets = {'apple','banana','orange','blueberry'}
print(mySets)

# The below coe is to loop the set
for i in mySets:
      print(i)
print('apple' in mySets)

# The below code is to add the element into a set
mySets = {'apple','banana','orange','blueberry'}
mySets.add('kiwi')
print(mySets)

# The below code is to concatenate the two sets
mySets = {'apple','banana','orange','blueberry'}
mySets1 = {1,2,3,4,5}
mySets.update(mySets1);  ''' It will accept the duplicate value if it is present in both sets'''
print(mySets)

# The below code is to remove the element in the set
mySets = {'apple','banana','orange','blueberry'}
mySets.remove('apple'); ''' It will remove the element'''
mySets.remove('abcds'); ''' It will through error'''
mySets.discard('abcds'); ''' It will not through an error it will search if the element is there it will remove, but if the element is not there then it execute without error '''
print(mySets)

# The below code is to delete the set
mySets = {'apple','banana','orange','blueberry'}
mySets.clear(); ''' It will remove all the elements in a sets'''
print(mySets)

del mySets; ''' another way to delete the all the elements in a sets '''