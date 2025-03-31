a = 2
b = 7

a += b # a= a+b
a -= b # a= a-b

print('a == b = ', a==b) # equal to operator  
print('a !=b =', a !=b) # not equal to operator

print('a += b')

print((a > 2) and (b < 10)) # and operator
a +=b
print (a)

a == b #cannot be seen since there is no print statement

print(a==b) # equal to operator  it is seen since there is a print statement

print((a > 2) and (b >= 10) )# and operator

x = "hello world"
y = {1:'a', 2:'b'}
print('h' in x) # in operator
print('hello' not in x) # not in operator
print(1 in y) # in operator
print('a' in y) # in operator
# The in operator is used to check if a value is present in a sequence (list, range, string etc). It returns True if the value is present, else it returns False. The not in operator is used to check if a value is not present in a sequence (list, range, string etc). It returns True if the value is not present, else it returns False

print('Hello' not in x) # not in operator  . Remember python is case sensitivei

list_a = [1,2,3,4,5]
 #index   0 1 2 3 4
print(list_a[4])
print(list_a[0:3]) # slicing   .this exludes the last index that is 3 in this case
print(list_a[0:4]) # slicing    .this exludes the last index that is 4 in this case
print(list_a[0:4:2]) # slicing with step of 2 in this case .this exludes the last index that is 4 in this case
print(list_a[1:4]) # slicing    .this exludes the last index that is 4 in this case

print(list_a[1:]) # slicing    .this doesnt exlude the last index that is 4 in this case
print(list_a[:3]) # slicing    .this exludes the last index that is 4 in this case
print(list_a[:]) # slicing    .this doesnt exlude the last index that is 4 in this case

list_a[2] = 10
print(list_a) # list is mutable

print(len(list_a)) # length of list gives the number of elements in the list
#--that is 5 in this case meaning 5 numbers in the list
list_a.insert(len(list_a), 7) # insert 7 at the end of the list
print(list_a) # list is mutable
list_a.append(8) # append 8 at the end of the list
print(list_a) # list is mutable
#list_a.remove(3) # remove 3 from the list
print(list_a.append(9)) # append 9 at the end of the list

#list_a.pop(2) # remove the element at index 2 from the list
#list_a.clear() # remove all elements from the list
list_a.sort() # sort the list in ascending order
print(list_a) # list is mutable
print(list_a.count(2)) # count the number of times 2 appears in the list

print(list_a.index(2)) # find the index of 2 in the list
if 2 in list_a[2:]:
	print(list_a.index(2, 2)) # find the index of 2 in the list starting from index 2
else:
	print("Value 2 not found starting from index 2")
	
#list_a.reverse() # reverse the list
list_a.extend([11, 12, 13]) # extend the list with elements from another list
print(list_a) # list is mutable
#list_a.extend(range(14, 16)) # extend the list with elements from a range

print(list_a.append(17)) # append 9 at the end of the list returns None
print(list_a) # list is mutable

list_a.extend(range(14, 18)) # extend the list with elements from a range   it exludes the last index that is 18 in this case
#the function range(14, 18) returns a range object with elements 14, 15, 16, 17
print(list_a) 

list_a.extend([18,19]) # extend the list with elements from another list here the last number which is 19 is included
print(list_a) 
list_a.pop() # remove the last element from the list
print(list_a) #poping works with index

del list_a[7]
print(list_a) # delete the element at index 7 from the list which is 10

list_a.remove(18) # remove the element 10 from the list  languages.remove("Python") # remove the element "Python" from the list
for item in list_a:
#for loop it is
	#print(item, end=' ') # print the elements of the list separated by space.... i dont elewa this

	print(item) #arranges the items downwards due for loop
numbers = [numbers*numbers for numbers in range(1, 11)] # list comprehension
print(numbers) # list comprehension
#a list can have strings, numbers, lists, dictionaries, tuples, sets etc as elements

capital_cities = {"Nepal": "Kathmandu", "India": "New Delhi", "USA": "Washington D.C."}
print(capital_cities["Nepal"]) # access the value of the key "Nepal"
print(capital_cities.keys()) # access the value of the key "India"

#a set doesnt accept duplication,a set is mutable,in sets there is 
# no indexing hence the elements come in different order when they are printed
# a set is unordered, unindexed, and unchangeable
empty_set = set() # create an empty 

print(empty_set) # print the empty set
empty_set.add(1) # add an element to the set
print(empty_set) # print the set

empty_dictionary ={}#creates an an empty dictionary
print(empty_dictionary) # print the empty dictionary

numbers2 = {1, 2, 3, 4, 5} # create a set with elements 1, 2, 3, 4, 5
print("Initial set:",numbers2) # print the set
numbers2.add(6) # add an element to the set
print("updated set:",numbers2) # print the 

companies = {"Lacoste", "Ralph Lauren"}

tech_companies = ["apple", "google", "apple"]
companies.update(tech_companies)
print(companies)
companies.discard("apple")
print(companies)
for company in companies:
	print(company) # print the elements of the set separated by space
print(len(companies)) # print the length of the set which  is 3 in this case
print("apple" in companies) # check if "apple" is in the set

