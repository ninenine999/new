import random
import string

'''登录信息'''


def loginnew():
    username = 'admin'
    password = 'admin'
    return [username, password]


'''帖子标题、帖子内容'''


def posting():
    title = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
    message = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(50))
    return [title, message]
