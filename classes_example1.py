class Employee:
    # When creating methods inside a class. They recieve the instance as the first arg automatically.
    # ...so we have placed self as it's a default vaule used.
    def __init__(self, fName, lName) -> None:
        self.fName = fName
        self.lName = lName
        self.email = fName + "." + lName + "." "@company.com"


# Create Objects from the class.
# If you don't assign values here you can do it later manually: See emp_3
emp_1 = Employee("Harry", "Potter")
emp_2 = Employee("Alice", "InWonderland")

# Assign values Manually to the class.variables for each object created
# emp_3.fName = "Harry"
# emp_3.lName = "Potter"

print(emp_1.fName, emp_1.lName)
print(emp_2.fName, emp_2.lName)
