def calculate_moving_costs():
    print("--- Relocation Financial Calculator ---")
    
    # Get user inputs
    old_rent = float(input("Enter rent for old apartment: €"))
    new_rent = float(input("Enter rent for new apartment: €"))
    overlap_months = int(input("How many months will you pay double rent? "))
    moving_lump_sum = float(input("Enter estimated moving service/lump sum costs: €"))
    
    # Calculate costs
    double_rent_cost = (old_rent + new_rent) * overlap_months
    total_moving_cost = double_rent_cost + moving_lump_sum
    
    # Output results
    print("\n--- Summary ---")
    print(f"Double Rent Burden: €{double_rent_cost:.2f}")
    print(f"Total Relocation Cost: €{total_moving_cost:.2f}")
    print("----------------")

if __name__ == "__main__":
    calculate_moving_costs()
