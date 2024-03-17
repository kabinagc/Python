n = int(input("enter a number"))

if(n==0 or n== 1):
    print(n,"number is either prime or composite")
elif n>1 :


    for n in range(2, 1000):
        if (n% range == 0):
             print('number is prime')
        else:
            print('number is composite')
else:
    print("enter a valid number")