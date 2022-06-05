s = input('')

def count_letters(s):
    up = len([i for i in s if i.isupper()])
    down = len([i for i in s if i.islower()])
    return up, down

print(count_letters(s))