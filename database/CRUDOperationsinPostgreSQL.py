# This Python class demonstartes how to connect to a PostgreSQL database and perform CRUD operations on it.
# Example is of Customer and accounts table, where customer can have multiple accounts.

import psycopg2 as  dblib

class CustomerDataRepository:
    def __init__(self):
        self.connection = dblib.connect(user="postgres",
                                        password="mysecretpassword",
                                        host="127.0.0.1",
                                        port="5432",
                                        database="postgres")
        self.cursor = self.connection.cursor()

    def createCustomerTable(self):
        createTableQuery = '''CREATE TABLE IF NOT EXISTS customer
        (id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        email VARCHAR(255) NOT NULL,
        phone VARCHAR(255) NOT NULL);'''
        self.cursor.execute(createTableQuery)
        self.connection.commit()

    def createAccountsTable(self):
        createTableQuery = '''CREATE TABLE IF NOT EXISTS accounts
        (id SERIAL PRIMARY KEY,
        accountNumber VARCHAR(255) NOT NULL,
        accountType VARCHAR(255) NOT NULL,
        customerId INTEGER NOT NULL,
        FOREIGN KEY (customerId) REFERENCES customer(id));'''
        self.cursor.execute(createTableQuery)
        self.connection.commit()

    def insertCustomer(self, name, email, phone):
        insertQuery = '''INSERT INTO customer(name, email, phone) VALUES (%s, %s, %s);'''
        self.cursor.execute(insertQuery, (name, email, phone))
        self.connection.commit()

    def insertAccount(self, accountNumber, accountType, customerId):
        insertQuery = '''INSERT INTO accounts(accountNumber, accountType, customerId) VALUES (%s, %s, %s);'''
        self.cursor.execute(insertQuery, (accountNumber, accountType, customerId))
        self.connection.commit()

    def getCustomer(self, id):
        selectQuery = '''SELECT * FROM customer WHERE id = %s;'''
        self.cursor.execute(selectQuery, (id,))
        return self.cursor.fetchone()
    
    def getAccount(self, id):
        selectQuery = '''SELECT * FROM accounts WHERE id = %s;'''
        self.cursor.execute(selectQuery, (id,))
        return self.cursor.fetchone()
    
    def updateCustomer(self, id, name, email, phone):
        updateQuery = '''UPDATE customer SET name = %s, email = %s, phone = %s WHERE id = %s;'''
        self.cursor.execute(updateQuery, (name, email, phone, id))
        self.connection.commit()

    def updateAccount(self, id, accountNumber, accountType, customerId):
        updateQuery = '''UPDATE accounts SET accountNumber = %s, accountType = %s, customerId = %s WHERE id = %s;'''
        self.cursor.execute(updateQuery, (accountNumber, accountType, customerId, id))
        self.connection.commit()
    
    def deleteCustomer(self, id):
        deleteQuery = '''DELETE FROM customer WHERE id = %s;'''
        self.cursor.execute(deleteQuery, (id,))
        self.connection.commit()

    def deleteAccount(self, id):
        deleteQuery = '''DELETE FROM accounts WHERE id = %s;'''
        self.cursor.execute(deleteQuery, (id,))
        self.connection.commit()

if __name__ == "__main__":
    crud = CRUDOperationsinPostgreSQL()
    crud.createCustomerTable()
    crud.createAccountsTable()
    
    crud.insertCustomer('John', 'pythonuser@pythonedu.in', '1234567890')
    crud.insertCustomer('Jane', 'pythondev@pythonedu.in','987654321')

    crud.insertAccount('1234567890', 'Savings', 1)
    crud.insertAccount('987654321', 'Current', 2)

    print(crud.getCustomer(1))
    print(crud.getAccount(1))

    crud.updateCustomer(1, 'John Doe', 'pythonuser@pythonedu.in', '1234567890')
    print(crud.getCustomer(1))