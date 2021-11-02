class Atm:
    def __init__(self, cardnumber, pin):
        self.cardnumber = cardnumber
        self.pin = pin

    def balanceinquiry(self):
        print("Your balcnce is 100$")

    def cashwidthdrawel(self, amount):
        new_amount = 100 - amount
        print("You widthdrawed " + str(amount) + ". Your balance remaining is " + str(new_amount) + "$")

    def cashdeposit(self, money):
        new_money = 100 + money
        print("You deposited " + str(money) + ". Your balance remaining is " + str(new_money) + "$")

def main():
    name = input("Hello!!! What is your name? ")
    print("Hello " + name)
    print("Welcome to the online Atm. Please enter the following details to enter into your account.")
    cardnumber = input("Please enter your Card number: ")
    pin = input("Please enter your Pin: ")
    new_user = Atm(cardnumber, pin)

    print("Choose what you want to do...")
    print("1. Check Bank Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    activity = int(input("Choose what you want to do: "))

    if (activity == 1):
        new_user.balanceinquiry()

    elif (activity == 2):
        money = int(input("Enter the amount you want to deposit: "))
        new_user.cashdeposit(money)
        print("Thank you for working with us... Have a nice day...")

    elif (activity == 3):
        amount = int(input("Enter the amount you want to withdraw: "))
        new_user.cashwidthdrawel(amount)
        print("Thank you for working with us... Have a nice day...")

if __name__ == "__main__":
    main()