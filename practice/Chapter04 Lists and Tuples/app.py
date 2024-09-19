friends = ["Apple", "Orange", 5, 345.06, False, "alvi", "Rohan"]

print(friends[0])
friends[0] = "Grapes" # Unlike Strings lists are mutable

print(friends[0])
print(friends[1:4])

friends = ["Apple", "Orange", 5, 345.06, False, "alvi", "Rohan"]
print(friends)
friends.append("bilal")
print(friends)

l1 = [1, 34,62, 8, 6, 11]
# l1.sort()
# l1.reverse()
# l1.insert(2, 333333) # Insert 333333 such that its index in the list is 2
value = l1.pop(2)
print(value)
print(l1)

l1.remove(11) 
print(l1)


a = () # this show a empty tuple
b = (1,) # this show a tuple carry 1 value
c = (1,45,342,3424,False, "bilal", "ali")
print(c)
print(type(b))

no = c.count(45)
print(no)

i = c.index(3424)
print(i)

print(len(c))

tup = (1 , 2 , 4 ,6 )
max = max(tup) # find the grater value in tuple
print(max)

min = min(tup) # find the lowest value in tuple
print(min)

sum = sum(tup) # to sum all the value in tuple 
print(sum)

find = 4 in tup # check the value in tuple or not 
print(find)