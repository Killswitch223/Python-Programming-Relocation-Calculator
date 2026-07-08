from models.profile import TenantProfile
from models.expense import Expense
from financial_engine import FinancialEngine

def run_app():
    print("=== Welcome to the Modular Relocation System ===")
    old_r = input("Enter old monthly rent: €")
    new_r = input("Enter new monthly rent: €")
    overlap = input("Enter lease overlap (in months): ")
    
    profile = TenantProfile(old_r, new_r, overlap)
    
    while True:
        print("\n[1] Add Moving Expense Line Item\n[2] Calculate & Save Final Report\n[3] Exit")
        choice = input("Select an option: ")
        
        if choice == '1':
            name = input("Expense name (e.g., Truck Rental): ")
            amt = input("Amount: €")
            profile.add_expense(Expense(name, amt))
        elif choice == '2':
            total = FinancialEngine.calculate_total_burden(profile)
            FinancialEngine.save_report_to_file(profile, total)
            break
        elif choice == '3':
            break
        else:
            print("Invalid selection.")

if __name__ == "__main__":
    run_app()
