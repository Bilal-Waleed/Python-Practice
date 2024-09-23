# topic dictionary 
marks = {
    "bilal" : 100, 
    "ahmad" : 40, 
    "zeenat" : 98,
    0 : "bilal" 
}

print(len(marks)) # for finding the length of dic
# print(marks.clear()) # clear use to clean th dictionary 

# print(marks , type(marks))

print(marks.items())  #([('bilal', 100), ('ahmad', 40), ('zeenat', 98), (0, 'bilal')])
print(marks.keys())  # dict_keys(['bilal', 'ahmad', 'zeenat', 0])
print(marks.values()) # dict_values([100, 40, 98, 'bilal'])

marks.update({"bilal" : 98 , "ali": 65 }) # update use for change value in dictionary or add new value in it
print(marks)
print(marks["zeenat"])

pop = marks.pop("ahmad") # this use to delete item from dic
print(pop)


pop_item = marks.popitem() # popitem use to delete the last key value pair of dic
print(pop_item)

print(marks)

# Topic set
e = set() # for make a empty set 
print(type(e))

s = {1 , 2 ,3 ,4 ,5 ,"bilal"}
s.remove(1)           # this method use for removng any value in set
print(s , type(s))

s.discard(4) # this use for discard a value if value is not in the set they don't return error
print(s)

s.add(7) #this use for add some value in set 
print(s)

s.pop() # this method remove the random value from the set 

s.clear() # this method use to clear the set 
print(s)

s1 = { 1, 33 ,4 ,5 ,7}
s2 = { 5 ,7  ,33}
print(s1.union(s2))
print(s1.intersection(s2))
print(s1.difference(s2))
print(s1.issubset(s2)) # false because s2 don't carry all s1 element
print(s1.issuperset(s2)) # true becaause s1 contain all s2 element
print(s1.isdisjoint(s2)) # false because s2 contain same element in s1 
