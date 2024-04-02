#passing Dict To Function

def myFunc(arg):
    for key in arg:
        print("key",key,"value:",arg[key])

Dict={'a':1, 'b':2, 'c':3}
myFunc(Dict)