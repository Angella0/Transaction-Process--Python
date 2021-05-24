class Car:

    def __init__(self,model,make):
        self.model = model
        self.make = make
        
    def start(self):
        return f"I am proud of my car {self.model}, It is super fast "
    def accelerate(self,accelerate,speed):
        return accelerate+speed   



        