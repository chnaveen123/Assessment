

def dec(fnc):
    def helper(*args):

     print("session Started")
     fnc(*args)

     print("session ended")
    return helper



class dwa:
    def init(self,function):
        self.function = function
    def call(self,*args):
        self.function(*args)


def dwia(name1,name2,name3):
    print(name1,name2,name3)
    def function(fnc):
        def inner(*args):
            print("session Started")
            fnc(*args)
            print("session ended")

        return inner
    return function



class cdwia:

    def init(self,name4,name5,name6):

        self.name4 = name4

        self.name5 = name5

        self.name6 = name6

    def init(self,function):

        self.function = function
    def call(self,*args):
        self.function(*args)


@dec
def fun2(a,b):
    print(f"we will win the soccer WC {a} {b}")

fun2(111, 222)


@dec
def fun3(x, y, z):
    print(f"Happy Sunday fun3 {x} {y} {z}")

fun3(10,20,30)



@dwia("Sachin","Suarav","Rahul")
def fun4(x, y):
    print(f"fun4 .. {x} {y}")

fun4(88, 77)



