name = input("Enter your full name(First, Middle, Last):")
extracted_name = name.split()
first_name = extracted_name[0].strip(",")
middle_name = extracted_name[1].strip(",")
last_name = extracted_name[2].strip(",")
capitalized_first_name = first_name.capitalize()
capitalized_middle_name = middle_name.capitalize()
capitalized_last_name = last_name.capitalize()
middle_initial = middle_name[0].upper() + "."
formatted_name = f"{capitalized_last_name}, {capitalized_first_name} {middle_initial}"
print("Formatted Name:", formatted_name)
print(capitalized_first_name)