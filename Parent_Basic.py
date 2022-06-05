class User:
    def __init__(self):
        self.__name = None
        self.__accNo = 0
        self.__deposit = 0
        self.__type = None
        self.__statement = 0
        self.__apply = 0
        self.__spchr = 0
        self.__contact = 0

    def getcontact(self):
        return self.__contact

    def getspchr(self):
        return self.__spchr

    def getStatement(self):
        return self.__statement

    def getapply(self):
        return self.__apply

    def getacc_no(self):
        return self.__accNo

    def getName(self):
        return self.__name

    def getAccountType(self):
        return self.__type

    def getDeposit(self):
        return self.__deposit

    def setacc_no(self, __accNo):
        self.__accNo = __accNo

    def setName(self, __name):
        self.__name = __name

    def setAccountType(self, __type):
        self.__type = __type

    def setDeposit(self, __deposit):
        self.__deposit = __deposit

    def setStatement(self, __statement):
        self.__statement = __statement

    def setapply(self, __apply):
        self.__apply = __apply

    def setspchr(self, __spchr):
        self.__spchr = __spchr

    def setcontact(self, __contact):
        self.__contact = __contact

    def __str__(self):
        print("User Details:\n")
        return f'''[Account No: {self.__accNo}\nName: {self.__name}\nAccount Type: {self.__type}\nDeposit: {self.__deposit}
Pin: {self.__spchr}\nBalance: {self.__statement}\nContact: {self.__contact}]'''










