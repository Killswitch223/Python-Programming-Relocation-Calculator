import os
from models.expense import Expense

class FinancialEngine:
    @staticmethod
    def calculate_total_burden(profile):
        # Calculate overlapping rent
        double_rent_cost = (profile.old_rent + profile.new_rent) * profile.overlap_months
        
        # Calculate extra expenses
        extra_costs = sum(exp.amount for exp in profile.additional_expenses)
        
        return double_rent_cost + extra_costs

    @staticmethod
    def save_report_to_file(profile, total_cost, filepath="data/expenses.txt"):
        # Ensure directory exists
        os.makedirs(os.path.dirname(filepath), exist_ok=True)
        
        with open(filepath, "w", encoding="utf-8") as file:
            file.write(f"--- Relocation Report ---\n")
            file.write(f"Base Double Rent Overlap: €{(profile.old_rent + profile.new_rent) * profile.overlap_months:.2f}\n")
            file.write("Additional Items Logged:\n")
            for exp in profile.additional_expenses:
                file.write(f" - {exp.to_string()}\n")
            file.write(f"Total Projected Financial Burden: €{total_cost:.2f}\n")
        print(f"\nReport successfully compiled and saved to {filepath}!")
