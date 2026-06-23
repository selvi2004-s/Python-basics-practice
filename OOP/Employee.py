from abc import ABC, abstractmethod

class Employee(ABC):

 def __init__(self,name,salary):
        self._name=name
        self.salary=salary
    
 @property
 def name(self):
        return self._name
    
 @property
 def salary(self):
       return self._salary
   
 @salary.setter
 def salary(self,salary):
      if salary<0:
           raise ValueError("No negative values")
      self._salary=salary

 @abstractmethod
 def calculate_monthly_pay(self):
      pass
 
 def describe(self):
      return f'{self.name} earns ${self.calculate_monthly_pay()}/month'
 
class FullTimeEmployee(Employee):
     
   def __init__(self, name,annual_salary):
    super().__init__(name, annual_salary)

   def calculate_monthly_pay(self):
       return self.salary/12
   
class Contractor(Employee):
    def __init__(self, name, hourly_rate, hours_per_month):
       self.hourly_rate = hourly_rate
       self.hours_per_month=hours_per_month
       super().__init__(name, hourly_rate*hours_per_month)
    
    def calculate_monthly_pay(self):
        return self.hourly_rate*self.hours_per_month
    

team = [
    FullTimeEmployee("Selvi", 60000),
    Contractor("Aram", 50, 80),
    FullTimeEmployee("Anna", 72000),
]

for emp in team:
    print(emp.describe())
# Selvi earns $5000.0/month
# Aram earns $4000/month
# Anna earns $6000.0/month

# Should fail
#Employee("nope", 1000)

 #ft = FullTimeEmployee("Test", 60000)
 #ft.salary = -1000   # should fail



          

     
