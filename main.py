import random, string, requests, os

os.system('cls' or 'clear')

letters = int(input('How many letters: '))
num = int(input('How many usernames: '))

print("""[1] Digit [2] Letter [3] Combined""")

option = int(input('Choose: '))
def checkOption(option):
    if option == 1: username = ('').join(random.choices(string.digits, k=letters))
    if option == 2: username = ('').join(random.choices(string.ascii_lowercase, k=letters))
    if option == 3: username = ('').join(random.choices(string.ascii_lowercase + string.digits, k=letters))
    return username

working = 0
def run():
    try:
        username = checkOption(option)
        r = requests.get('https://api.github.com/users/' + username)
    except Exception as error:
        print(error)
    if r.status_code == 200:
        print('[-] ' + username)
    else:
        global working
        working+=1
        print('[+] ' + username)

for i in range(int(num)):
    run()