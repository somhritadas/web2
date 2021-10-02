class Employee:
    company="google"

    def showDetails(self):
        print("this is just an employee")

class Programmer(Member):
    Language=("python")

    def getLanguage(self):
        print(f"the language is {self.Language}")
    
    def showDetails(self):
        print("this is a programmer")
e=Member()
p=Programmer()
p.showDetails()
e.showDetails()
print(p.company)


class Member:
    company="visa"
    ecode= 120
    
class Freelancer:
    company="fiveer"
    level=0
    def upgradeLevel(self):
        self.level=self.level + 1

class Programmer(Employee,Freelancer):
    name="Rohit"


e=Employee()
p=Programmer()
p.upgradeLevel()
print(p.level)
print(p.company)

#multiple inheritence
class Employee:
    company="visa"
    ecode= 120
    
class Freelancer:
    company="fiveer"
    level=0
    def upgradeLevel(self):
        self.level=self.level + 1

class Programmer(Employee,Freelancer):
    name="Rohit"

#multilevel inheritance

class person:
    country="india"

    def takeBreath(self):
        print("i am breathing")

class employee(person):
    company="honda"

    def getSalary(self):
        print(f"salary is {self.salary}")

    def takeBreath(self):
        print("i am luckily breathing ++")

class programmer (employee):
   company="fivver"
    
   def getSalary(self):
       print("no salary for programmer")

   def takeBreath(self):
        print("i am breathing ..")

p=programmer()
e=employee()
pr=person()
pr.takeBreath()
e.takeBreath()
p.takeBreath()
print(e.company)
print(p.company)
print(p.country)
print(e.country)
print(pr.country)
