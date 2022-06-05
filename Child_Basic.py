from Parent_Basic import User

class database:
    user_database = []
    acc_no = 100

    def add_database(self):
        us = User()
        us.setacc_no(database.acc_no)
        us.setName(input('Enter Name: '))
        us.setAccountType(input('Enter account type: '))
        us.setDeposit(input('Enter amount to deposit: '))
        us.setspchr(int(input('Enter special 4 digit pin: ')))
        us.setStatement(float(input('Enter the balance amount: ')))
        us.setcontact(int(input('Enter your contact no: ')))
        database.user_database.append(us)
        database.acc_no += 1
        print('User entered into database successfully.')

    def showAllAccount(self):
        for us in database.user_database:
            print(us)

    def Open_New_account(self):
        account = set()
        num = int(input('1. Savings Account\n2. Current Account : '))
        for us in database.user_database:
            if num == 1:
                enter = int(input('Enter 4 digit pin: '))
                if len(str(enter)) == 4 or enter == us.getspchr():
                    print('Your balance amount is: ', us.getStatement())
                elif len(str(enter)) != 4 or enter != us.getspchr():
                    print('User not found. Please enter valid pin.')
            elif num == 2:
                name = input('Enter your full name: ')
                contact = int(input('Enter contact number: '))
                if name == us.getName() or contact == us.getcontact():
                    print('User already exist')
                else:
                    database.user_database.append(name)
                    database.user_database.append(contact)
                    # name = database.user_database.append(us.setName)
                    # contact = database.user_database.append(us.setcontact)
                    account.add(tuple(database.user_database))
                    # account.add(us)
                    print('User information stored', account)
                    return
                    # return us.getName or us.getcontact
            else:
                print('Enter value between 1 and 2 only')

    def deposit(self):
        acc_no = int(input('Enter account number: '))
        for us in database.user_database:
            if acc_no == database.acc_no:
                amount = float(input('Enter the amount you want to deposit: '))
                us.setStatement = us.getStatement() + amount
                print("Account balance has been updated : ₹", us.setStatement)
            else:
                print("Account does not exist...")

    def updateAccount(self):
        acc_no = int(input("Enter Account Number : "))
        for us in database.user_database:
            if acc_no == database.acc_no:
                self.__name = input("Modify Account Holder Name :")
                self.__contact = input("Modify contact information :")
                print('Information updated successfully.')

    def withdraw(self):
        acc_no = int(input('Enter Account Number : '))
        for us in database.user_database:
            if acc_no == database.acc_no:
                amount = float(input('Enter the amount you want to withdraw: '))
                if us.getStatement() > amount:
                    us.setStatement = us.getStatement() - amount
                    print("Account balance has been updated : ₹", us.setStatement)
                else:
                    print("Insufficient balance :_)")
            else:
                print("User does not exist...")

    def enquiry(self):
        num1 = int(input('Enter 4 digit pin: '))
        phn = int(input('Enter your contact no: '))
        for us in database.user_database:
            return us if len(str(num1)) == 4 and num1 == us.getspchr() and phn == us.getcontact() else print("User does not exist...")



obj = database()
'''obj.add_database()
obj.Open_New_account()'''
obj.showAllAccount()














