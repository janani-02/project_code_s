# project_code_s
def add(x,y):
    print("x is {} and y is {}".format(x,y))
    return x+y
add(5,6)


def varargs(*args):
    return args
varargs(1,2,3)

def keyword_args(**kwargs):
    return kwargs
keyword_args(gig="foot",loch="ness")

def all_the_args(*args,**kwargs):
    print(args)
    print(kwargs)
all_the_args(1,2,a=3,b=4)


def swap(x,y):
    return y,x
x=1
y=2
x,y=swap(x,y)


x=5
def set_x(num):
    x=num
    print(x)

def set_global_x(num):
    global x
    print(x)
    x=num
    print(x)


def create_adder(x):
    def adder(y):
        return x+y
    return adder
add_10=create_adder(10)
add_10(3)    



import math
print(math.sqrt(16))



from math import ceil, floor
print(ceil(3.7))
print(floor(3.7))
