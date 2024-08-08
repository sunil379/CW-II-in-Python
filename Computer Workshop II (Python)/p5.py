def comparison(n1,n2):
    if n1%2==0 and n2%2==0:
        if(n1<n2):
            min =  n1
        else:
            min =  n2
        print("The Lesser value of two given numbers is ",min)
    elif(n1%2!=0 or n2%2!=0):
        if(n1>n2):
            max = n1
        else:
            max =  n2
        print("The Greater value of two given numbers is ",max)
            
a = input("Enter a value for number 1 ")
b = input("Enter a value for number 2 ")
result  = comparison(int(a),int(b))
