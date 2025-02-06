a = {'a', 'b', 'c'}
b = {1, 2, 3}
c = a.union(b)
print(c)

# The below no duplicate value will take in sets
q = {'a', 'b', 'c'}
w = {'a', 'w', 'l'}
e = q.union(w)
print(e)

# Intersection Update
# x = {"apple", "banana", "cherry"}
# y = {"cherry", "apple", "microsoft"}
# x.intersection_update(y); ''' It will give the output for duplicate matched elements'''
# z = x.intersection(y); ''' It return and store in a variable the duplicate elements'''
# print('X: ',x)
# print('Z', z)


# Symmetric Difference
x = {"apple", "banana", "cherry"}
y = {"cherry", "apple", "microsoft"}
x.symmetric_difference_update(y); ''' It will give the non duplicate elements'''
z = x.symmetric_difference(y); ''' It will give the non duplicate elements, but it will store in to variable'''
print("X: ",x)
print("Z: ",z)