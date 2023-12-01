class Employee:

    def __init__(self, name, job_title, starting_year, salary):
        self.name = name
        self.title = job_title
        self.year = starting_year
        self.salary = salary


    def __str__(self):
        return(f"{self.name} has worked at the company since {self.year} as a {self.title} and currently has a salary of ${self.salary}.")

    def get_salary(self):
        return (f"${self.salary}")
    def get_name(self):
        return (f"{self.name}")



def compare_salary(employee1, employee2):

    if employee1.salary > employee2.salary:
        return (f"{employee1.name} earns more.")
    
    elif employee1.salary == employee2.salary:
        return (f"{employee1.name} and {employee2.name} earn the same salary.")
    
    elif employee2.salary > employee1.salary:
        return (f"{employee2.name} earns more.")
  
        

