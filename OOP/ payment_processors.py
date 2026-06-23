from abc import ABC, abstractmethod

class PaymentMethod(ABC):

 def __init__ (self,name):
  #name is read only property, then i will write getter but not write setter
  self._name = name

 @property
 def name(self):
  return self._name

 @abstractmethod
 def pay(self,amount):
  pass

 @abstractmethod
 def refund (self,amount):
  pass

 def describe (self):
  return f'Payment method: {self.name}'

class CreditCard(PaymentMethod):
  
 def __init__(self, name):
   super().__init__(name)

 def pay(self,amount):
    return f'CreditCard charged {amount}'
   
 def refund(self,amount):
    return f'CreditCard refunded {amount}'
   
class PayPal(PaymentMethod):
 def __init__(self, name):
   super().__init__(name)

 def pay(self,amount):
    return f'PayPal charged {amount}'
   
 def refund(self,amount):
    return f'PayPal refunded {amount}'

def process_payment(method,amount):
  return method.pay(amount)

cc = CreditCard("Visa")
pp = PayPal("Personal")

print(cc.describe())           # "Payment method: Visa"
print(process_payment(cc, 50)) # "CreditCard charged $50"
print(process_payment(pp, 75)) # "PayPal charged $75"


