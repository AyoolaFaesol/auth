
database = {

}
import random


def init():

    print('welcome to our bank')
        
    account = int(input('are you a customer in our bank: 1. (YES) 2. (NO) \n'))
    if(account == 1):   
        login()
        
    elif(account == 2):       
        register()
        
    else:
        print('invalid option selected')
        init()

def login():
    print('this is the login section')
        
    useraccount = int(input('what is your account number \n'))
    password = input('enter your password \n')
    for accountnumber, userdetails in database.items():
        if(accountnumber == useraccount and userdetails[3] == password):
            operations()
            
        else:
            print('invalid login details')
            login()

        
                
        
        
        
def operations():
    print('WELCOME, what transactions are you performing today')
    optionselected = int(input('please select from these options (1). currentbalance (2). withdrawal (3). deposit (4). complaints (5).logout \n '))
    if (optionselected == 1):
       currentbalance()
        
    elif(optionselected == 2):
         withdrawal()
        
    elif(optionselected == 3):
        deposit()
        
    elif(optionselected == 4):
        complaints()
        
    elif(optionselected == 5):
        logout()
    else:
        print('invalid option selected, try again')
        operations()

        
def generateaccountnumber():
    return random.randrange(1111111111, 9999999999)


def register():
    print('---REGISTER HERE---')
    email = input('what is your email address \n')
    first_name = input('first name \n')
    last_name =  input('last name \n')
    password = input('enter a new  password \n')
    accountnumber = generateaccountnumber()

    database[accountnumber] = [first_name, last_name, email, password, 30000] #this database contains the customer's account number, names, email and current account balance saved upon registeration
    print(database)
    print('Account successfully created ')
    print('you will be directed to the login section')
    login()

def currentbalance():
    for accountnumber, userdetails in database.items():
        print('your current balance is %d' %userdetails[4])

def withdrawal():
    for accountnumber, userdetails in database.items():
        print('---WITHDRAW HERE---')
        print(userdetails[4])
        amt_with = int(input('how much would you like to withdrawv from your account \n'))
        if(amt_with < userdetails[4]):
            print('transaction in process....')
            print('you have successfully withdraw %d, take your cash' %amt_with)
        else:
            print('insufficient amount, try again')
            withdrawal()

def deposit():
    print('---MAKE YOUR DEPOSIT HERE---')
    depo = int(input('how much would you like to deposit? \n'))
    print('you deposited %d' %depo)
    for accountnumber, userdetails in database.items():
        new_bal = depo + userdetails[4]
        print('your balance is now %d' %new_bal)

def complaints():
    print('---COMPLAINTS SECTION---')
    input('drop your complaints below and we will give you a feedback as soon as possible \n')
    print('thank you, our customer sevice will see to your complaints')

def logout():
    print('Thank you for banking with us...')
    exit()



init()

