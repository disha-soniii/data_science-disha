# print("hello world")
# print("hello world")

# a=10
# print(a)

# _a=4
# __a=5
# a7v=6

# name="disha"
# print(name)
# print("type of sring",type(name)) #checking data type
# print("length of string",len(name)) #checking length of string

# # indexing
# print(name[0])
# print(name[4])

# #slicing
# print(name[0:3])
# print(name[-5:-2])
# print(name[-3:-1])

# operation
# name="disha"
# upper_case= name.upper()
# print(upper_case)

# last="SONI"
# lower_case= last.lower()
# print(lower_case)

# name="disha"
# title_name= name.title() #It will capitalize every word's first letter in a sentence
# print(title_name)
# cap_name= name.capitalize() #It will capitalixe only first word's first letter in sentence
# print(cap_name)
# print(name.count("s"))

# name="disha"
# last="soni"
# print(name+" "+last)

#reverse of string-> 
# name="disha"
# print(name[::-1])

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> list >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# mutable
# allow duplicates
# hetergeneous elements (diff datatypes can be stored in single list)
# indexing 
# slicing

# diff b/w array and list
# array is homogeneous and list is heterogeneous

# my_list= [1,2,3,4,5,6,6,"disha","soni"]
# print("my first list:", my_list)
# print("type of my list",type(my_list))
# print("lenght of my list",len(my_list))
# print((my_list.count(6)))
# print("indexing",my_list[3])
# print("slicing",my_list[3:7])
# print(my_list[::-1])

# my_list= [1,2,3,4,5,6,6,"disha","soni"]
# reverse_list= my_list.reverse()
# print(reverse_list)
# The code gives `None` as output because the `reverse()` function modifies 
# the original list in place and does not return a new list. Instead of producing 
# a reversed version as a separate value, it simply updates the existing list and
# returns `None` by default. When the result of `my_list.reverse()` is assigned to
# `reverse_list`, the value stored is actually `None`, not the reversed list. Therefore,
# printing `reverse_list` displays `None` instead of the expected list.

#So, we use this code
# my_list= [1,2,3,4,5,6,6,"disha","soni"]
# my_list.reverse()
# print(my_list)

# my_list= [1,2,3,4,5,6,6,"disha","soni"]
# my_list.append(100)
# print(my_list)

# my_list.clear()
# print(my_list)

# my_list= [1,2,3,4,5,6,6,"disha","soni"]  sort operation can't be applied on this
# my_list= [1,9,6,4,5,22,3,6,10,7,2.4]
# my_list.sort()
# print(my_list)

# my_list= [1,9,6,4,5,22,3,6,10,7,2.4]
# my_list.pop()
# print(my_list)
# my_list.remove(4)
# print(my_list)
# my_list= [1,9,6,4,5,22,3,6,10,7,2.4]
# my_list[1]=1001
# print(my_list)
# my_list= [1,9,6,4,5,22,3,6,10,7,2.4]
# my_list.insert(3,555)
# print(my_list)
# my_list= [1,9,6,4,5,22,3,6,10,7,2.4]
# copy_of_list=my_list.copy()
# print(copy_of_list)



# can we add, subtract, multiply or divide list?
# we can add, multiply list but can subtract and divide

# add
# a = [1, 2]
# b = [3, 4]
# print(a + b)  # Output: [1, 2, 3, 4]

# multiply
# a = [1, 2]
# print(a * 2)  # Output: [1, 2, 1, 2]

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> tuple >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# ordered
# immutable
# heterogeneous elements
# contains duplicate

# tpl=(1,2,3,4,5,5)
# print("my first tuple",tpl)
# print("type of tuple",type(tpl))
# print("length of tuple",len(tpl))
# print(tpl.count(5))
# print("indexing",tpl.index(2))   #It will show index of element 2
# print(tpl[3])
# print(tpl[::-1])
# print(tpl[1:4])
# print(tpl[0:4:2])
# tpl[3]=9 #we can't change the items in the tuple i.e. tuple is immutable
# tpl.append(100) #this operation can't be performed
# print(tpl)

# name= 1,2,3,4,5,6,7 #It will by default stored in tuple
# print(name)
# print(type(name))

# name=("disha","soni","sangam")
# print(name)
# print(type(name))

# tuple unpacking      no. of elements must be exactly same as no. of variables
# num=(1,2,3,4)
# a,b,c,d=num
# print(a)
# print(b)
# print(c)
# print(d)

# tpl1=(1,2,3,4,5,6,7,8,9)
# tpl2=(1,2,3,4,5,6,7,8,9)
# print(tpl1+tpl2)
# print(tpl1*2)
# print(tpl1*tpl2)
# print(tpl1/tpl2)

# tpl1=(1,2,3,4,5,6,7,8,9)
# tpl1=list(tpl1)
# tpl1.append(100)
# print(tuple(tpl1))

# task=["ritik","diya","rohit",[1,2,[3,6],4]] #access 6
# print(task[3][2][1])


#<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<< dict <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# mutable
# key value pair
# key must be unique
# key must be immutable
# can't do indexing and slicing of a dictionary i.e. it is not possible to access index in dictionary
# my_dict={"name":"disha","age":20,"address":"ajmer"}
# print("my first dict",my_dict)
# print("type of my dict",type(my_dict))
# print("length of my dict",len(my_dict))
# print(my_dict["name"])
# print(my_dict["age"])
# print(my_dict["address"])

# my_dict={"name":"disha","age":20,"address":"ajmer"}
# print(my_dict.keys())
# print(my_dict.values())
# print(my_dict.items())
# my_dict["mobile no."]= 1234567890

# update function
# my_dict.update({"address":"nagaur"})
# print(my_dict)
# copy
# deep copy
# copy_dict=my_dict.copy()
# print(copy_dict)
# my_dict.clear()

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> set >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
# mutable
# inordered
# no duplicate values
# no indexing
# no slicing

# set1={11,2,3,4,2,5,6,7,5,7}
# # print("my first set",set1)
# # print("type of my set",type(set1))
# # print("length of my set",len(set1))
# print("minimum of set",min(set1))
# print("maximum of set",max(set1))
# print("sum of all elements of set",sum(set1))

# set1.add(9)               # Adds element 9
# print(set1)
# set1.remove(20)           # Removes element 20 (raises error if not found)
# print(set1)
# set1.discard(20)          # Removes element 20 (no error if not found)
# print(set1)
# set1.clear()              # Removes all elements
# print(set1)
# print(set1.pop())         # Removes and returns a random element
# print(set1)

# my_list = [1, 2, 2, 3, 3, 3]             # given list with duplicates
# my_set = set(my_list)                    # set() constructor Convert list/tuple to set
# print(my_set)                            # this will print by removing duplicates because set does not allow duplicates



# a = {1, 2, 3}
# b = {3, 4, 5}

# # union
# print(a.union(b))                        # or a | b
# print(a|b)

# # intersection
# print(a.intersection(b))                 # or a & b
# print(a&b)

# # difference
# print(a.difference(b))                   # or a - b
# print(a-b)

# print(b.difference(a))                   # or b - a
# print(b-a)

# # symmetric difference
# print(a.symmetric_difference(b))         # or a ^ b
# print(a^b)

# a = {1, 2, 3, 4}
# b = {3, 4, 5}
# c = {4, 5, 6}

# result = a & b | c                         # chaining set operations
# print(result)


# a = {1, 2}
# b = {1, 2, 3, 4}

# print(a.issubset(b))                      # It will print true if a is subset of b else print false
# print(b.issuperset(a))                    # It will print true if b is superset of a else print false
# print(b.issubset(a))                      # It will print true if b is subset of a else print false
# print(a.issuperset(b))                    # It will print true if a is superset of b else print false

# a = {1, 2}
# b = {3, 4}
# print(a.isdisjoint(b))                    # Checks if two sets have no common elements


# a = {1, 2}
# b = {2, 1}
# print(a == b)                             # True because sets ignore order

# c = a.copy()
# print(c)                                  # Copy of set a

import copy
dict1={"a":1,"b":2,"c":[2,3]}
dict2=dict1.copy()

dict1["a"]=10
dict2["b"]=0
dict1["c"][0]=20

print(dict1)
print(dict2)


import copy
dict1={"a":1,"b":2,"c":[2,3]}
deep=copy.deepcopy(dict1)

deep["c"][0]=99

print(dict1)
print(deep)



 




