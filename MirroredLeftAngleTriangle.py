n = int(input("Enter number of rows: "))
i = n
while i >= 1:
    print(" " * (n - i) + '*' * i)
    i = i - 1
