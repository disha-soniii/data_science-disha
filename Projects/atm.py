#check balance
#deposit
#withdraw
#transaction history
user_data={"1111":{"name":"disha","balance":10000,"history":[]},
           "2222":{"name":"sangam","balance":15000,"history":[]}}
print("-----------------Welcome to ATM---------------------")
pin=input("Enter your 4 digit pin\n")
if pin in user_data:
    print("welcome",user_data[pin]['name'])
else:
    print("Invalid input")
    
def Show_menu():
    print("-----------MAIN MENU--------------")
    print("1.Check Balance")
    print("2.Deposit Money")
    print("3.Withdraw money")
    print("4.Check Transaction History")
    

def Check_balance(pin):
    print("Your Current Balance is:",user_data[pin]["balance"])
    
def Deposit(pin):
    deposited_amount=float(input("Enter Amount to Deposit\n"))
    if deposited_amount>0:
        user_data[pin]['balance']+=deposited_amount
        user_data[pin]['history'].append(f"Deposited amount{deposited_amount}")
    else:
        print("Invalid Input")
        
def Withdraw(pin):
    withdrawal_amount=float(input("Enter Amount to withdraw\n"))
    if withdrawal_amount>user_data[pin]['balance']:
        print("Invalid Input")
    else:
        if withdrawal_amount>0:
            user_data[pin]['balance']-=withdrawal_amount
            user_data[pin]['history'].append(f"withdraw amount{withdrawal_amount}")
        else:
            print("Invalid Input")
        
def History(pin):
    print("------TRANSACTION HISTORY------")
    if user_data[pin]['history']:
        for h in user_data[pin]['history']:
                print(h)
    else:
            print("No Transactions Yet")
while True:    
    Show_menu()
    choice=int(input("Select options 1-4\n"))
    

    if choice==1:
        Check_balance(pin)
    elif choice==2:
        Deposit(pin)
    elif choice==3:
        Withdraw(pin)
    elif choice==4:
        History(pin)
    elif choice==5:
        print("Thank you for using the ATM")
        break
    else:
        print("Invalid input, choose from 1-5")
        
        
            
    
    
    
    
        
    