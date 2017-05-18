#NAME:OCHIENG EVANS
#REGISTRATION NO.:16/K/2260/PS
#STUDENT NO.:216002413
#COMPUTER YEAR 1
import calendar #this is an inbuilt module that will enable us get the week day
name = input("Enter your name")#ser to input name
print('Hello',name,',welcome to our program')
date = int(input('Enter your date of birth:'))
month = int(input('Enter your month of birth:'))
year = int(input('Enter your year of birth:'))
get = calendar.weekday(year,month,date)#gets the corresponding day of the week
selection = {0:'Monday',1:'Tuesday',2:'Wednesday',3:'Thursday',4:'Friday',5:'Saturday',6:'Sunday'}
'''This is a dictionary with the key as a number and value as a weekday'''
print(name,',you were born on a',selection[get])#prints user name and birthday
