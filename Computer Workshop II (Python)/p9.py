def multiply(numbers):
    result=1
    for i in numbers:
        result*=i
    print("Product of elements of the list : ",result)
no_list = [1,2,3,4,5]
print("List : ",no_list)
result = multiply(no_list)