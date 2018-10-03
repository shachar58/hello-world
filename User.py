class User(object):
<<<<<<< HEAD
    def __init__(self,userName,password):
        self.userName = userName
=======
    def __init__(self,user_name,password):
        self.userName = user_name
>>>>>>> shachar_change
        self.password = password
        self.isLogon = False

    def __str__(self):
<<<<<<< HEAD
        return f"{self.userName} login: {self.isLogon}"
=======
        return f"{self.user_name} login: {self.isLogon}"
>>>>>>> shachar_change
