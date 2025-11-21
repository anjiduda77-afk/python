def fun(n):
    if n<=0:
        print("Incorrect input")

    elif n==1:
        return 0
    elif n==2:
        return 1
    else: 
        return fun(n-1)+fun(n-2)
    print(fun(20))
    