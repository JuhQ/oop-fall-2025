class Employee:

    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def get_information(self):
        return f"Name: {self.name}, Department: {self.department}"

    def print_information(self):
        print("I AM NOW PRINTING in Employee class")
        print(self.get_information())

class HourlyEmployee(Employee):

    #def __init__(self, name, department, salary):
    #    super().__init__(name, department, salary)
    #    self.salary = salary

    def print_salary(self):
        print(f"Salary: {self.salary}")

    def get_information(self):
        return f"{super().get_information()}, Hourly salary: {self.salary}"

    def print_information(self):
        print("Printing from HourlyEmployee")
        print(self.get_information())
        #super().print_information()
        #self.print_salary()

class MonthlyEmployee(Employee):

    def __init__(self, cups_of_coffee, name, department, salary):
        self.name = "Something"
        super().__init__(name, department, salary)
        self.cups_of_coffee = cups_of_coffee

    def get_information(self):
        return (f"{super().get_information()}, Monthly salary: {self.salary}\n"
                f"Access to {self.cups_of_coffee} cups of coffee")

    def get_coffee(self):
        return True



employee1 = Employee("Juha", "ICT", 0)
employee1.print_information()
#employee1.print_salary()

employee2 = HourlyEmployee("Matti", "Coding", 100)
employee2.print_information()
#employee2.print_salary()

employee3 = MonthlyEmployee(300, "Pekka", "Coffee", 5000)
employee3.print_information()