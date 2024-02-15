def demo(name,age):
    print(name,age)


demo('King',25)

def func(*args):
    func1 = (20, 40, 80)
    print(func1)


func()

def func1(*args):
    for i in args:
        print(i)

func1(9.4, 57, 24)
func1(34,100)


