class CoffeeMachine:

    espresso = [250, 0, 16, 1, -4]
    latte = [350, 75, 20, 1, -7]
    cappuccino = [200, 100, 12, 1, -6]
    supplies_name = ["water", "milk", "coffee beans", "disposable cup", "money"]

    def __init__(self, water, milk, coffee_beans, cups, money):
        self.supplies = [water, milk, coffee_beans, cups, money]

    def main_menu(self):
        print("Write action (buy, fill, take, remaining, exit):")
        action = input()
        if action == "buy":
            self.buy(self.choose_recipe())
        elif action == "fill":
            CoffeeMachine.fill(self)
        elif action == "take":
            CoffeeMachine.take(self)
        elif action == "remaining":
            CoffeeMachine.remaining(self)
        elif action == "exit":
            return None

    def remaining(self):
        print(f"\nThe coffee machine has:\n"
              f"{self.supplies[0]} of water\n"
              f"{self.supplies[1]} of milk\n"
              f"{self.supplies[2]} of coffee beans\n"
              f"{self.supplies[3]} of disposable cups\n"
              f"${self.supplies[4]} of money\n")
        return self.main_menu()

    def choose_recipe(self):
        print()
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        menu = input()
        if menu == "1":
            return self.espresso
        if menu == "2":
            return self.latte
        if menu == "3":
            return self.cappuccino
        if menu == "back":
            print()
            return self.main_menu()

    def buy(self, recipe):
        if recipe is None:
            pass
        else:
            for i in range(len(self.supplies)):
                if self.supplies[i] - recipe[i] < 0:
                    print(f"Sorry, not enough {self.supplies_name[i]}!\n")
                    return self.main_menu()
                else:
                    self.supplies[i] -= recipe[i]
                    if i == len(self.supplies) - 1:
                        print("I have enough resources, making you a coffee!\n")
                        return self.main_menu()

    def fill(self):
        print()
        for i in range(len(self.supplies) - 1):
            if i < 2:
                print(f"Write how many ml of {self.supplies_name[i]} do you want to add:")
                self.supplies[i] += int(input())
            elif i == 2:
                print("Write how many grams of coffee beans do you want to add:")
                self.supplies[i] += int(input())
            else:
                print('Write how many disposable cups of coffee you will need to add:')
                self.supplies[i] += int(input())
        print()
        return self.main_menu()

    def take(self):
        print(f"\nI gave you ${self.supplies[4]}")
        self.supplies[4] -= self.supplies[4]
        print()
        return self.main_menu()


coffee = CoffeeMachine(400, 540, 120, 9, 550)
coffee.main_menu()
