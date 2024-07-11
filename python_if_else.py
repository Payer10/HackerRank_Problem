n = int(input().strip())
if n%2==1:
    print("Weird")
else:
    if n>=2 and 5>=n:
        print("Not Weird")
    elif n>=6 and 20>=n:
        print("Weird")
    else:
        print("Not Weird")
