'''pyhon program to calculte function
with many unknownparameters of arguments
where can calculate the sum of the parameters'''

def fun_sum (*numbers):
    sum = 0
    for i in numbers:
        sum+=i
    return sum
print(fun_sum(1,2,3,7,8))