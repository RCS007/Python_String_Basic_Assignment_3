# Question 3

# Ask the user to enter their first name and surname in lower case. Change the case to title case and join them
# together. Display the finished result.

# Ask the user to enter their first name in lowercase
first_name = input("Enter your first name in lowercase: ")

# Ask the user to enter their surname in lowercase
surname = input("Enter your surname in lowercase: ")

# Convert both names to title case (first letter capitalized)
full_name = first_name.title() + " " + surname.title()

# Display the final result
print(f"Your formatted name is: {full_name}")