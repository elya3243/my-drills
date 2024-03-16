class Cal:#(calculate)
    def __init__(self,a ,b):
        self.a = a
        self.b = b
    def jam(self):
        result = self.a + self.b
        print(result)
    def menha(self):
        result = self.a - self.b
        print(result)
    def zarb(self):
        result = self.a * self.b
        print(result)
    def taghsim(self):
        result = self.a / self.b
        print(result)
def f1():
    condition = True
    while condition:
        c = input('What can i do?')
        a = input('Enter a number:')
        b = input('Enter a number elss:')

        adad = Cal(int(a),int(b))

        if c == "jam":
            adad.jam()
        elif c == "menha":
            adad.menha()
        elif c == "zarb":
            adad.zarb()
        elif c == "taghsim":
            adad.taghsim()
        d = input('Do you have any question?')
        if d == 'No':
            condition = False
        elif d == "Yes":
            condition = True
f1()