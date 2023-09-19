class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def greet(self,name):
        print("Hello",name+ ". My name is", self.name)

    def __str__(self):
        return ""+str(self.age)+" "+self.name
    
class Employee(Person):
    def __init__(self, name,age,job):
        super().__init__(name,age,)
        self.job = job

    def greet(self,name):
        print("Hello",name+ ". My name is", self.name,"and I work as",self.job)
    
        


def main():
    p = Person("Abdalle Wais",30)
    p.greet("Abbe")
    print(p)
    e = Employee("Khadar",28, "Koodari")
    e.greet("Kha!")
    print(e)

if __name__ == "__main__":
    main()


