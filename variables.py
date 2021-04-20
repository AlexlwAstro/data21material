"""
variable_name = 'Hello'
print(variable_name + str(50))
print(type(variable_name))

#print ("What is your name?")
name = input("What is your name?\n")

# print("Hello, " + name)
# same as ...
print(f"Hello, {name}")


# ask for name, height, height, DoB
name = input("What is your name?\n")
age = input("How old are you?\n")
height = input("How tall are you?\n")
DoB = input("When were you born?\n")

print(f"Hello, {name}! You are {age} years old, {height} metres tall and you were born on {DoB}")

a = 80
b = 63
print(a > b)
print(a == b)

a = 'one-quote string'
b = "two-quote string"

print(a,'\t',b)

greeting = "Hello World!"

print(greeting[::-1])
print(greeting.count(''))

print (greeting.isalpha())
print (greeting.endswith('!'))

x = 10
y = 0
print(bool(x))
print(bool(y))

# lists
shopping_list = ["eggs", "milk", "bread"]
shopping_list[0] = "bacon"
print(shopping_list*2, type(shopping_list))

# tuples
shopping_tuple = ("eggs", "milk", "bread")
print(shopping_tuple, type(shopping_tuple))

student_dict = {
    'FirstName' : 'Alex',
    'LastName' : 'Lisboa-Wright',
    'List grades' : [82,79,90,85]
}

# dictionaries - are hashable, random print order
print(student_dict)
student_dict['FirstName'] = 'Hugo'
print(student_dict)
student_dict.pop('FirstName')
print(student_dict)

# sets - ignore duplicates, are hashable, random print order (unless using set seeds)
car_brands = {'BMW', 'Mazda', 'Hyundai', 'VW'}
car_brands.add('Mercedes')
print(car_brands)
"""
# control flows - if statements, for, while loops
age = 4
if (age >= 18):
    print('Adult')
elif (age <= 5):
    print('Free entry')
else:
    print('Child')

data1 = [1,2,3]
data2 = [4,5,6]
datas = (data1,data2)
for i in datas:
    print(i)
    for k in i:
        print(k)

# careful with while loops - they will keep going forever if condition is never false!!!
x = 0
while (x < 10):
    print(x,'continue loop')
    if (x == 4):
        print('stopping')
        break
    x += 1