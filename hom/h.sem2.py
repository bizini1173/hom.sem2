from abc import ABC, abstractmethod

# Абстрактный класс Vehicle
class Vehicle(ABC):
    def __init__(self, id, brand, model, year, vehicle_type):
        self.id = id
        self.brand = brand
        self.model = model
        self.year = year
        self.vehicle_type = vehicle_type

    @abstractmethod
    def startEngine(self):
        pass

    @abstractmethod
    def stopEngine(self):
        pass

    @abstractmethod
    def accelerate(self, speed):
        pass

    @abstractmethod
    def brake(self):
        pass

    @abstractmethod
    def displayInfo(self):
        pass

# Класс Car, наследующий от Vehicle
class Car(Vehicle):
    def __init__(self, id, brand, model, year, fuel_capacity):
        super().__init__(id, brand, model, year, "Car")
        self.fuel_capacity = fuel_capacity
        self.current_fuel_level = 0

    def startEngine(self):
        print(f"Запуск двигателя {self.vehicle_type} {self.brand} {self.model}")

    def stopEngine(self):
        print(f"Остановка двигателя {self.vehicle_type} {self.brand} {self.model}")

    def accelerate(self, speed):
        print(f"Увеличение скорости {self.vehicle_type} {self.brand} {self.model} на {speed} km/h.")

    def brake(self):
        print(f"Прекращение движения {self.vehicle_type} {self.brand} {self.model}.")

    def refuel(self, liters):
        if self.current_fuel_level + liters <= self.fuel_capacity:
            self.current_fuel_level += liters
            print(f"{liters} литров заправлено. Текущий уровень топлива: {self.current_fuel_level}/{self.fuel_capacity}")
        else:
            print(f"Невозможно заправить. Превышает емкость топливного бака. Текущий уровень топлива: {self.current_fuel_level}/{self.fuel_capacity}")

    def displayInfo(self):
        print(f"{self.brand} {self.model}, Год: {self.year}, Уровень топлива: {self.current_fuel_level}/{self.fuel_capacity}")
# Интерфейс Flyable
class Flyable(ABC):
    @abstractmethod
    def takeOff(self):
        pass

    @abstractmethod
    def land(self):
        pass

# Интерфейс Swimmable
class Swimmable(ABC):
    @abstractmethod
    def startSwimming(self):
        pass

    @abstractmethod
    def stopSwimming(self):
        pass
# Класс FlyingVehicle, реализующий абстрактный класс Vehicle и интерфейс Flyable
class FlyingVehicle(Vehicle, Flyable):
    def __init__(self, id, brand, model, year):
        super().__init__(id, brand, model, year, "Fly")

    def startEngine(self):
        print(f"Запуск двигателя {self.vehicle_type} {self.brand} {self.model}")

    def stopEngine(self):
        print(f"Остановка двигателя {self.vehicle_type} {self.brand} {self.model}")

    def accelerate(self, speed):
        print(f"Увеличение скорости {self.vehicle_type} {self.brand} {self.model} на {speed} km/h.")

    def brake(self):
        print(f"Прекращение движения {self.vehicle_type} {self.brand} {self.model}.")

    def displayInfo(self):
        print(f"{self.brand} {self.model}, Год: {self.year}")

    def takeOff(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} взлетает.")

    def land(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} приземляется.")


# Класс SwimmingVehicle, реализующий абстрактный класс Vehicle и интерфейс Swimmable
class SwimmingVehicle(Vehicle, Swimmable):
    def __init__(self, id, brand, model, year):
        super().__init__(id, brand, model, year, "Swim")

    def startEngine(self):
        print(f"Запуск двигателя {self.vehicle_type} {self.brand} {self.model}")

    def stopEngine(self):
        print(f"Остановка двигателя {self.vehicle_type} {self.brand} {self.model}")

    def accelerate(self, speed):
        print(f"Увеличение скорости {self.vehicle_type} {self.brand} {self.model} на {speed} узла.")  # Указание скорости в узлах для плавающего транспорта.

    def brake(self):
        print(f"Прекращение движения {self.vehicle_type} {self.brand} {self.model} в воде.")

    def displayInfo(self):
        print(f"{self.brand} {self.model}, Год: {self.year}")

    def startSwimming(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} начинает плавание.")

    def stopSwimming(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} прекращает плавание.")

# Класс Aircraft, наследующий от Vehicle
class Aircraft(Vehicle, Flyable):
    def __init__(self, id, brand, model, year, max_altitude):
        super().__init__(id, brand, model, year, "Aircraft")
        self.max_altitude = max_altitude
        self.is_flying = False

    def startEngine(self):
        print(f"Запуск двигателя {self.vehicle_type} {self.brand} {self.model}")

    def stopEngine(self):
        print(f"Остановка двигателя {self.vehicle_type} {self.brand} {self.model}")

    def takeOff(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} взлетает.")
        self.is_flying = True

    def land(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} приземляется.")
        self.is_flying = False

    def accelerate(self, speed):
        print(f"Увеличение скорости {self.vehicle_type} {self.brand} {self.model} на {speed} km/h.")

    def brake(self):
        print(f"Прекращение движения {self.vehicle_type} {self.brand} {self.model} в воздухе.")

    def displayInfo(self):
        print(f"{self.brand} {self.model}, Год: {self.year}, Максимальная высота полета: {self.max_altitude} м.")


# Класс Boat, наследующий от Vehicle
class Boat(Vehicle, Swimmable):
    def __init__(self, id, brand, model, year, max_speed):
        super().__init__(id, brand, model, year, "Boat")
        self.max_speed = max_speed
        self.is_sailing = False

    def startEngine(self):
        print(f"Запуск двигателя {self.vehicle_type} {self.brand} {self.model}")

    def stopEngine(self):
        print(f"Остановка двигателя {self.vehicle_type} {self.brand} {self.model}")

    def startSwimming(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} начинает движение по воде.")
        self.is_sailing = True

    def stopSwimming(self):
        print(f"{self.vehicle_type} {self.brand} {self.model} прекращает движение по воде.")
        self.is_sailing = False

    def accelerate(self, speed):
        print(f"Увеличение скорости {self.vehicle_type} {self.brand} {self.model} на {speed} узлов.")  # Указание скорости в узлах для плавающего транспорта.

    def brake(self):
        print(f"Прекращение движения {self.vehicle_type} {self.brand} {self.model} в воде.")

    def displayInfo(self):
        print(f"{self.brand} {self.model}, Год: {self.year}, Максимальная скорость на воде: {self.max_speed} узлов.")

class Main:
    @staticmethod
    def test_vehicles():
        # Создание объектов различных транспортных средств
        car = Car(id=1, brand="Toyota", model="Corolla", year=2023, fuel_capacity=50)
        aircraft = Aircraft(id=4, brand="AirBrand", model="AirModel", year=2023, max_altitude=10000)
        boat = Boat(id=5, brand="BoatBrand", model="BoatModel", year=2023, max_speed=30)
        
        # Демонстрация работы транспортных средств
        print("------ Test Car ------")
        car.startEngine()
        car.accelerate(100)
        car.brake()
        car.refuel(20)
        car.displayInfo()

        print("\n------ Test Aircraft ------")
        aircraft.startEngine()
        aircraft.takeOff()
        aircraft.accelerate(500)
        aircraft.land()
        aircraft.stopEngine()
        aircraft.displayInfo()

        print("\n------ Test Boat ------")
        boat.startEngine()
        boat.startSwimming()
        boat.accelerate(10)
        boat.stopSwimming()
        boat.stopEngine()
        boat.displayInfo()

if __name__ == "__main__":
    Main.test_vehicles()
