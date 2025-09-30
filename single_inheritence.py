class Human:
    def __init__(self,num_heart):
        self.num_eyes=2
        self.num_nose=1
        self.num_heart=num_heart
    def eat(self):
        print("I can eat")
    def work(self):
        print("I can work")
class Male(Human):
    def __init__(self,name,heart):
        super(). __init__(heart)
        self.name=name
    def flirt(self):
        print("I can flirt")
    def work(self):
        super().work()
        print("I can code")
male_1=Male("Rithik",1)
print(male_1.num_eyes)
print(male_1.num_nose)
print(male_1.num_heart)
male_1.work()
male_1.flirt()
male_1.eat()

    
    