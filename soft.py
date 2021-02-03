from flask import Flask
from flask import request
from flask import make_response

app = Flask(__name__)

@app.route('/api/ussd/callback', methods=['POST'])
def ussd_callback():
    session_id = request.values.get("sessionId", None)
    serviceCode = request.values.get("serviceCode", None)
    phoneNumber = request.values.get("phoneNumber", None)
    text = request.values.get("text", None)

    #serve menus based on text
    if text == "":
        menu_text = "CON What would you want to check \n"
        menu_text += "1. My Account \n"
        menu_text += "2. My phone number \n"
        menu_text += "3. My branch"

    elif text =="1":
        menu_text = "CON Choose the account information that you want to view \n"
        menu_text += "1. My Account balance\n"
        menu_text += "2. My Account number \n"

    elif text =="2":
            menu_text = "END Your phone number is "+ phoneNumber

    elif text =="1*1":
            menu_text = "END Your account number is ACOO10SWO2101."

    elif text =="1*2":
            menu_text = "END Your BALANCE  is KES 120/-"

    resp = make_response(menu_text, 200)
    resp.headers['Content-Type'] = "text/plain"
    return resp
if __name__ == "__main__":
        app.run()

# print("          Welcome to Afia na airtime")
# choice = input("     Do you want to opt for afia na airtime? (y/n): ")
# if choice == "y" or choice == "Y":
#   print("     Print please select what you want to opt for")
#   print("      1. Do you want to opt for comprehensive?")
#   print("      2. Do you want to opt for normal coverage?")
#   option = int(input("Option: "))
#   if option == 1:
#     f_name = input("      Enter your first name: ")
#     s_name = input("      Enter the second name: ")
#     user_id = input("     Enter national id :")
#     recharge_amount = input("      Enter the amount to recharge: ")
#   else:
#     print("Invalid inputs")

# elif choice == "n" or choice == "N":
#   print("Welcome some other time")
# else:
#   print("Invalid input")
