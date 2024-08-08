str = "print only the word that starts with s in this sentence"
for i in str.split():
    if len(i)%2==0:
        print(i)
