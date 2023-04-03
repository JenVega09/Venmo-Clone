# Venmo Clone Project with Bonus Stories # 1 & 4

# Creating dictionaries

user_one = {
    'full_name':'Joaquin Humm',
    'user_name':'qhumm',
    'password':'Qcumber',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 2500),
        ('Chase',2000),
        ('PNC', 1500)
    ]
}

user_two = {
    'full_name':'Orlando Humm',
    'user_name':'ohumm',
    'password':'Juice',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 2500),
        ('Chase',2000),
        ('PNC', 1500)
    ]
}

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

    print("\nDisplaying current account information...")
    print(f"Your current available balance is: ${payor['account_balance']}\n")
    print("Your available funds from connected banks are as follows:")
    for funds in payor['connected_banks']:
        print(f"{funds[0]}: ${funds[1]}")

def confirming_transaction (recipient):
    user_input = input(f"\nAre you sure that you want to transfer mney to {recipient['full_name']}? y/n: ").lower()
    if user_input == 'y':
        return True
    else:
        return False

def get_transfer_amount (recipient):
    money_to_transfer = int(input(f"\nHow much money would you like to transfer to {recipient['full_name']}? (Whole dollars only): "))
    return money_to_transfer

def check_fund_availability (money_to_transfer, payor):
    if money_to_transfer > payor ['account_balance'] or payor ['account_balance'] <= 0:
        return False
    else: 
        return True

def perform_transfer (money_to_transfer, payor, recipient):
    payor['account_balance'] -= money_to_transfer
    recipient['account_balance'] += money_to_transfer
    print (f"\nTransaction successful!!  You now have {payor['account_balance']} left in your account")

def additional_transfer_check (recipient):
    user_input = input(f"\nWould you like to make another transfer to {recipient['full_name']}? y/n: ").lower()
    if user_input == 'y':
        return True
    else:
        return False

def end_message (payor):
    print (f"End of transaction.  You now have ${payor['account_balance']} remaining in your account.  Have a GREAT day!")

# Setting Payor/Recipient

payor = input(f"Who would like to do the transfer today, a: {user_one['full_name']}, or b: {user_two['full_name']}? a/b: ").lower()
if payor == 'a':
    payor = user_one
    recipient = user_two
else:
    payor = user_two
    recipient = user_one

user_name_check (payor)
password_check (payor)
display_account_info (payor)

performing_transactions = confirming_transaction (recipient)
while performing_transactions == True: 
        money_to_transfer = get_transfer_amount (recipient)
        funds_available = check_fund_availability (money_to_transfer, payor)
        if funds_available == True:
            perform_transfer (money_to_transfer,payor, recipient)    
            performing_transactions = additional_transfer_check (recipient)
        elif payor['account_balance'] <= 0:
            print ("I'm sorry, you have no more money left in your account.")
            performing_transactions = False
            break
        else:
            print (f"Insufficient Funds.  You must enter amount less than or equal to {payor['account_balance']}.  ")
else:
    end_message (payor)
