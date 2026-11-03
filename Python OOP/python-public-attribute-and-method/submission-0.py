class StoreItem:
    def __init__(self, name, price):
        self.name = name
        self.price = price


chips = StoreItem("Chips", 1.99) # Don't modify this line
print(f"{chips.name}")
print(chips.price)


