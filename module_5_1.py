class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        for i in range(0, new_floor + 1):
            if 1 <= new_floor <= self.number_of_floors:
                print(i)
                continue
            if 0 == new_floor:
                print(f'Это подвал или парковка на нижнем этаже: {new_floor}')
                continue
            else:
                print(f'Такого этажа не существует: {new_floor}')
                break

h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
print("*****************************")
h3 = House('ЖК Хвойная роща', 7)
h3.go_to(0)
print("*****************************")
h3.go_to(3)
print("*****************************")
h3.go_to(8)
print("*****************************")
h3.go_to(7)