class Counter:

   def __init__(self, current: int = 1, min_value: int = 0, max_value: int = 10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start: int):
       if self.min_value <= start <= self.max_value:
           self.current = start
       else:
           raise ValueError("Поточне значення повинно бути в межах мінімального та максимального значень.")

   def set_max(self, max_max: int):
       if max_max >= self.min_value:
           self.max_value = max_max
           if self.current > self.max_value:
               self.current = self.max_value
       else:
           raise ValueError("Помилка! Максимальне значення не може бути менше за мінімальне.")

   def set_min(self, min_min: int):
       if min_min <= self.max_value:
           self.min_value = min_min
           if self.current < self.min_value:
               self.current = self.min_value
       else:
           raise ValueError("Помилка! Мінімальне значення не може бути більше за максимальне.")

   def step_up(self) -> None:
       if self.current < self.max_value:
           self.current += 1
       else:
           raise ValueError(f"Досягнуто максимуму: {self.max_value}. Неможливо збільшити значення.")

   def step_down(self) -> None:
       if self.current > self.min_value:
           self.current -= 1
       else:
           raise ValueError((f"Досягнуто мінімуму: {self.min_value}. Неможливо зменшити значення."))

   def get_current(self)-> int:
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'
