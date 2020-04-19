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