import random
import string

def generate_employee_id():
    prefix = 'EMP'  # Prefix for employee ID
    # Generate a random string of digits
    random_digits = ''.join(random.choices(string.digits, k=6))  # Adjust the length as needed
    # Concatenate the prefix and random digits to create the employee ID
    employee_id = f'{prefix}-{random_digits}'
    return employee_id