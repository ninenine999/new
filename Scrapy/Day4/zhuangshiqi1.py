user='guanxinyue'
pwd='123123'
def auth(auth_type):
    def outer_wrappe(func):
        print('auth_func',auth_type)
        def wrapper(*args, **kwargs):
            username = input('usename:').strip()
            password = input('pwd:').strip()
            if username == user and password == pwd:
                print('skdfla s wi la fldsf ')
                res = func(*args, **kwargs)
                return res
            else:
                exit('sdkd fl ld fwk la ')

        return wrapper
    return outer_wrappe


def index():
    print('welcome to index page')
@auth(auth_type='local')
def Home():
    print('welcome to home page')
    return 'form home'
@auth
def bbs():
    print('welcome to bbs page')

index()
print(Home())
bbs()