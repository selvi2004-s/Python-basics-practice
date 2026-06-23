class Vehicle:

    def __init__(self, make, model):
        self._make = make
        self._model = model

    @property
    def make(self):
        return self._make

    #  @make.setter
    #  def make(self, value):
    #      self.make._ = value

    @property
    def model(self):
        return self._model

    #   @make.setter
    #  def model(self, value):
    #     model._ = value

    def describe(self):
        return f"{self.make} {self.model}"

    def move(self):
        return f"{self.make} {self.model} is moving"

    def __str__(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):

    def __init__(self, make, model, num_door):
        super().__init__(make, model)
        self._num_door = num_door

    @property
    def num_door(self):
        return self._num_door

    # @num_door.setter
    # def num_door(self,value):
    # self._num_door = value

    def move(self):
        return f"{self.make} {self.model} is driving on the road"

    def __str__(self):
        return f"Car: {self.make} {self.model} ({self.num_door} doors)"


class Boat(Vehicle):

    def __init__(self, make, model, max_speed_knots):
        super().__init__(make, model)
        self.max_speed_knots = max_speed_knots

    @property
    def max_speed_knots(self):
        return self._max_speed_knots

    @max_speed_knots.setter
    def max_speed_knots(self, value):
        if value <= 0:
            raise ValueError("Value should be positive")
        self._max_speed_knots = value

    def move(self):
        return f"{self.make} {self.model} is sailing"


c = Car("Honda", "Civic", 4)
b = Boat("Yamaha", "WaveRunner", 50)

#print(c.make)
#print(c.describe())
#print(c.move())
#print(c)
#print(b.move())
#b.max_speed_knots = 70
#print(b.max_speed_knots)


#for v in [c, b]:
    #print(v.move())


class BankAccount:

    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        if initial_balance <= 0:
            raise ValueError("Balance can't be negative")
        self._balance = initial_balance

    @property
    def owner(self):
        return self._owner

    @owner.setter
    def owner(self, owner):
        if not isinstance(owner, str):
            raise TypeError("Owner should be name")
        if not owner:
            raise ValueError("Name cannot be empty")
        self._owner = owner

    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        if value <= 0:
            raise ValueError("Amount cant be negative or zero")
        self._balance += value

    def withdraw(self, value):
        if value <= 0:
            raise ValueError("Amount cant be negative or zero")
        if value > self.balance:
            raise ValueError("Insufficient funds: cannot withdraw more than balance")
        self._balance -= value

    def __str__(self):
      return f"{self.owner}'s account: ${self.balance}"

acc = BankAccount("Selvi", 100)
print(acc)                   # "Selvi's account: $100"
print(acc.balance)           # 100
print(acc.owner)             # "Selvi"

acc.deposit(50)
acc.withdraw(70)
print(acc.balance)           # 80

acc.owner = "Selvi Smith"
print(acc.owner)            

# These should all fail
# acc.balance = 1_000_000
# acc.owner = ""
# acc.deposit(-50)
# acc.withdraw(99999)
# BankAccount("", 100)]

