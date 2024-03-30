
# it automatically work like constructor



class A():
    def __init__(self,name,age):
        self.name=name
        self.age=age


    def __str__(self):
        return f"hey im {self.name} and im {self.age} years old"


obj=A("vicky",20)

print(obj)