import random
import string

#  Generate an instance name
def generate_instance_name(index, department):
    random_suffix = ''.join(random.choices(string.ascii_uppercase + string.digits, k=5))
    return f"{department.lower()}-instance-{index}-{random_suffix}"

# How many instance does the user want
try:
    num_instances = int(input("How many instances do you need? "))
    if num_instances <= 0:
        print("Please enter a positive number.")
    else:
        # Ask for the department name
        department_name = input("Enter your department name (e.g., Marketing, Accounting, FinOps): ").strip()

        print("\nHere are your instance names:")
        for i in range(1, num_instances + 1):
            print(generate_instance_name(i, department_name))
except ValueError:
    print("Invalid input! Please enter a valid number.")