def calculation(a,b):
    add = a + b
    sub = a - b
    return add , sub

res = calculation(40,10)
print(res)


def show_employee(name,salary=9000):
    print('name: ', name, "salary: ", salary)


show_employee('jessa')
show_employee('ben', 12000)

def outer(a,b):
    def inner(a,b):
        addition = a + b
        return addition
    sum = inner(a,b)
    return sum + 5


result = outer(5,10)
print(result)

# Create a recursive function
def recurring(num):
    if num:
        # call same function by reducing number by 1
        return num + recurring(num-1)
    else:
        return 0

res = recurring(10)
print(res)

# Assign a different name to function and call it through the new name
def display_student(name,age):
    print(name,age)

def show_student(name,age):
    display_student = show_student
    print(name,age)

display_student("emma", 26)   
show_student("emma", 26)

# print without list constructor
for i in range(4,30,2):
   print(i)

# or 
print(list(range(4,30,2)))


# Find the largest item from a given list
x = [4,6,8,24,12,2]
print(max(x))
# or
