class Expense:
    def __init__(self, name, amount, is_recurring=False):
        self.name = name
        self.amount = float(amount)
        self.is_recurring = is_recurring

    def to_string(self):
        type_str = "Monthly" if self.is_recurring else "One-off"
        return f"{self.name}: €{self.amount:.2f} ({type_str})"
