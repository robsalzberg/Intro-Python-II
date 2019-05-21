class Item:
    def __init__(self, name, t, durability, description):
        self.name = name
        self.type = t
        self.durability = durability
        self.description = description

    def __str__(self):
        return f"Item Name & Description: {self.name}\n: {self.description}\n"
