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
    'password':'O',
    'account_balance': 5000,
    'connected_banks':[
        ('USAA', 500),
        ('Chase',2000),
        ('PNC', 2500)
    ]
}
# Checking user_one credentials

i = True
while i == True:
    user_one_credentials = input('Please enter your user name:  ')
    if user_one_credentials == user_one['user_name']:
        i=False
        j = True
        while j == True:
            user_one_password = input("Please enter your password:  ")
            if user_one_password == user_one['password']:
                j = False
                print(" ")
                print(f"Log in successful!  Welcome {user_one['full_name']}")
            else:
                print("Incorrect password, please try again.")
    else:
        print("Incorrect username, please try again.")

# Displaying Account Information

print(" ")
print("Displaying current account information...")
print(f"Your current available balance is: ${user_one['account_balance']}")
print(" ")
print("Your available funds from connected banks are as follows:")
for funds in user_one['connected_banks']:
    print(f"{funds[0]}: ${funds[1]}")
print(" ")

# Beginning transaction

transfer_funds = input(f"Are you sure that you want to transfer money to {user_two['full_name']}? (y/n): ").lower()
if transfer_funds == 'n':
    print("Transaction cancelled.  Have a nice day!")
else:
    k = False
    transfer_amount = int(input(f"How much money would you like to transfer to {user_two['full_name']}? (Whole dollars only): "))
    while k == False:
        if transfer_amount > user_one['account_balance']:
            print(f"Insufficient Funds.  Your transfer must be less than or equal to {user_one['account_balance']}.  Please enter a smaller amount to transfer.")
            transfer_amount = int(input(f"How much money would you like to transfer to {user_two['account_balance']}? (Whole dollars only): "))
        else: 
            k = True

    print(f"Initiating transfer of {transfer_amount} to {user_two['full_name']}.")
    print(" ")
    user_one['account_balance']-=transfer_amount
    user_two['account_balance']+=transfer_amount
    print(user_one['account_balance'])
    print(user_two['account_balance'])
    
    # print(f"Transaction successful, you now have ${user_one['account_balance']} remaining in your account.")
       

