#after first login
print('have you logged in before?')
login = input()
with open("userpassword.txt") as text_file:
        # read 1 line at a time
    for line in text_file:
        print(line)


#first login
username = input('Please enter a Username (case sensitive): ')
print("please enter a password for", username,"(case sensitive): ")
password = input()
print('is', password,'correct?(yes or no): ')
response = input()
while response == 'no':
    print("please enter a password for", username,"(case sensitive): ")
    password = input()
    print('is', password,'correct?(yes or no): ')
    response = input()
else:
    print('welcome in', username,'have a good stay!')
    
#file
CREDENTIALS_FILENAME = 'userpassword.txt'
credentials = (f'username is {username}\n'
              f'password for {username} is {password}')
with open(CREDENTIALS_FILENAME, 'w') as f:
    f.write(credentials)
print('wrote to txt file!')