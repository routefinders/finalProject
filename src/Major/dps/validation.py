from models import *

def UserExists(username):
    try :
        _ = Users.objects.get(username=username)
        return True
    except Users.DoesNotExist:
        return False

def EmailExists(email):
    try :
        _ = Users.objects.get(email=email)
        return True
    except Users.DoesNotExist:
        return False


def Validate(username, password):
    try:
        user = Users.objects.get(username = username, password = password)
        
        return user
    except Users.DoesNotExist:
        return False
