# Ichki holatni yashirish va faqat kerakli interfeys orqali kirishni ta'minlash.  # noqa
# https://github.com/theMirmakhmudov
# https://youtube.com/@Mirmakhmudov_coder # noqa

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private attribute

    def deposit(self, amount):
        self.__balance += amount

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.__balance


base_account = BankAccount(100_000)
deposit_balance = BankAccount.deposit(base_account, 300_000)
print(BankAccount.get_balance(base_account))
