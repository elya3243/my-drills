def f1():
    a = {"book": 'کتاب', "hat": 'کلاه', "sea": 'دریا'}
    condition = True
    while condition:
        b = input("Enter your word:", )
        c = a.get(b, "Has not exist.")
        if b == "exit":
            condition = False
        print(c)


f1()
