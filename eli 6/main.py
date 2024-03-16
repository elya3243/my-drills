def f1():
    v = []
    condition_b = True
    b = input("How many number you need?")
    while condition_b:
        try:
            b = int(b)
            condition_b = False
        except:
            b = input("Pleas enter a number not term:")
    for i in range(int(b)):
        condition_c = True
        c = input("Enter your number:")
        while condition_c:
            try:
                c = int(c)
                condition_c = False
            except:
                c = input("Try again! Enter a number not term:")
        v.append(int(c))
    s = sum(v)/len(v)
    print(v,"=",s)
f1()
