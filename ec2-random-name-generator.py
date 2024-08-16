import random
import string

# Step 1: Input Validation
ec2_count = int(input('How many EC2 instances? '))
if ec2_count < 1:
    print('Enter a valid count!')
else:
    print(f'You have {ec2_count} instances to name!')

dept_name = input('What is your department name? ')
valid_departments = ['Marketing', 'Accounting', 'FinOps']

if dept_name not in valid_departments:
    print('You should not use this Name Generator!')
else:
    print('Congratulations! You qualify to use the Name Generator!')

# Step 2: Generate Unique Names
def generate_unique_name(dept_name):
    # Random string of 6 characters (letters and digits)
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"{dept_name}-{random_string}"

unique_names = []
for _ in range(ec2_count):
    unique_name = generate_unique_name(dept_name)
    unique_names.append(unique_name)

# Step 3: Output the Names
print("\nGenerated EC2 Instance Names:")
for name in unique_names:
    print(name)


