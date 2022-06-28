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
        print(us)

    def showAllAccount(self):
        for us in database.user_database:
            print(us)

    def Open_New_account(self, acc_no=100):
        num = int(input('1. Savings Account\n2. Current Account : '))
        type = str
        if num == 1:
            type = 'Savings'
        elif num == 2:
            type = 'Current'
        for us in database.user_database:
            if num == 1:
                enter = int(input('Enter 4 digit pin: '))
                if len(str(enter)) == 4:
                    if enter == us.getspchr():
                        print('Your balance amount is: ', us.getStatement())
                    database.acc_no = database.acc_no
                if len(str(enter)) != 4:
                    print('Enter 4 digit pin only. ')
                elif enter != us.getspchr():
                    print('User not found. Please enter valid pin.')
            elif num == 2:
                name = input('Enter your full name: ')
                contact = int(input('Enter contact number: '))
                if name == us.getName():
                    print('User already exist')
                elif contact == us.getcontact():
                    print('User already exist')
                else:
                    acc_type = print('Account type selected: ', type)
                    pin = int(input('Enter 4 digit pin for account: '))
                    if len(str(pin)) != 4:
                        print('Enter 4 digit pin only.')
                    else:
                        deposit = int(input('Enter minimum amount to be deposited into account\n(should be more than ₹10000): '))
                        database.acc_no += 1
                        us.setName(name)
                        us.setcontact(contact)
                        us.setAccountType(acc_type)
                        us.setspchr(pin)
                        us.setDeposit(deposit)
                        us.setStatement(deposit)
                        us.setacc_no(database.acc_no)
                        database.user_database.append(us)
                        #acc_no += 1
                        #print('Account No: ', acc_no)
                        balance = 0
                        if (deposit >= 10000):
                            print('Amount deposited into your account = ₹', deposit)
                            balance = print('Your balance amount : ₹', deposit)
                            print('User information stored')
                            print(us)
                            break
                        elif (deposit < 10000):
                            print('Enter value more than ₹10000 only')
                            break
                            #balance = print('Your balance amount :', deposit)
                        '''else:
                            #elif name != us.getName() or contact != us.getcontact():
                            us.setName(name)
                            us.setcontact(contact)
                            us.setAccountType(acc_type)
                            us.setDeposit(deposit)
                            us.setStatement(deposit)
                            database.user_database.append(us)
                            acc_no += 1
                            database.user_database.append(name)
                            database.user_database.append(contact)
                            database.user_database.append(type)
                            database.user_database.append(deposit)
                            database.user_database.append(balance)'''
                            # name = database.user_database.append(us.setName)
                            # contact = database.user_database.append(us.setcontact)
                            #account.add(tuple(database.user_database))
                            # account.add
                            #print('User information stored') # database.user_database.append(us))
                            #print('User information stored', account)
                            #return
                        # return us.getName or us.getcontact
            else:
                print('Enter value between 1 and 2 only')

    def deposit(self):
        acc_no = int(input('Enter account number to deposit in : '))
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
                name = input('Modify Account Holder Name: ')
                contact = int(input('Modify contact information: '))
                us.setName(name)
                us.setcontact(contact)
                print('Information updated successfully.')
                print(us)
                break
            else:
                print('Account number not found in database.')

    def withdraw(self):
        acc_no = int(input('Enter Account Number : '))
        for us in database.user_database:
            if acc_no == database.acc_no:
                amount = float(input('Enter the amount you want to withdraw: '))
                if us.getStatement(acc_no) > amount:
                    for acc_no in database.user_database:
                        balance = database.user_database.count(us.getStatement())
                        us.setStatement = balance - amount
                        print("Account balance has been updated : ₹", us.setStatement)
                        break
                else:
                    print("Insufficient balance :_)")
            else:
                print("User does not exist...")

    def enquiry(self):
        acc_no = int(input('Enter account number for information: '))
        num1 = int(input('Enter 4 digit pin: '))
        phn = int(input('Enter your contact no: '))
        for us in database.user_database:
            if acc_no == database.acc_no:
                continue
            if len(str(num1)) == 4:
                continue
            elif num1 == us.getspchr(acc_no):
                continue
            elif phn == us.getcontact(acc_no):
                print(us)
            else:
                print("User does not exist...")

    def SignUp(self):
        name = input('Enter your name: ')
        acc_no = int(input('Enter your account no: '))
        mob_no = int(input('Enter your mobile no: '))
        for us in database.user_database:
            if mob_no == database.user_database.__getitem__(us()):
                print('User already registered. Please login instead')
                break
            else:
                type = input('Enter type of account to open (Savings / Current): ')
                amount_min = int(input('Enter minimum amount to be deposited in account\n(should be ₹1000 minimum): '))
                if (amount_min >= 1000):
                    print('Amount deposited into your account = ₹', amount_min)
                else:
                    print('Enter value more than ₹1000 only')
                    continue
                balance = print("Amount in your balance: ", amount_min)
                pin = int(input('Enter 4 digit password: '))
                pin1 = int(input('Re-enter your 4 digit password: '))
                us.setacc_no(acc_no)
                us.setName(name)
                us.setcontact(mob_no)
                us.setAccountType(type)
                us.setDeposit(amount_min)
                us.setStatement(balance)
                us.setspchr(pin)
                database.user_database.append(us)
                acc_no += 1
                print(us)
                print('User information stored successfully\n')
                break



obj = database()
obj.add_database()
#obj.add_database()
#obj.Open_New_account()
#obj.deposit()
#obj.showAllAccount()
#obj.updateAccount()
#obj.enquiry()
#obj.withdraw()
obj.SignUp()












