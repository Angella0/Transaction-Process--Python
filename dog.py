class Dog:
    def __init__(self,name,age,bark):
        self.name = name
        self.age = age
        self.bark = bark
    def barking(self): 
        return f" Hello my dog barks like {self.bark}"
    def protective(self):
        return f"I have a protector called {self.name} and that is my dog"

    