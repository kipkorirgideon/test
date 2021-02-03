import sqlite3
# @ Author KIPKORIR GIDEON MEDICAL ENGINEER  14th - 15th November 2020 Hackathon Allians Frankaisse Nyali
# con = sqlite3.connect("Afia na airtime.db") 
# #create a cursor
# c = con.cursor()
# #create table()
# c.execute("""CREATE TABLE details (
#        HUDUMA_NUMBER integer,
#        USERNAME text,
#        PACKAGE text,
#        PREMIUM integer
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
    account_sid = 'AC962e5cc292547f1528c9638670c2950a'
    auth_token = '2c31f9befaf6d7c07804a5dd0b0d3c4c'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        to = '+254745761314',
                        from_='+19378216696',
                        body='Recharge successful. Airtime balance is Ksh.{}, Ksh.{} has been deducted to pay your Afya na Airtime'.format(balance, premium), 
                    )
def send_congratsms():
    account_sid = 'AC962e5cc292547f1528c9638670c2950a'
    auth_token = '2c31f9befaf6d7c07804a5dd0b0d3c4c'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
                        to = '+254745761314',
                        from_='+19378216696',
                        body='Congratulations! Account successfully created current premium amount is Ksh.0', 
                    )
def runProg():
    global huduma
    global username
    try:
        huduma = int(input("       Enter your huduma number: "))
        username = input("       Enter username: ")
        checkUser()
        
    except ValueError:
        print("Sorry invalid huduma number")
def askpackage():
    global option
    print("      1. Do you want to opt for normal coverage?")
    print("      2. Do you want to opt for comprehensive?")
    option = int(input("     Please choose your package: "))
def run():
    global recharge_amount
    choice = input("     Do you want to opt for Afya na Airtime? (y/n): ")
    if choice == "y" or choice == "Y":
      print("      1. Do you want to opt for normal coverage?")
      print("      2. Do you want to opt for comprehensive?")
      option = int(input("     Please choose your package: "))
      if option == 1:
        try:
            huduma_number = int(input("     Enter your huduma number: "))
            recharge_amount = int(input("      Enter the amount to recharge: "))
            premiumNormal()
            send_sms()
        except ValueError:
            print("   Sorry! Invalid input")  
      elif option == 2:
        huduma_number = int(input("        Enter your huduma number: "))
        recharge_amount = int(input("      Enter the amount to recharge: "))
        premiumComp()
        send_sms()

      else:
        print("Invalid inputs")

    elif choice == "n" or choice == "N":
      print("   Welcome some other time\n")
    else:
      print("   Sorry! Invalid input\n")
def insertData():
    premium = 0
    con = sqlite3.connect("Afia na airtime.db")
    #create a cursor
    c = con.cursor()

    c.execute("INSERT INTO details VALUES (?,?,?,?)",[huduma,
                                                     username,
                                                     package,
                                                     premium
                                                     ])
    #commit changes
    con.commit()
    #close connections
    con.close()

def errorHandlingPackage():
    print("   \nPlease Opt for Afya na Airtime")
    print("      1. Do you want to opt for normal coverage?")
    print("      2. Do you want to opt for comprehensive?\n")
    try:
        option = int(input("   Please choose your package (1/2): "))
        if option == 1:
            package = "normal"
            insertData()
            send_congratsms()
        elif option == 2:
            package = "comprehensive"
            insertData()
            send_congratsms() 
    except ValueError:
        print("   Sorry! Invalid package input")  
def checkUser():
    global recharge_amount 
    global package

    con = sqlite3.connect("Afia na airtime.db")
    #create a cursor
    c = con.cursor()
    c.execute ("SELECT *,oid  FROM details")
    my_data = c.fetchall()

    user_data = [list(ele) for ele in my_data]

    #commit changes
    con.commit()
    #close connections
    con.close()
    if len(user_data) == 0:
        print("      1. Do you want to opt for normal coverage?")
        print("      2. Do you want to opt for comprehensive?")
        option = int(input("     Please choose your package (1/2): "))
        if option == 1:
            package = "normal"
            insertData()
            send_congratsms()
        elif option == 2:
            package = "comprehensive"
            insertData()
            send_congratsms()         
        else:
            print("Invalid input")

    else:
        hudumaNumber = str(huduma)
        con = sqlite3.connect("Afia na airtime.db")
        #create a cursor
        c = con.cursor()
        try:  
            c.execute("SELECT  USERNAME, HUDUMA_NUMBER FROM details WHERE HUDUMA_NUMBER = "+ hudumaNumber)
            def Convertion(tup,dicti):
                dicti = dict(tup)
                return dicti 
            tups =c.fetchall()
            dictionary = {}
            final_dictionary = Convertion(tups, dictionary) 
            if final_dictionary[username] == int(huduma):
                 print("You have already opted for Afya na Airtime")
                
            else:
                errorHandlingPackage()       
        except:
            errorHandlingPackage()
# runProg()