class Car(object):

    def __init__(self, make, model, year):

        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):

        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

    def  read_dometer(self):
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, message):
        self.odometer_reading = message

my_new_car = Car('audi', 'a4', 2016)
print (my_new_car.get_descriptive_name())

my_new_car.update_odometer(23)
my_new_car.read_dometer()