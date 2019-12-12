user,passwd = 'alex','abc123'
def auth(func):
    def wrapper(*args, **kwargs):
        username = input("Username:").strip()
        password = input("Password:").strip()
        if username
        print("\033[32;1mUser has passed authentication\033[0m")
        func(*args, **kwargs)