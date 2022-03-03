import os
CREDENTIALS_FILENAME = 'credentials.txt'
content = ''
if os.path.isfile(CREDENTIALS_FILENAME):
    with open(CREDENTIALS_FILENAME, 'r') as f:
        content = f.read()

if content:
    logged_in_before = input('Have you logged in before?')
    if logged_in_before == 'yes':
        username1 = input('What user do you want to login as?')
        if username1 in content:
            print('please enter the password for ' , username1 , ': ')
            password1 = input()
            if password1 in content:
                print('welcome', username1 ,'have a good stay')
            while password1 not in content:
                print('incorrect,please try again')
                print('please enter the password for', username1, ': ')
                password1 = input()
    else:
        print('TODO implement first login process')
else:
    #first login (creation of credentials file)
    username = input('Please enter a Username (case sensitive): ')
    print("please enter a password for", username, "(case sensitive): ")
    password = input()
    print('is', password, 'correct?(yes or no): ')
    response = input()
    while response == 'no':
        print("please enter a password for", username, "(case sensitive): ")
        password = input()
        print('is', password, 'correct?(yes or no): ')
        response = input()
    else:
        print('welcome in', username, 'have a good stay!')

    # write a file
    with open(CREDENTIALS_FILENAME, 'w') as f:
        f.write((f'username is {username}\n'
                 f'password for {username} is {password}'))
    print('done to text file!')