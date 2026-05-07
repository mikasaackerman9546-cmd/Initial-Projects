class Circle: 
    def __init__(self, radius):
        self.radius= radius
    
    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius

c1 = Circle(21)
print(c1.area())
print(c1.perimeter())



class Employee:
    def __init__(self, role, dept, salary):
        self.role = role
        self.dept = dept
        self.salary = salary

    def showDetails(self):
        print("role =", self.role)
        print("dept =", self.dept)
        print("salary =", self.salary)

e1 = Employee("accountant", "Finance" ,"$ 1,00,000")
e1.showDetails()
