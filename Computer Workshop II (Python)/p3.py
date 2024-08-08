for i in range(1,100):
    if (i%3==0)and(i%5==0):
        print("FIZZBUZZ");
        continue
    elif i%3==0:
        print("FIZZ")
        continue
    elif i%5==0:
        print("BUZZ");
        continue
    else:
        print(i)