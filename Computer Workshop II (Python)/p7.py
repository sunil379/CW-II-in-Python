def count_upper_lower(str):
    lower = upper = 0
    for char in str:
        if(char.isupper()):
            upper+=1
        elif char.islower():
            lower+=1
    print("Uppercase count : ",upper)
    print("Lowercase count : ",lower)

sentence = "This is a Python Code."
count_upper_lower(sentence)
