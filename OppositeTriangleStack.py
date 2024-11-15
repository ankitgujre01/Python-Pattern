n = int(input("enter no. of element"))
i = 1
while i<=n :
    print('*' * i + ' ' * (n-1))
    i = i+1
    # print(i)
i = i-2
while i>0 :
    print(" " * (n - i) + '*' * i)
    i = i-1