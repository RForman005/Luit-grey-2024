user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if user_age < 25 and user_country == 'Germany':
    print('You an apply for a German student exchange program')
else:
    print('Sorry, you do not qualify')

if user_country == 'Sweden' or user_country == 'Denmark' or user_country == 'Norway':
    print('You can apply for a Scandinavian student exchange program')
else:
    print('Sorry, you do not qualify')


user_country = input('Where do you come from?')
if not user_country == 'Germany':
    print('you are not German!')
else:
    print('you are German')

user_age = int(input('What is your age? '))
user_country = input('What is your country? ')

if not user_country == 'Germany' and user_age < 25 or \
user_country == 'Germany' and user_age < 23:
    print('You qualify!')
else:
    print('You don\'t qualify!')
