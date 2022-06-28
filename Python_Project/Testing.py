from Parent_Basic import User
from Child_Basic import database
us = User()
obj = database()
# account = set()
user_id = 123456
password = 123456
#acc_no = 100
while True:
    print('1.SignUp\n2.Login\n3.Office Login\n4.Exit')
    choice = int(input('Enter your choice: '))
    if choice==1:
        name = input('Enter your name: ')
        acc_no = int(input('Enter your account no: '))
        mob_no = int(input('Enter your mobile no: '))
        '''if acc_no==obj.acc_no:
            print('Account already in database. Please login to your account.')'''
        if mob_no!=us.setcontact(database.user_database):
            #mob_no = int(input('Enter your mobile no: '))
            type = input('Enter type of account to open (Savings / Current): ')
            amount_min = int(input('Enter minimum amount to be deposited in account\n(should be ₹1000 minimum): '))
            if (amount_min >= 1000):
                print('Amount deposited into your account = ₹', amount_min)
            else:
                print('Enter value more than ₹1000 only')
            pin = int(input('Enter 4 digit password: '))
            pin1 = int(input('Re-enter your 4 digit password: '))
            us.setacc_no(acc_no)
            us.setName(name)
            us.setcontact(mob_no)
            us.setAccountType(type)
            us.setDeposit(amount_min)
            us.setStatement(amount_min)
            us.setspchr(pin)
            database.user_database.append(us)
            acc_no += 1
            print(us)
            print('User information stored successfully\n')
        elif mob_no == us.setcontact(database.user_database):
            print('Mobile number already registered in database. Please login instead')
    elif choice==2:
        acc_no = int(input('Enter Account number: '))
        if acc_no == obj.user_database:
            pin = int(input('Enter 4 digit pin: '))
            if pin == us.setspchr(database.user_database):
                print('1.Open Account or get Statement\n2.Deposit Money\n3.Withdraw Money\n4.Update Account Information\n5.Account Information\n6.Back')
                choice1 = int(input('Enter your choice: '))
                if choice1 == 1:
                    obj.Open_New_account()
                elif choice1 == 2:
                    obj.deposit()
                elif choice1 == 3:
                    obj.withdraw()
                elif choice1 == 4:
                    obj.updateAccount()
                elif choice1 == 5:
                    obj.enquiry()
                elif choice1 == 6:
                    continue
                else:
                    print('Please select from the numbers given only.')
    elif choice==3:
        user_id1 = int(input('Enter office id: '))
        password1 = int(input('Enter office password: '))
        if user_id1==user_id and password1==password:
            print('1.Add Database\n2.Show all Account')
            choice2 = int(input('Enter your choice: '))
            if choice2==1:
                obj.add_database()
            elif choice2==2:
                obj.showAllAccount()
            else:
                print('Please select choice between 1 and 2')
        else:
            print('Wrong office_id or password')
    elif choice==4:
        print('Thank you for using :)')
        break
    else:
        print('Please select from the numbers given only.')








