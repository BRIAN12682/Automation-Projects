def func(a , b=2,*args, **kwargs):
    print (a, b, args, kwargs)
func(1,3,4,5, c=6,d=7)


a =[1,2,3,4,5]
b=[i for i in a if i % 2 ==0]
print (b)