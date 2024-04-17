class House:
  def __init__(self):
    self.numberOfFloors=10

  def print_current_floor(self):
    for floor in range(1, self.numberOfFloors + 1):
      print("Текущий этаж равен", floor)

house = House()
house.print_current_floor()