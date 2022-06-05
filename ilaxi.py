s = input('')

def count_letters(s):
    upper = len([i for i in s if i.isupper()])
    downer = len([i for i in s if i.islower()])
    return upper, downer

print(count_letters(s))