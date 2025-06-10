# Fence cost calculator
# Author:Caleb whitcombe
# Date: 28 May 2025
# Version 1.0

def calculate_fence_cost():
    while True:
        try:
            # Ask for the dimensions of the fence
            length = float(input("Enter the length of the fence (in meters): "))
            width = float(input("Enter the width of the fence (in meters): "))
            
            # Calculate the perimeter
            perimeter = 2 * (length + width)
            print(f"The perimeter of the fence is {perimeter} meters.")
            
            # Ask for the cost of fencing per meter
            cost_per_meter = float(input("Enter the cost of fencing per meter: "))
            
            # Calculate the total cost
            total_cost = perimeter * cost_per_meter
            print(f"The total cost of fencing is ${total_cost:.2f}")
            
            # Ask if the user wants to perform another calculation
            keep_going = input("Press <Enter> to calculate again or any other key to quit: ")
            if keep_going != "":
                print("Goodbye!")
                break
        except ValueError:
            print("Invalid input. Please enter numeric values.")
        