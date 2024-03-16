class Mostatil:
    def __init__(self, tol, arz):
        self.tol = tol
        self.arz = arz

    def area(self):
        area = self.tol * self.arz
        print(f"area is:{area}")

    def mohit(self):
        mohit = (self.tol + self.arz) * 2
        print(f"mohit is:{mohit}")
def f1():
    a = input("Select your request:")
    b = input("Enter tol:")
    c = input("Enter arz:")
    m1 = Mostatil(int(b), int(c))

    if a == "mohit":
        m1.mohit()
    elif a == "area":
        m1.area()
f1()


