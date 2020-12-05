class CoffeeMachine:
    def __init__(self):
        print("Coffee machine is ON")
        self.water = 2000
        self.milk = 1500
        self.coffee = 1000
        self.money  = 10

    def report(self):
        print("The Current resource Available are:")
        print("Water : ", self.water)
        print("Milk  : ", self.milk)
        print("Coffee: ", self.coffee)
        print("Money : ", self.money)

    def checkResources(self, coffee):
        if coffee["milk"] >= self.milk:
            print("Sorry there is not enough Milk")
            return -1
        elif coffee["water"] >= self.water:
            print("Sorry there is not enough Water")
            return -1
        elif coffee["coffee"] >= self.coffee:
            print("Sorry there is not enough Coffee")            
            return -1
        else:
            return 1
    
    def getMoney(self):
        print("Insert Coins")
        q = int(input("Enter no.of Quarters: "))
        d = int(input("Enter no.of Dimes: "))
        n = int(input("Enter no.of Nickel: "))
        p = int(input("Enter no.of Pennies: "))

        return (q*0.25) + (d*0.10) + (n*0.05) + (p*0.01)

    def checkMoney(self, coffee, amount):
        if coffee["money"] > amount:
            print("\nSorry that's not enough money")
            return -1
        elif coffee["money"] < amount:
            self.money = self.money + coffee["money"]
            self.water = self.water - coffee["water"]
            self.milk = self.milk - coffee["milk"]
            self.coffee = self.coffee - coffee["coffee"]
            print("\n---->Here is the change: ", amount - coffee["money"])
            return 1
        else:
            self.money = self.money + coffee["money"]
