import pyperclip
class User:
    '''
    Class that generates new instances of users.
    '''
    user_list=[]# Empty user list

    def __init__(self,user_name,email,account_name,password):

       self.user_name=user_name
       self.email=email
       self.account_name=account_name
       self.password=password

    user_list=[] # Empty user list

    def save_user(self):
        '''
        save_user method saves user objects into user_list
        '''
        User.user_list.append(self)

    def delete_user(self):

        '''
        delete_user method deletes a saved user from the user_list
        '''
        User.user_list.remove(self)

    @classmethod
    def find_by_user_name(cls,user_name):
        '''
        Method that takes in a user_name and returns a user that matches that user_name.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user

    @classmethod
    def user_exist(cls,user_name):
        '''
        Method that checks if a user exists from the user list.
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                    return True

        return False

    @classmethod
    def display_users(cls):
        '''
        method that returns the user list
        '''
        return cls.user_list

    @classmethod
    def copy_password(cls,password):
        '''
        method that copies the password
        '''
        user_found = User.find_by_user_name(password)
        pyperclip.copy(user_found.password)

        

