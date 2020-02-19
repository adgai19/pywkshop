def hello():
        '''prints  hello world'''
        print("hello world")

def helloname(name):
        '''prints hello S where S '''
        print("hello "+name)

def returnsum(a,b):
        return a+b

def returnname():
        return "random"

def rec(no):
        if no==0:
                return 0
        else:return rec(no-1)+no



def defaultarg(test="cowsay"):
        print("hello",test)

def multipleargs(arg1, arg2="hello"):
        print(arg1,arg2)
hello()

helloname("aditya")

ans=returnsum(5,10)
print(ans)

print(returnsum("hello new ","world"))

print(returnname())


print(rec(5))
print(defaultarg("cow"))
print(defaultarg())

multipleargs(arg2="hello",arg1="world")
print(hello.__doc__ )
