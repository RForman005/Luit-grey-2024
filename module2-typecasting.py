height_cm = input('Height converter: enter your height in cm: ')
float_height_cm = float(height_cm)
print('Your height in feet is:', float_height_cm / 30.48 )

height_cm = input('Height converter: enter your height in cm: ')
print('Your height in feet is:', float_height_cm / 30.48 )

int() # integer 
year_born = int(input('What year were you born?'))
print('In 2100, you will be', 2100 - year_born, 'years old, provided you live this long!')

str()
temp_c = input('Enter the temperature toda in Celsius degrees; ')
temp_f = float(temp_c) * 1.8 + 32
temp_statement = str(temp_c) + ' degrees Celsius equals ' + str(temp_f) + 'degrees Fahrenheit'
print(temp_statement)