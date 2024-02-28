import random
print('Welcome to the PyPassword Generator!\n')
no_of_letters = int(input("How many letters would you like in your password?\n"))
no_of_symbols = int(input("How many symbols would ypu like?\n"))
no_of_numbers = int(input("How many numbers would you like?\n"))
letters_list = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers_list = ['0','1','2','3','4','5','6','7','8','9']
symbols_list = ['!','@','#','$','%','^','&','*','(',')']
password = []
for i in range(0,no_of_letters+1):
    password.append(random.choice(letters_list))

for i in range(0,no_of_symbols):
    password.append(random.choice(symbols_list))

for i in range(0,no_of_numbers):
    password.append(random.choice(numbers_list))

random.shuffle(password)
password1 = ""
for i in password:
    password1 = password1+i

print(f"Here is your password: {password1}")