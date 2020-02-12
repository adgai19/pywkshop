def hello():
        print("hello world")

def helloname(name):
        print("hello "+name)

def returnsum(a,b):
        return a+b

def returnname():
        return "random"

def rec(no):
        if no==0:
                return 0
        else:return rec(no-1)+no
hello()

helloname("aditya")

ans=returnsum(5,10)
print(ans)

print(returnsum("hello new ","world"))

print(returnname())


print(rec(5))