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
                    print("Use these short codes : cu - create a password Locker account, du - display password locker accounts, fu -find password locker account, ex -exit the password locker account list ")

                    short_code = input().lower()

                    if short_code == 'cu':
                            print("New Account")
                            print("-"*10)

                            print ("User name ....")
                            user_name = input()

                            print("Email address...")
                            e_address = input()

                            print("Account name ...")
                            acc_name = input()

                            print("Password ...")
                            password = input()


                            save_users(create_user(user_name,e_address,acc_name,password)) # create and save new user.
                            print ('\n')
                            print(f"New User {user_name} {e_address} created")
                            print ('\n')

                    elif short_code == 'du':

                            if display_users():
                                    print("Here is a list of all your password Locker accounts and passwords")
                                    print('\n')

                                    for user in display_users():
                                            print(f"{user.user_name} {user.account_name} .....{user.password}")

                                    print('\n')
                            else:
                                    print('\n')
                                    print("You dont seem to have any password Locker account saved yet")
                                    print('\n')

                    elif short_code == 'fu':

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
                            print("Bye .......")
                            break
                    else:
                            print("I really didn't get that. Please use the short codes")
if __name__ == '__main__':
 main()





