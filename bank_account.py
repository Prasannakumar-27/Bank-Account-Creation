import random
import string
import hashlib

class Account:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = self.hash_password(password)
        self.account_number = self.generate_account_number()
        self.balance = 0  # Initial balance is 0
        self.transaction_history = []  # To store transaction records

    def hash_password(self, password):
        """Hash the password for security purposes (simple example using SHA-256)"""
        return hashlib.sha256(password.encode()).hexdigest()

    def generate_account_number(self):
        """Generate a random 10-digit account number"""
        return ''.join(random.choices(string.digits, k=10))

    def deposit(self, amount):
        """Deposits money into the account."""
        if amount <= 0:
            print("Deposit amount must be greater than 0.")
        else:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}. New balance: {self.balance}")
            print(f"Deposited {amount}. New balance: {self.balance}")

    def withdraw(self, amount):
        """Withdraws money from the account, ensuring sufficient balance."""
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.balance:
            print(f"Insufficient funds. Your balance is {self.balance}.")
        else:
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}. New balance: {self.balance}")
            print(f"Withdrew {amount}. New balance: {self.balance}")

    def check_balance(self):
        """Returns the current balance of the account."""
        print(f"Current balance: {self.balance}")

    def transfer(self, amount, target_account):
        """Transfers money from this account to another account."""
        if amount <= 0:
            print("Transfer amount must be greater than 0.")
            return

        if amount > self.balance:
            print(f"Insufficient funds. Your balance is {self.balance}.")
            return

        self.balance -= amount
        target_account.balance += amount

        # Record the transaction in both accounts' history
        self.transaction_history.append(f"Transferred {amount} to {target_account.account_number}. New balance: {self.balance}")
        target_account.transaction_history.append(f"Received {amount} from {self.account_number}. New balance: {target_account.balance}")

        print(f"Transferred {amount} to account {target_account.account_number}. New balance: {self.balance}")

    def __str__(self):
        return f"Account Name: {self.name}, Email: {self.email}, Account Number: {self.account_number}, Balance: {self.balance}"

    def show_transaction_history(self):
        """Show the transaction history for this account."""
        if self.transaction_history:
            print("Transaction History:")
            for transaction in self.transaction_history:
                print(transaction)
        else:
            print("No transactions yet.")

class AccountManager:
    def __init__(self):
        self.accounts = {}

    def create_account(self, name, email, password):
        """Creates a new account."""
        # Check if email already exists
        if email in self.accounts:
            print(f"An account with email {email} already exists.")
            return None

        # Create a new account and add it to the dictionary
        new_account = Account(name, email, password)
        self.accounts[email] = new_account
        print(f"Account created successfully for {name}. Account Number: {new_account.account_number}")
        return new_account

    def get_account(self, email):
        """Retrieves account by email."""
        return self.accounts.get(email, None)

    def display_all_accounts(self):
        """Displays all created accounts."""
        for account in self.accounts.values():
            print(account)

# Main function to interact with the system
def main():
    account_manager = AccountManager()

    while True:
        print("\nAccount Management Menu:")
        print("1. Create Account")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Check Balance")
        print("5. Transfer Money")
        print("6. Show Transaction History")
        print("7. View All Accounts")
        print("8. Exit")
        
        choice = input("Please choose an option (1/2/3/4/5/6/7/8): ").strip()
        
        if choice == '1':
            name = input("Enter your name: ").strip()
            email = input("Enter your email: ").strip()
            password = input("Enter your password: ").strip()
            
            account_manager.create_account(name, email, password)

        elif choice == '2':
            email = input("Enter your email: ").strip()
            account = account_manager.get_account(email)
            if account:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            else:
                print("Account not found.")

        elif choice == '3':
            email = input("Enter your email: ").strip()
            account = account_manager.get_account(email)
            if account:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount. Please enter a numeric value.")
            else:
                print("Account not found.")
        
        elif choice == '4':
            email = input("Enter your email: ").strip()
            account = account_manager.get_account(email)
            if account:
                account.check_balance()
            else:
                print("Account not found.")
        
        elif choice == '5':
            sender_email = input("Enter your email: ").strip()
            sender_account = account_manager.get_account(sender_email)
            if sender_account:
                target_email = input("Enter the recipient's email: ").strip()
                target_account = account_manager.get_account(target_email)
                if target_account:
                    try:
                        amount = float(input("Enter amount to transfer: "))
                        sender_account.transfer(amount, target_account)
                    except ValueError:
                        print("Invalid amount. Please enter a numeric value.")
                else:
                    print("Recipient account not found.")
            else:
                print("Your account not found.")
        
        elif choice == '6':
            email = input("Enter your email: ").strip()
            account = account_manager.get_account(email)
            if account:
                account.show_transaction_history()
            else:
                print("Account not found.")

        elif choice == '7':
            account_manager.display_all_accounts()

        elif choice == '8':
            print("Exiting the system.")
            break
        
        else:
            print("Invalid option, please try again.")

# Run the main function to start the account management system
if __name__ == "__main__":
    main()
