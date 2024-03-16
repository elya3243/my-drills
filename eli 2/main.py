def f2():
    name=[]
    for x in range(5):
        a = input("please enter your student name:")
        name.append(a)
    print ("the students are:",",".join(name))
f2()