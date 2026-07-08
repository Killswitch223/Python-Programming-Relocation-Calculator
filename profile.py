class TenantProfile:
    def __init__(self, old_rent, new_rent, overlap_months):
        self.old_rent = float(old_rent)
        self.new_rent = float(new_rent)
        self.overlap_months = int(overlap_months)
        self.additional_expenses = []

    def add_expense(self, expense):
        self.additional_expenses.append(expense)
