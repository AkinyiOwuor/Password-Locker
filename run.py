#!/usr/bin/env python3.6
from user import User

def create_user(username,email,accname,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,email,accname,password)
    return new_user

def save_users(user):
    '''
    Function to save user
    '''
    user.save_user()

def del_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def find_user(user_name):
    '''
    Function that finds a user by user_name and returns the user
    '''
    return User.find_by_user_name(user_name)

def check_existing_users(user_name):
    '''
    Function that check if a user exists with that user_name and return a Boolean
    '''
    return User.user_exist(user_name)

def display_users():
    '''
    Function that returns all the saved users
    '''
    return User.display_users()

def main():
    print("Hello Welcome to your password Locker account. What is your name?")
    user_name = input()

    print(f"Hello {user_name}. what would you like to do?")
    print('\n')

    while True:
        print("Use these short codes :su-Sign Up, da-Log in to your accout, fa-Find password locker account, ex-Exit Password Locker. ")
        short_code = input().lower()
        if short_code == 'su':
            print("Create a Password Locker Account")
            print("_"*10)
            user_name = input('User name:')
            print ('\n')
            email = input('Email Address:')
            print ('\n')
            account_name = input('Account Name : ')
            print ('\n')
            password = input('Password:')
            save_users(create_user(user_name,email,account_name,password)) 
            print ('\n')
            print(f"A new {account_name} account with the user name  {user_name} has been created.")
            print(f"You can now login to your {account_name} account using your password.")
            print ('\n')
        elif short_code == 'da':
             if display_users():
                 print("Here is your password locker account and your details")
                 print('\n')
                 for user in display_users():
                     print(f"User name:{user.user_name}  Account name: {user.account_name} Password:{user.password}")
                     print('\n')
             else:
                 print('\n')
                 print("You dont seem to have created an account yet.Sign up to create a new account.")
                 print('\n')
        
        elif short_code == 'fa':

                            print("Enter the password locker account you want to search for")

                            search_user_name = input()
                            if check_existing_users(search_user_name):
                                    search_user = find_user(search_user_name)
                                    print(f"{search_user.user_name} .......{search_user.email}")
                                    print('-' * 20)

                                    print(f"User name.......{search_user.user_name}")
                                    print(f"Account name.......{search_user.account_name}")
                                    print(f"Password.......{search_user.password}")
                            else:
                                    print("That password locker account does not exist")

        elif short_code == "ex":
                            print("Thanks for your time.Bye!.......")
                            
        else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
 main()





