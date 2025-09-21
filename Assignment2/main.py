import data
from sandwich_maker import SandwichMaker
from cashier import Cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

def main():
    while True:
        choice = input("What would you like? (small/medium/large): ").strip().lower()
        if choice == "off":
            break
        if choice == "report":
            for k, v in resources.items():
                print(f"{k}: {v}")
            continue
        if choice not in recipes:
            print("Invalid selection.")
            continue
        order = recipes[choice]
        ingredients = order["ingredients"]
        cost = order["cost"]
        if not sandwich_maker_instance.check_resources(ingredients):
            continue
        coins = cashier_instance.process_coins()
        if not cashier_instance.transaction_result(coins, cost):
            continue
        sandwich_maker_instance.make_sandwich(choice, ingredients)

if __name__ == "__main__":
    main()
