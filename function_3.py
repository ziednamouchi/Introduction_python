#function 
def answer():
    print(42)
answer()
def run_something(func):
    func()
run_something(answer)
def add_args(arg1, arg2):
    print(arg1 + arg2)
def run_something_with_args(func, arg1, arg2):
    func(arg1, arg2)
run_something_with_args(add_args, 5, 9)
def sum_args(*args):
    return sum(args)
print(sum_args(1,2,3))
def run_with_positional_args(func,*args):
    return func(*args)
print(run_with_positional_args(sum_args, 1, 2, 3, 4))
#inner functions
def outer(a,b):
    def inner(c,d):
        return c + d
    return inner(a,b)
print(outer(4,8))
def knights(saying):
    def inner(quote):
        return "We are the knights who say:'%s'" % quote
    return inner(saying)
print(knights('hi!'))
#closures
def knights2(saying):
    def inner2():
        return "We are the knights who say:'%s'" % saying
    return inner2
a= knights2('Duck')
b=knights2('Hasenpfeffer')
print(a())
print(b())
