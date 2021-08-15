
class Employee:
    no_of_leaves = 8

    def __init__(self, aname, asalary, arole):
        self.name = aname
        self.salary = asalary
        self.role = arole

    def printdetails(self):
        return f"The Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def changeleaves(cls,newleaves):
        cls.no_of_leaves=newleaves


harry = Employee("Harry", 255, "Instructor")
rohan = Employee("Rohan", 455, "student")

print(harry.no_of_leaves)
rohan.changeleaves(34)
print(harry.no_of_leaves)

