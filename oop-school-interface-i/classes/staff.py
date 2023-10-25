import csv
from classes.person import Person
class Staff(Person):
    def __init__(self, name, age, role, employee_id, password):
        super().__init__(name, age, role, password)
        # self.name = name 
        # self.age = age         
        # self.password = password
        # self.role = role
        self.employee_id = employee_id

    @classmethod
    def all_staff(cls):
        staff = []
        with open('./data/staff.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                new_staff = cls(**row)
                #**kwargs arg simplifies process of assigning every key value does this under the hood: role="student") for dictionary we created from csv file ***destructured someone here, study more
                staff.append(new_staff)
        #print(staff)
        return staff
        

Staff.all_staff()