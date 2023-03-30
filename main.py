# Creating dictionaries

user_one = {
    'full_name':'Joaquin Humm',
    'user_name':'q',
    'password':'q',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 500),
        ('Chase',2000),
        ('PNC', 2500)
    ]
}

user_two = {
    'full_name':'Orlando Humm',
    'user_name':'o',
    'password':'o',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 500),
        ('Chase',2000),
        ('PNC', 2500)
    ]
}
# Checking user_one credentials

# User credential Function
def credential_check (user_one):
    inputting_user_name  = True
    while inputting_user_name == True:
        user_one_credentials = input('Please enter your user name:  ')
        if user_one_credentials == user_one['user_name']:
            inputting_user_name = False
            inputting_password = True
            while inputting_password == True:
                user_one_password = input("Please enter your password:  ")
                if user_one_password == user_one['password']:
                    inputting_password = False
                    print(" ")
                    print(f"Log in successful!  Welcome {user_one['full_name']}")
                else:
                    print("Incorrect password, please try again.")
        else:
            print("Incorrect username, please try again.")

# Displaying Account Information Function

def account_info(user_one):
    print(" ")
    print("Displaying current account information...")
    print(f"Your current available balance is: ${user_one['account_balance']}")
    print(" ")
    print("Your available funds from connected banks are as follows:\n")
    for funds in user_one['connected_banks']:
        print(f"{funds[0]}: ${funds[1]}")
        print(" ")

# Transaction Function

def transaction(user_one,user_two):
    transfer_funds = input(f"Are you sure that you want to transfer money to {user_two['full_name']}? (y/n): ").lower()
    transfer_confirmed = True
    while transfer_confirmed == True:
        if transfer_funds == 'n':
            print("Transaction cancelled.  Have a nice day!")
            transfer_confirmed = False
        else:
            funds_available = False
            transfer_amount = int(input(f"\nHow much money would you like to transfer to {user_two['full_name']}? (Whole dollars only): "))
            while funds_available == False:
                if transfer_amount > user_one['account_balance']:
                    print(f"Insufficient Funds.  Your transfer must be less than or equal to {user_one['account_balance']}.  Please enter a smaller amount to transfer.")
                    transfer_amount = int(input(f"How much money would you like to transfer to {user_two['account_balance']}? (Whole dollars only): "))
                else: 
                    funds_available = True

        print(f"\nInitiating transfer of {transfer_amount} to \"{user_two['full_name']}\".\n")
        user_one['account_balance']-=transfer_amount
        user_two['account_balance']+=transfer_amount
        print(f"Transaction successful!  You now have ${user_one['account_balance']} remaining.")
        
        additional_transaction=input("Would you like to make an additional transfer? (y/n): ").lower()
        if additional_transaction == 'n':
            print(f"\nYou now have {user_one['account_balance']} left in your account.  Have a GREAT day!")
            transfer_confirmed = False
      
# Calling Functions
credential_check(user_one)
account_info(user_one)
transaction(user_one,user_two)

