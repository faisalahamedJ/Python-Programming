ch = raw_input("Enter the Input\n")
for i in ch:
    x = i.lower()
    if(x in ('a','e','i','o','u')):
        print(i, "is Vowel")
    else:
        print(i, "is Consonant")
