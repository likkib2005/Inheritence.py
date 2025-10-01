class Human:
    def work(self):
        print("I can work")
    def sleep(self):
        print("I can sleep")

class Male(Human):
    def work(self):
        print("I can code")
    def eat(self):
        print("I can eat")
class Boy(Male):
    def work(self):
        print("I can test")
    def flirt(self):
        print("I can flirt")
Boy_1=Boy()
Boy_1.work()
Male.work(Boy_1)
Boy_1.flirt()

class Human:
    def __init__(self,num_heart):
        self.eyes=2
        self.nose=1
        self.num_heart=num_heart
    def work(self):
        print("I can work")
    def eat(self):
        print("I can eat")
class Male(Human):
    def __init__(self,language):
        self.name="likhitha"
        self.language=language
    def work(self):
        print("I can code")
    def sleep(self):
        print("I can sleep")
class Boy(Male):
    def __init__(self,heart,language):
        Human. __init__(self,heart)
        Male. __init__(self,language)
        self.address="palamaner"
    def work(self):
        print("I can test")
Boy_1=Boy(1,"python")
print(Boy_1.nose)
print(Boy_1.eyes)
print(Boy_1.language)