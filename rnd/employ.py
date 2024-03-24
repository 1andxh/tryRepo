from typing import Self


class Employee:
    def __init__(self, first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@edu.com'
        
    def fullname():
        return '{} {}'. format(Self.first, Self.last)
    
         

emp_1 = Employee('Daniel','fletcher',50000)
emp_2 = Employee('Sarah','Duke',75000)

print(emp_1.email)
print(emp_2.email)
print(emp_1.fullname())

# print('{} {}'.format(emp_1.first, emp_1.last)) print full name