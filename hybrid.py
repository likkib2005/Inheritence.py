class A:
    def display(self):
        print("Display from A class")
class B(A):
    def display(self):
        print("Display from B class ")
class C:
    def show(self):
        print("Hi from c class")
class D(B,C):
    def display(self):
        print("Display from D class")
d1=D()
d1.show()
A.display(d1)
d1.display()
