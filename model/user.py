class User:
    id = 0
    email = ""
    password = ""
    first_name = ""
    last_name = ""
    phone = ""
    role = 1
    
    def __init__(email, password, first_name, last_name, phone):
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.phone = phone

