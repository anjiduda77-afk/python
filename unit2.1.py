class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is starting.")
        else:
            print(f"{self.year} {self.make} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} is stopping.")
        else:
            print(f"{self.year} {self.make} {self.model} is already stopped.")


# -------- Main Program --------
make = input("Enter car make: ")
model = input("Enter car model: ")
year = input("Enter car year: ")

# Create car object
my_car = Car(make, model, year)

print("\n--- Car Actions ---")
my_car.start()
my_car.start()  # try starting again
my_car.stop()
my_car.stop()   # try stopping again
