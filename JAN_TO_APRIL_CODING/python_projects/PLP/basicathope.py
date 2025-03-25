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

print('Hello' not in x) # not in operator  . Remember python is case sensitive