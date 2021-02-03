# import sqlite3
# con = sqlite3.connect("Afia na airtime.db")
# #create a cursor
# c = con.cursor()
# #create table()
# c.execute("""CREATE TABLE details (
#        HUDUMA_NUMBER text,
#        PACKAGE text,
#        PREMIUM text
#        )""")
# #commit changes
# con.commit()
# #close connections
# con.close()

import os
from twilio.rest import Client
def premiumComp():
    global premium
    global balance
    premium= 0.02 * recharge_amount
    balance =   recharge_amount - premium

def premiumNormal():
    global premium
    global balance

    premium= 0.01 * recharge_amount
    balance =  recharge_amount - premium
def send_sms():
    account_sid = 'ACa6dd7cbe7750000191dfcd6ae332ed66'
    auth_token = '4e88eaead51aae9af9716980db6f8c74'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        to = '+254729960053',
                        from_='+13157435889',
                        body='Recharge successful. Airtime balance is Ksh.{}, Ksh.{} has been deducted to pay your afia na airtime'.format(balance, premium), 
                    )

print("________________WELCOME TO AFYA NA AIRTIME________________\n")
choice = input("     Do you want to opt for afia na airtime? (y/n): ")
if choice == "y" or choice == "Y":
  print("     Print please select what you want to opt for")  
  print("      1. Do you want to opt for normal coverage?")
  print("      2. Do you want to opt for comprehensive?")
  option = int(input("    Please choose your Option: "))
  if option == 1:
    recharge_amount =int(input("      Enter the amount to recharge: "))

    premiumNormal()
    send_sms()
  elif option == 2:
    f_name = input("      Enter your first name: ")
    s_name = input("      Enter the second name: ")
    user_id = input("     Enter national id :")
    recharge_amount = int(input("      Enter the amount to recharge: "))
    premiumComp()
    send_sms()
    
  else:
    print("Invalid inputs")

elif choice == "n" or choice == "N":
  print("Welcome some other time")
else:
  print("Invalid input")
