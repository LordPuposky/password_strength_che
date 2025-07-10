# Password Strength Checker - W02 Project
# This program helps employees check the strength of their passwords
# Created by: Yesid Romero
#CSE - 111 Programming with functions
# Character type constants defined by the architect Sven
# These lists define the 4 types of characters used for complexity calculation

LOWER = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
UPPER = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SPECIAL = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+", "[", "]", "{", "}", "|", ";", ":", "\"", "'", ",", ".", "<", ">", "?", "/", "`", "~"]

def word_in_file(word, filename, case_sensitive=False):
    """
    Checks if a word exists in a file where each line contains a single word.
    
    Parameters:
    - word: The word to search for
    - filename: The name of the file to search in
    - case_sensitive: If True, performs case-sensitive match; if False, case-insensitive (default: False)
    
    Returns:
    - Boolean: True if word is found, False otherwise
    """
    pass

def word_has_character(word, character_list):
    """
    Checks if any character in the word exists in the provided character list.
    
    Parameters:
    - word: The string to check
    - character_list: List of characters to look for
    
    Returns:
    - Boolean: True if any character from word is in character_list, False otherwise
    """
    pass

def word_complexity(word):
    """
    Calculates the complexity score of a word based on character types it contains.
    Uses the word_has_character function to check for each of the 4 character types.
    
    Parameters:
    - word: The word to analyze
    
    Returns:
    - Integer: Complexity score from 0 to 4 (one point per character type found)
    """
    pass

def password_strength(password, min_length=10, strong_length=16):
    """
    Determines the strength of a password based on multiple criteria.
    Checks against dictionary words, common passwords, length, and complexity.
    
    Parameters:
    - password: The password to evaluate
    - min_length: Minimum acceptable password length (default: 10)
    - strong_length: Length at which password is considered strong (default: 16)
    
    Returns:
    - Integer: Strength score from 0 to 5
    """
    pass

def main():
    """
    Main program loop that handles user interaction.
    Continuously asks for passwords to test until user enters 'q' or 'Q' to quit.
    """
    print("Password Strength Checker")
    print("Enter 'q' or 'Q' to quit the program")
    print("-" * 40)
    
    while True:
        # Get password input from user
        password = input("Enter a password to test: ")
        
        # Check if user wants to quit
        if password == "q" or password == "Q":
            print("Thank you for using the Password Strength Checker!")
            break
        
        # For milestone: just display the password entered
        # Later this will be replaced with actual password_strength function call
        print(f"You entered the password: {password}")
        print("(Password strength analysis will be implemented in the next phase)")
        print("-" * 40)

# This code ensures that main() only runs when the script is executed directly
# (not when imported as a module). This helps the testing team.
if __name__ == "__main__":
    main()