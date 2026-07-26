# Bank Management System

accounts = {}

print("****Welcome to the Bank Management system****")

while True:
    # Display menu
    print("Select an option to perform an operation")
    print("1. Creat Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View all details")
    print("5. Delete Account")
    print("6. Exit")

    choice = int(input("Enter the option between 1 to 6: "))

    # Create a new account
    if choice == 1:
        acc_no = int(input("Enter the Account number: "))

        if acc_no in accounts:
            print("Account alredy exists !")
        else:
            name = input("Enter Account Holder name : ")
            balance = float(input("Enter the Initial balance Rs : "))

            # Store account details
            accounts[acc_no] = {
                "name": name,
                "balance": balance
            }

            print("Account created succesfully")

    # Deposit money
    elif choice == 2:
        acc_no = int(input("Enter the Account number: "))

        if acc_no in accounts:
            deposit = float(input("Enter the amount to deposit Rs : "))
            accounts[acc_no]["balance"] += deposit
            print("Deposit money successfully and the balance is Rs :", accounts[acc_no]["balance"])
        else:
            print("Account not found !")

    # Withdraw money
    elif choice == 3:
        acc_no = int(input("Enter the Account number: "))

        if acc_no in accounts:
            amount = float(input("Enter the amount to Withdraw Rs : "))

            # Check sufficient balance
            if amount <= accounts[acc_no]["balance"]:
                accounts[acc_no]["balance"] -= amount
                print("Withdraw Rs", amount, "successfully done and the balance is Rs", accounts[acc_no]["balance"])
            else:
                print("Invelaid balance! Pleas try again")

    # View account details
    elif choice == 4:
        acc_no = int(input("Enter the Account number: "))

        if acc_no in accounts:
            print("*****Account details****")
            print("Account holder name :", accounts[acc_no]["name"])
            print("Current Balance Rs :", accounts[acc_no]["balance"])
        else:
            print("Account not found!!")

    # Delete account
    elif choice == 5:
        acc_no = int(input("Enter the Account number: "))

        if acc_no in accounts:
            del accounts[acc_no]
            print("Account succesfully Deleted")
        else:
            print("Account not found!!")

    # Exit program
    elif choice == 6:
        print("Thank you for using Bank Management system. Please visit again")
        break

    # Invalid choice
    else:
        print("Invelaid choice !!. please try again")
