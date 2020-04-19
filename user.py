import pyperclip
class User:
    '''
    Class that generates new instances of users.
    '''
    user_list=[]# Empty user list

    def __init__(self,user_name,email,account_name,password):

       self.user_name=user_name
       self.email=email
       self.phone_number=account_name
       self.password=password

    user_list=[] # Empty user list