user_details={
    'Name':'Balaji',
    'phone':7416866586,
    'ATM_PIN': 2003,
    'email':'akulasivasaibalaji47@gmail.com',
    'ACC_num':4450811858,
    'IFSC':'KKBK0008454',
    'ACC_Balance': 1000
}
import random
attempts=3
while attempts>0:
    user_pin=int(input('Enter your ATM_PIN: '))
    if user_details['ATM_PIN']==user_pin:
        print("WELCOME TO ATM")
        print("==============")
        print()
        print("1.withdrawl\n2.deposit\n3.check balance\n4.pinchange")
        user_choice=int(input("Enter a option from above :) "))
        if user_choice==1:
            withdraw_amount=int(input("Enter amount in multiples of 100,200,500: "))
            if withdraw_amount%100==0:
                if withdraw_amount<=user_details['ACC_Balance']:
                    user_details['ACC_Balance']=user_details['ACC_Balance']-withdraw_amount
                    print(f"Take Your Cash {withdraw_amount} rupees")
                    print(f"remaining amount {user_details['ACC_Balance']}")
                else:
                    print("Insuficcent Balance !!!")
                    break
            else:
                print("entered invalid amount :( ")
                break
        elif user_choice==3:
            print(f"{user_details['ACC_Balance']} is your account balance")

        elif user_choice==2:
            deposit=int(input("Enter you deposit amount: "))
            if deposit%100==0:
                user_details['ACC_Balance']+=deposit
                print(f"Your Acc_Balance is {user_details['ACC_Balance']} after {deposit} amount added")
            else:
                print("Enter amount in multiples of 100 200 500")

        elif user_choice==4:
            otp=random.randint(1000,9999)
            print(f"otp : {otp} ")
            user_otp=int(input("Enter the above OTP: "))
            if otp==user_otp:
                new_pin=int(input("Enter your new 4 digit-pin"))
                new_pin=str(new_pin)
                new_pin_list=list(new_pin)            
                if len(new_pin_list)==4:
                    new_pin=int(new_pin)
                    user_details['ATM_PIN']=new_pin
                    print(f"New pin generated - {user_details['ATM_PIN']}")
                else:
                    print("invalid new pin")
            else:
                print("Invalid OTP")
        else:
            print("Invalid choice")
            break
    else:
        attempts=attempts-1
        if attempts>0:
            print(f"Incorrect pin you still have {attempts} attempts left")
        else:
            print("card is blocked")