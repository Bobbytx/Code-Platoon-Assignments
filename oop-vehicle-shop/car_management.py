class CarManager:
    
    all_cars = {}
    total_cars = 0
    id = 0

    def __init__ (self, make, model, year, mileage, services = None):
        CarManager.total_cars += 1
        self._make = make
        self._model = model
        self._year = year
        self._mileage = mileage
        self._services = services or []
        self._id = CarManager.total_cars
        CarManager.all_cars[self] = self

    @property
    def get_make(self):
        return self._make
        
    @get_make.setter
    def set_make(self, new_make):
        self._make = new_make

    @property
    def get_model(self):
        return self._model
        
    @get_model.setter
    def set_model(self, new_model):
        self._model = new_model

    @property
    def get_year(self):
        return self._year
        
    @get_year.setter
    def set_year(self, new_year):
        self._year = new_year

    @property
    def get_mileage(self):
        return self._mileage
        
    @get_mileage.setter
    def set_mileage(self, new_mileage):
        self._mileage = new_mileage

    @property
    def get_services(self):
        return self._services

    @get_services.setter
    def set_services(self, new_services):
        self._services.append(new_services)


    def run_menu():
        choice = '0'
        while choice != '7':
            print("---- WELCOME ----\n1. Add a car \n2. View all cars\n3. View total number of cars\n4. See a car's details\n5. Service a car\n6. Update mileage\n7. Quit\n")

            choice = input("Choose an option: ")

            if choice == '1':
                CarManager.add_a_car()
            if choice == '2':
                CarManager.view_all_cars()
            if choice == '3':
                print(f'Total Cars: {CarManager.total_cars}')
            if choice == '4':
                car_id = input("Enter the ID of the car you want to see details of: ")
                CarManager.view_car_details(car_id)
            if choice == '5':
                pass
            if choice == '6':
                car_id = input("Enter the ID of the car you want to update the miles on: ")
                #self.set_mileage = input("Enter updated mileage: ")

               

    def __repr__(self):
        return f"ID: {self._id}, Make: {self._make}, Model: {self._model}, Year: {self._year}, Mileage: {self._mileage}, Services: {self._services}"

    
    def add_a_car():
        make = input("Enter make of car:  ")
        model = input("Enter model of car: ")
        year = input("Enter year of car: ")
        mileage = input("Enter mileage of car: ")
        services = input("Enter services for car: ")
        CarManager(make, model, year, mileage, services)
        return CarManager.view_all_cars()
    
    def view_car_details(car_id):
        car = CarManager.all_cars.get(car_id)
        if car:
            print(car)
        else:
            print(f"No car found with ID {car_id}\n")

    @staticmethod
    def view_all_cars():
        for cars in CarManager.all_cars.values():
            print(cars)
