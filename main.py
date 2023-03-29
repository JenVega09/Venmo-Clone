# Creating dictionaries

user_one = {
    'full_name':'Joaquin Humm',
    'user_name':'q',
    'password':'Q',
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

# Formatting beginning of Venmo transactions
print(" ")
print("Displaying current account information...")
print(f"Your current available balance is: ${user_one['account_balance']}")