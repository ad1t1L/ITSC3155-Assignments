class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        for item, required in ingredients.items():
            if self.machine_resources.get(item, 0) < required:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item, qty in order_ingredients.items():
            self.machine_resources[item] -= qty
        print(f"{sandwich_size} sandwich is ready. Bon appetit!")
