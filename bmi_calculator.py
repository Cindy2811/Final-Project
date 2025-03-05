# Global variable to store the last BMI calculated in the BMI Calculator module
last_bmi = None

def calculate_bmi(weight, height):
    """
    Calculates the Body Mass Index (BMI) using the formula: BMI = weight / (height^2).
    """
    return weight / (height ** 2)

def evaluate_bmi(bmi):
    """
    Evaluates the BMI and returns a string indicating the category:
    "Underweight", "Normal weight", "Overweight", or "Obesity".
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def evaluate_diet(bmi, goal, activity, dietary_restriction, preference):
    """
    Evaluates the user's responses along with their BMI to recommend a dietary plan.
    
    - If the goal is 'gain', recommends a "Caloric Surplus".
    - If the goal is 'lose', recommends a "Caloric Deficit".
    - If the goal is 'maintain', recommends "Maintenance".
    For any other goal, returns "Unrecognized goal".
    """
    if goal.lower() == "gain":
         return "Caloric Surplus"
    elif goal.lower() == "lose":
         return "Caloric Deficit"
    elif goal.lower() == "maintain":
         return "Maintenance"
    else:
         return "Unrecognized goal"

def menu_bmi():
    """
    Interactive menu for the BMI Calculator.
    Prompts the user for gender, age, weight, and height, calculates the BMI,
    displays the category, and then asks if the user wants to perform another BMI calculation.
    Returns True if the user wants to calculate another BMI, or False to return to the main menu.
    """
    global last_bmi
    print("\n--- BMI Calculator ---")
    gender = input("Enter your gender: ")
    try:
        age = int(input("Enter your age: "))
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
    except ValueError:
        print("Invalid input. Please enter numeric values for age, weight, and height.")
        return False

    bmi = calculate_bmi(weight, height)
    last_bmi = bmi  # Store the BMI globally for later use
    category = evaluate_bmi(bmi)
    print(f"\nYour BMI is: {bmi:.2f}")
    print(f"Category: {category}")
    
    # Ask if the user wants to calculate another BMI
    choice = input("\nWould you like to calculate another BMI? (yes/no): ").strip().lower()
    return choice in ("yes", "y")

def menu_diet():
    """
    Interactive menu for dietary recommendations.
    Uses the BMI calculated in the BMI Calculator (Step 1) and then directly asks four key questions:
      1. Main goal (gain/lose/maintain)
      2. Physical activity level (low/medium/high)
      3. Dietary restriction (none/vegetarian/vegan/other)
      4. Eating preference (yes/no for consuming more food at a specific time of day)
    """
    global last_bmi
    print("\n--- Diet ---")
    if last_bmi is None:
        print("You need to calculate your BMI first using the BMI Calculator.")
        input("\nPress Enter to return to the main menu...")
        return
    else:
        print(f"\nYour BMI is: {last_bmi:.2f} ({evaluate_bmi(last_bmi)})")
    
    # Directly ask the four key questions without repeating BMI Calculator inputs
    goal = input("What is your main goal? (gain/lose/maintain): ")
    activity = input("What is your physical activity level? (low/medium/high): ")
    dietary_restriction = input("Do you have any dietary restriction? (none/vegetarian/vegan/other): ")
    preference = input("Do you prefer consuming more food at a specific time of day? (yes/no): ")

    recommendation = evaluate_diet(last_bmi, goal, activity, dietary_restriction, preference)
    print(f"\nRecommendation: {recommendation}")
    input("\nPress Enter to exit the Diet module...")

def main():
    """
    Main function that displays the main menu and allows the user to choose between:
      1. BMI Calculator
      2. Diet
      3. Exit
    """
    while True:
        print("\n=== Main Menu ===")
        print("1. BMI Calculator")
        print("2. Diet")
        print("3. Exit")
        option = input("Select an option (1-3): ")

        if option == "1":
            # Allow repeated BMI calculations until the user decides to exit this module
            while True:
                if not menu_bmi():
                    break
        elif option == "2":
            menu_diet()
        elif option == "3":
            print("Exiting the program...")
            break
        else:
            print("Invalid option. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()