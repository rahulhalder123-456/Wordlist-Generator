import itertools
import random
import os

def generate_case_combinations(word):
    """Generates all possible combinations of uppercase and lowercase letters for a given word."""
    return [''.join(combination) for combination in itertools.product(*((char.lower(), char.upper()) for char in word))]

def add_leading_zeros(number):
    """Adds leading zeros to a number if it's a single digit."""
    if len(number) == 1:
        return ["0" + number, "00" + number]
    return [number]

def wordlist_generator():
    # Getting user input without defaults, skipping empty inputs
    f_name = input("Enter your first name (optional): ")
    l_name = input("Enter your last name (optional): ")
    animal = input("Enter your favorite animal (optional): ")
    pet_name = input("Enter your pet's name (optional): ")
    number = input("Enter your lucky number (optional): ")
    favourite = input("Enter your favorite thing (optional): ")
    movie = input("Enter your favorite movie (optional): ")
    dob = input("Enter your date of birth (in DDMMYYYY format, optional): ")

    # Split DOB into day, month, and year if provided
    dob_day = dob[:2] if dob else None
    dob_month = dob[2:4] if dob else None
    dob_year = dob[4:] if dob else None

    # Adding inputs to the list only if they are not empty
    words = []
    
    if f_name: words.extend(generate_case_combinations(f_name))
    if l_name: words.extend(generate_case_combinations(l_name))
    if animal: words.extend(generate_case_combinations(animal))
    if pet_name: words.extend(generate_case_combinations(pet_name))
    if number: 
        number_variants = add_leading_zeros(number)
        words.extend(number_variants)
    if favourite: words.extend(generate_case_combinations(favourite))
    if dob_day: words.append(dob_day)
    if dob_month: words.append(dob_month)
    if dob_year: words.append(dob_year)
    if movie: words.extend(generate_case_combinations(movie))

    # Define special characters
    special_chars = ['@', '#', '$', '%', '&', '*', "!", "^", "(", ")", "?", ">", "<", "/", "|", ".", "{", "}", "[", "]", ";", ":"]

    wordlist = []

    # Generate combinations of different lengths
    for r in range(1, min(4, len(words) + 1)):  # Limiting the combination length to prevent explosion
        for combination in itertools.combinations(words, r):
            # Generate permutations of each combination
            for permutation in itertools.permutations(combination):
                # Convert the permutation to a list
                perm_list = list(permutation)

                # Optionally insert special characters
                if random.choice([True, False]):
                    # Randomly decide how many special characters to add
                    num_special_chars = random.randint(1, len(perm_list))

                    # Insert special characters at random positions
                    for _ in range(num_special_chars):
                        special_char = random.choice(special_chars)
                        position = random.randint(0, len(perm_list))
                        perm_list.insert(position, special_char)

                # Join the list into a string and add to the wordlist without spaces
                wordlist.append(''.join(perm_list))

    # Get the directory of the current Python script
    current_directory = os.path.dirname(os.path.abspath(__file__))

    # Define the path for the output txt file
    file_path = os.path.join(current_directory, "wordlist.txt")

    # Write the wordlist to the txt file
    with open(file_path, "w") as file:
        for word in wordlist:
            file.write(word + "\n")

    print(f"Wordlist has been saved to '{file_path}' with {len(wordlist)} entries.")

# Running the function
wordlist_generator()
