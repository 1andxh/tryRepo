import datetime as dt
import turtle
now = dt.datetime.now()
print(now)

# for loop to calculate sum of a list
num = [20, 33, 6 , 87]
sum = 0
for i in num:
    sum =+ i
print(sum)

programmingLanguages = {'J': 'Java', 'P': 'Python'}
for key, value in programmingLanguages.items():
    print(key, value)



def greet(course):
    print('wasgood bro')
    print( f"is {course} coming on today?")


greet("DCIT409")


