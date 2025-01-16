class Customer:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def displayCustomer(self):
        print(f"Name: {self.name}, Email: {self.email}, Phone: {self.phone}")

    @property
    def account_id(self):
        return self.account_id
    
    @account_id.setter
    def withAccountIds(self, *account_id):
        self.account_id = account_id

    @property
    def name(self):
        return self.name
    
    @name.setter
    def withName(self, name):
        self.name = name

    @property
    def email(self):
        return self.email
    
    @email.setter
    def withEmail(self, email):
        self.email = email
    
    @property
    def phone(self):
        return self.phone
    
    @phone.setter
    def withPhone(self, phone):
        self.phone = phone