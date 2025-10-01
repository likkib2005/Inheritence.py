class Human:
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def work(self):
        print("I can test")
    def sleep(self):
        print("I can sleep")
Boy_1=Boy()
Boy_1.eat()
Boy_1.work()
Male.work(Boy_1)
Boy.work(Boy_1)
Male_1=Male()
Male_1.flirt()
print(Boy.mro())

class Human:
    def __init__(self,heart):
        self.eyes=2
        self.nose=1
        self.heart=heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male:
    def __init__(self,name):
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        print("I can code")
class Boy(Human,Male):
    def __init__(self,name,heart,language):
        self.language=language
        Human. __init__(self,heart)
        Male. __init__(self,name)
Boy_1=Boy("likitha",1,"python")
print(Boy_1.eyes)
print(Boy_1.nose)
print(Boy_1.name)
print(Boy_1.heart)
print(Boy_1.language)