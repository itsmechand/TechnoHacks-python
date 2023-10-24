class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        return self.balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"The deposited amount is {amount}. The total new amount is: {self.balance}"
        else:
            return "You entered an invalid amount..."
        
    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            return f"The withdrawal amount is {amount}. The available amount is: {self.balance}"
        else:
            return "Insufficient funds or invalid withdrawal amount."

def main():
    atm = ATM(0)

    while True:
        print("\nATM Simulation machine")
        print("Select an operation you want to perform:")
        print("1. Check Balance")
        print("2. Deposit amount")
        print("3. Withdraw amount")
        print("4. Exit")

        choice = int(input("Enter option number: "))

        if choice == 1:
            print(f"The available balance is: {atm.check_balance()}")

        elif choice == 2:
            amount = float(input("Enter amount you want to deposit: "))
            print(atm.deposit(amount))
            print(f"The available balance is: {atm.check_balance()}")

        elif choice == 3:
            amount = float(input("Enter amount you want to withdraw: "))
            print(atm.withdraw(amount))
            print(f"The available balance is: {atm.check_balance()}")

        elif choice == 4:
            print("Thank you for using the ATM. Goodbye")
            break

        else:
            print("Invalid choice. Please choose a valid option.")


if __name__ == "__main__":
    main()