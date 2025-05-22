from inheritance.Car import Car
from inheritance.ElectroCar import ElectroCar
from inheritance.RaceCar import RaceCar

race_car = RaceCar("Ferrari",5000,600)
electro_car = ElectroCar("Tesla",3000,100)

# print(isinstance(race_car,Car))


# print(electro_car.get_info())
cars = [race_car,electro_car]

for car in cars:
    #Предоставляем скидку на гоночные авто
    if isinstance(car,RaceCar):
        car.add_discaunt(1500)
    print(car.get_info())
    print("*"*50)
