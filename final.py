import os
from twilio.rest import Client
from data import *
user = '+254745761314',

def premiumComp():
  global premium
  global balance
  global premiumPaid
  premiumPaid= 0.2 * recharge
  balance =   recharge - premiumPaid
# def premCalculation():


def premiumNormal():
  global premium
  global balance
  global premiumPaid

  premiumPaid= 0.1 * recharge
  balance =  recharge - premiumPaid
def send_sms():
  account_sid = 'AC962e5cc292547f1528c9638670c2950a'
  auth_token = '2c31f9befaf6d7c07804a5dd0b0d3c4c'
  client = Client(account_sid, auth_token)


  message = client.messages.create(
                      to = user,
                      from_='+19378216696',
                      body='Recharge successful. Airtime balance is Ksh.{}, Ksh.{} has been deducted to pay for your afya na airtime'.format(balance, premiumPaid), 
                  )
  print("\nThe balance is {} and the premiumPaid is {}".format(balance, premiumPaid))

def compreOne():
  con = sqlite3.connect("Afia na airtime.db")
  #create a cursor
  c = con.cursor()
  c.execute ("SELECT  PREMIUM,oid FROM details  WHERE  HUDUMA_NUMBER = "+ new_huduma)
  data = c.fetchall()
  premium = [list(ele) for ele in data]
  premValue = premium[0][0]
  newPrem = premiumPaid + premValue
  rowid = premium[0][-1]
  con.commit()
  #close connections
  con.close()

  con = sqlite3.connect("Afia na airtime.db")
  #create a cursor
  c = con.cursor()

  c.execute("UPDATE details SET PREMIUM = (?) WHERE  oid = (?)",[newPrem ,rowid])
  send_sms()
  #commit changes
  con.commit()
  #close connections
  con.close()
def normOne():
  con = sqlite3.connect("Afia na airtime.db")
  #create a cursor
  c = con.cursor()
  c.execute ("SELECT  PREMIUM,oid FROM details  WHERE  HUDUMA_NUMBER = "+ new_huduma)
  data = c.fetchall()
  premium = [list(ele) for ele in data]
  premValue = premium[0][0]
  newPrem = premValue + premiumPaid
  rowid = premium[0][-1]
  con.commit()
  #close connections
  con.close()

  con = sqlite3.connect("Afia na airtime.db")
  #create a cursor
  c = con.cursor()

  c.execute("UPDATE details SET PREMIUM = (?) WHERE  oid = (?)",[ newPrem  ,rowid])
  send_sms()
  #commit changes
  con.commit()
  #close connections
  con.close()

def recharge():
  global recharge
  global new_huduma
  if user:
    try:
      premium = 0
      huduma = str(88)
      recharge = int(input("\n  Enter the amount to recharge: "))
      huduma = input("  Enter your huduma number: ")

      balance = recharge + premium
      try:
        huduma = int(huduma)
        new_huduma = str(huduma)

        con = sqlite3.connect("Afia na airtime.db")
        #create a cursor
        c = con.cursor()
        c.execute ("SELECT  PACKAGE FROM details  WHERE  HUDUMA_NUMBER = "+ new_huduma)
        dataPackage = c.fetchall()
        package = [list(ele) for ele in dataPackage]
        
        package = package[0][0]
        con.commit()
        #close connections
        con.close()
        if package == "comprehensive":
          premiumComp()
          compreOne()
        else:
          premiumNormal()
          normOne()
      except AttributeError:
        print("   Sorry! Invalid Huduma number ")

    except ValueError:
      print("   Sorry! Invalid input\n")
  else:
    print("   Sorry! The user is not recognised!.Try to register")
# recharge()
def changePackage():
  print("\n   Sorry!, the service is currrently unavailable")
def unsubscribe():
  print("\n   Sorry!, the service is currrently unavailable")
def customercare():
  print("\n   Sorry!, the service is currrently unavailable")
def menu():
  print("________________WELCOME TO AFYA NA AIRTIME________________\n")
  print("   Kindly choose appropriate option")
  print("      1. Subscribe")
  print("      2. Recharge")
  print("      3. Change package")
  print("      4. Contact Customercare")
  print("      5. Unsubscribe ")
  print("      6. EXIT   \n")
  option = input("   Select your option: ")
  try:
    option = int(option)
    if option == 1:
      runProg()
    elif option == 2:
      recharge()
    elif option == 3:
      changePackage()
    elif option == 4:
      unsubscribe()
    elif option == 5:
      customercare()
    elif option == 6:
      exit()
    else:
      print("   Sorry! Invalid option")
  except ValueError:
    print("   Sorry! invald input")
menu()






