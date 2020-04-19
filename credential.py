class Credential:
    '''
    Class that generates new credentials
    '''
    Credential_list=[]

    def __init__(self,account_name,user_name,password,email):
        self.account_name=account_name
        self.user_name=user_name
        self.password=password
        self.email=email

    def save_credential(self):
        '''
        method that saves credential object into credential list
        '''
        Credential.Credential_list.append(self)
