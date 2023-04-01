# Creating dictionaries

user_one = {
    'full_name':'Joaquin Humm',
    'user_name':'q',
    'password':'q',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 2500),
        ('Chase',2000),
        ('PNC', 1500)
    ]
}

user_two = {
    'full_name':'Orlando Humm',
    'user_name':'o',
    'password':'o',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 2500),
        ('Chase',2000),
        ('PNC', 1500)
    ]
}

# Setting Payor/Recipient

payor = input(f"Who would like to do the transfer today, a: {user_one['full_name']}, or b: {user_two['full_name']}? a/b: ").lower()
if payor == 'a':
    payor = user_one
    recipient = user_two
else:
    payor = user_two
    recipient = user_one

# Username validation Function

def user_name_check (payor):
    inputting_user_name = True
    while inputting_user_name == True:
        payor_user_name = input ('Please enter your username: ')
        if payor_user_name == payor['user_name']:
            inputting_user_name = False
        else:
            print ('\nIncorrect user name, please try again.')

# Password validation function

def password_check (payor):
    inputting_password = True
    while inputting_password == True:
        payor_password = input ('Please enter your password: ')
        if payor_password == payor['password']:
            inputting_password = False
            print(f"\nLog in successful!  Welcome {payor['full_name']}")
        else:
            print ("Incorrect password, please try again.")

# Displaying Account Information Function

def display_account_info(payor):

    print(" ")
    print("Displaying current account information...")
    print(f"Your current available balance is: ${payor['account_balance']}\n")
    print("Your available funds from connected banks are as follows:")
    for funds in payor['connected_banks']:
        print(f"{funds[0]}: ${funds[1]}")

# Transaction Function

def transaction(payor,recipient):
    transfer_funds = input(f"Are you sure that you want to transfer money to {recipient['full_name']}? (y/n): ").lower()
    if transfer_funds == 'n':
        print("Transaction cancelled.  Have a nice day!")
    else:
        funds_available = False
        transfer_amount = int(input(f"\nHow much money would you like to transfer to {recipient['full_name']}? (Whole dollars only): "))
        while funds_available == False:
            if transfer_amount > recipient['account_balance']:
                print(f"Insufficient Funds.  Your transfer must be less than or equal to {payor['account_balance']}.  Please enter a smaller amount to transfer.")
                transfer_amount = int(input(f"How much money would you like to transfer to {recipient['account_balance']}? (Whole dollars only): "))
            else: 
                funds_available = True

            print(f"\nInitiating transfer of {transfer_amount} to \"{recipient['full_name']}\".\n")
            payor['account_balance']-=transfer_amount
            recipient['account_balance']+=transfer_amount
            print(f"Transaction successful!  You now have ${payor['account_balance']} remaining.")
        
            additional_transaction=input("Would you like to make an additional transfer? (y/n): ").lower()
            if additional_transaction == 'n':
                print(f"\nYou now have {payor['account_balance']} left in your account.  Have a GREAT day!")
                transfer_confirmed = False
                
# Checking available balance function
# def balance_check (payor, transfer_amount)
# while
# Calling Functions
user_name_check (payor)
password_check (payor)
display_account_info (payor)
transaction (payor,recipient)
