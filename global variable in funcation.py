#Use golobal 
n=4
def f1():
    global n
    n = n**4
    print(n)
f1()

