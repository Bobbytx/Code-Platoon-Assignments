class Student:

    def __init__(self, name, education, email, legs, id):
        self.name = name
        self.education = education
        self._email = email
        self._legs = legs
        self._id = id
        #underscore creates 'getters' to make attributes private

    #now give it a couple of methods

    #creates getter for email
    @property
    def email(self):
        return self._email
    
    #creates setter for email
    @email.setter
    def set_email(self, new_email):
        if type(new_email) == str and "@school.org" in new_email:
            self.email = new_email

     #creates getter for legs, did not create setter for legs
    @property
    def legs(self):
        return self._legs
   
    #creates getter for id
    @property
    def id(self):
        return self._id

    #creates setter for id
    @id.setter
    def set_id(self, new_id):
        if len(new_id) == 8 and not new_id[0].isnumeric():
            self._id = new_id
    
    #creates a method for student to call
    def go_to_school(self):
        print(f"{self.name} going to school!")
    
    def __str__(self):
        return f"{self.name} | {self.education} | {self.email} | {self.email}"

#creates student object
Student_one = Student("Mike", "High School", "mike@school.org", 3, "m2345678")

print(Student_one)
#change student id
Student_one.set_id = "m43fosi8"
print(Student_one.id)
    