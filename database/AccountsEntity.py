class Accounts:
    def __init__(self, account_id, account_name, account_type, account_balance):
        self.account_id = account_id
        self.account_name = account_name
        self.account_type = account_type
        self.account_balance = account_balance

    def displayAccount(self):
        print(f"Account ID: {self.account_id}, Account Name: {self.account_name}, Account Type: {self.account_type}, 
              Account Balance: {self.account_balance}, Customer: {self.customer.name} if self.customer else unassigned Account")

    @property
    def customer(self, customer):
        self.customer = customer

    @customer.setter
    def assignCustomer(self, customer):
        self.customer = customer

    def generateUnAssignedAccounts(self, numberOfAccounts):
        accounts = []
        for i in range(numberOfAccounts):
            accounts.append(Accounts(i, f"Account {i}", "Savings", 0))
        return accounts