class User:

    all_post = []

    def __init__(self, name, email, address, dlnum):
        self.name = name
        self.email = email
        self.address = address
        self.dlnum = dlnum
        self.user_posts = []

    def __str__(self):
        return f"{self.name} email is {self.email} located in {self.address} and their driver license # is: {self.dlnum}"
    
    def emailaddress(self):
        print(f"{self.name}'s email address is: {self.email}")

    def create_a_post(self):
        body = input("What's on your mind?\n\n")
        self.user_posts.append(body)
        User.all_post.append(body)

Bobby = User("Bobby", "bobby@gmail.com", "Houston, TX", "12345")
Mason = User("Mason", "mason@hotmail.com", "Somewhere In HOU, TX", "123456")
Josh = User("Josh", "josh@yahoo.com", "Elsewhere, US", "1234567")

Bobby.emailaddress()
print(Bobby.address)
print(Bobby)