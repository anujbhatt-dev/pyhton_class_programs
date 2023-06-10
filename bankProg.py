#Write Python Program to Simulate a Bank Account for deposit,withdraw and balance
#Operations

class Bank:
    def __init__(self, name):
        self.cust_name = name
        self.bal = 0.0

    def sbal(self):
        print(f"{self.cust_name} has a balance of {self.bal} Rs")

    def wmon(self, amt):
        if amt > self.bal:
            print("You don't have sufficient funds in your account")
        else:
            self.bal -= amt
            print(f"{self.cust_name} has withdrawn an amount of {self.bal} Rs")

    def dmon(self, amt):
        self.bal += amt
        print(f"{self.cust_name} has deposited an amount of {self.bal} Rs")
        
def main():
    acc = Bank("Nihira")
    acc.dmon(1000)
    acc.sbal()
    acc.wmon(500)
    acc.sbal()

if __name__ == "__main__":
    main()
