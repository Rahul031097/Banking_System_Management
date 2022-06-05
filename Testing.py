from Project_for_interview.Basic import database

obj = database()
account = set()
user_id = 123456
password = 123456
while True:
    print('1.SignUp\n2.Login\n3.Office Login\n4.Exit')
    choice = int(input('Enter your choice: '))
    if choice==1:
        name = input('Enter your name: ')
        acc_no = int(input('Enter your account no: '))
        mob_no = int(input('Enter your mobile no: '))
        pin = int(input('Enter 4 digit password: '))
        pin1 = int(input('Re-enter your 4 digit password: '))
        if acc_no==database.acc_no:
            print('1.Open New Account\n2.Deposit Money\n3.Transfer Money\n4.Update Account Information\n5.Get account details')
            choice1 = int(input('Enter your choice: '))
            if choice1==1:
                obj.Open_New_account()
            elif choice1==2:
                obj.deposit()
            elif choice1==3:
                obj.withdraw()
            elif choice1==4:
                obj.updateAccount()
            elif choice1==5:
                obj.enquiry()
        elif acc_no!=database.acc_no:
            database.user_database.append(acc_no)
            database.user_database.append(acc_no)
            database.user_database.append(mob_no)
            database.user_database.append(pin)
            account.add(tuple(database.user_database))
            print('User information stored successfully\n', account)
    elif choice==2:
        print('1.Open New Account\n2.Deposit Money\n3.Transfer Money\n4.Update Account Information\n5.Get account details')
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








