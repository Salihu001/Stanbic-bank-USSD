print("Here are the available bank USSD codes:\n---------------------------")
available_bank = {"UBA": "*919#", "Wema bank": "*945#", "FCMB": "*329#", "Access bank": "*901#",
                  "Polaris(Skye)": "*833#", "GT Bank": "*737#", "Zenith bank": "*966#",
                  "Eco bank": "*326#", "First Bank": "*894#", "Stanbic IBTC bank": "*909#",
                  "Diamond bank": "*426#", "Fidelity bank": "*770#", "Sterling bank": "*822#",
                  "Unity bank": "*7799#\n---------------------------"}

my_bank_name = "Stanbic IBTC bank"
my_bank_code = "909"

for key, value in available_bank.items():
    print("{}:{}".format(key, value))

my_bank_ussd = input("Please enter your bank ussd code here without non-digit characters>")

if my_bank_ussd == my_bank_code:
    print("\nYou have entered the code for", my_bank_name)

    print("\n1.\tCheck your balance\n2.\tTransfers\n3.\tAirtime\n4.\tTransaction history")
    option = int(input("\nPlease select an option: "))


    def main_menu():
        while True:
            print("\n1.\tCheck your balance\n2.\tTransfers\n3.\tAirtime\n4.\tTransaction history")

            option = int(input("\nPlease select an option: "))

            if option == 1:
                account_balance = "10,000.00"
                print("Your account balance is NGN", account_balance)
                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                if return_menu == 2:
                    exit(0)

            elif option == 2:
                transfer_account = input('Enter account number you want to transfer money to: \n')
                transfer_amount = input("Enter amount: ")
                transfer_confirm = int(input("Do you want to send NGN {} to this {} ?\n1.\tYES\n2.\tNO".format(transfer_amount,transfer_account)))
                if transfer_confirm == 1:
                    transfer_pin = int(input("Enter 4-digit pin: "))
                    if transfer_pin == 1235:
                        print("TRANSACTION SUCESSFUL")
                if transfer_confirm == 2:
                    return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                    if return_menu == 1:
                        continue
                    if return_menu == 2:
                        exit(0)

                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                if return_menu == 2:
                    exit(0)

            elif option == 3:
                airtime_menu = int(input("Enter 1 or 2: \n1.\tFor self\n2.\tFor others"))
                airtime_self_no = 234706043040
                if airtime_menu == 1:
                 airtime_amount = int(input("Enter amount: "))
                 print("Do you want to buy NGN{} worth of airtime for {}".format(airtime_amount, airtime_self_no))
                 airtime_confirm = int(input("Enter 1 or 2: \n1.\tYES\n2.\tNO"))
                 if airtime_confirm == 1:
                     transfer_pin = int(input("Enter 4-digit pin: "))
                     if transfer_pin == 1235:
                         print("TRANSACTION SUCESSFUL")
                         return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                         if return_menu == 1:
                             continue
                         if return_menu == 2:
                             exit(0)

                elif airtime_menu ==2:
                    airtime_others = int(input("Enter number you want to buy airtime for:"))
                    airtime_amount = int(input("Enter amount: "))
                    print("Do you want to buy NGN{} worth of airtime for {}".format(airtime_amount, airtime_others))
                    airtime_confirm = int(input("Enter 1 or 2: \n1.\tYES\n2.\tNO"))
                    if airtime_confirm == 1:
                        transfer_pin = int(input("Enter 4-digit pin: "))
                        if transfer_pin == 1235:
                            print("TRANSACTION SUCESSFUL")

                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                if return_menu == 2:
                    exit(0)

            elif option == 4:
                print('An SMS message would be sent to you shortly\n')
                return_menu = int(input("ENTER 1. TO RETURN MENU 2.TO END"))
                if return_menu == 1:
                    continue
                if return_menu == 2:
                    exit(0)


    main_menu()


else:
    if type(my_bank_ussd) != int:

        print("That wasn't a numeric input, try again!")
    else:
        print("Sorry only ", my_bank_name, "USSD banking is available at the moment\nKindly check back")
