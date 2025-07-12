# Password Strength Checker - W02 Project
# This program helps employees check the strength of their passwords
# Created by: Yesid Romero
# CSE - 111 Programming with functions
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
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line_word = line.strip()
                if case_sensitive:
                    if line_word == word:
                        return True
                else:
                    if line_word.lower() == word.lower():
                        return True
    except FileNotFoundError:
        # Silent mode - no warning messages for missing files
        pass
    return False

def word_has_character(word, character_list):
    """
    Checks if any character in the word exists in the provided character list.
    
    Parameters:
    - word: The string to check
    - character_list: List of characters to look for
    
    Returns:
    - Boolean: True if any character from word is in character_list, False otherwise
    """
    for char in word:
        if char in character_list:
            return True
    return False

def word_complexity(word):
    """
    Calculates the complexity score of a word based on character types it contains.
    Uses the word_has_character function to check for each of the 4 character types.
    
    Parameters:
    - word: The word to analyze
    
    Returns:
    - Integer: Complexity score from 0 to 4 (one point per character type found)
    """
    complexity = 0
    if word_has_character(word, LOWER):
        complexity += 1
    if word_has_character(word, UPPER):
        complexity += 1
    if word_has_character(word, DIGITS):
        complexity += 1
    if word_has_character(word, SPECIAL):
        complexity += 1
    return complexity

# CREATIVE ENHANCEMENT 1: Pattern Detection
def has_common_patterns(password):
    """
    Checks for common unsafe patterns in passwords.
    This is a creative enhancement to improve password security analysis.
    
    Parameters:
    - password: The password to analyze
    
    Returns:
    - Boolean: True if common patterns are found, False otherwise
    """
    password_lower = password.lower()
    common_patterns = [
        "123", "abc", "qwerty", "password", "admin", "user",
        "000", "111", "aaa", "login", "welcome", "master"
    ]
    
    for pattern in common_patterns:
        if pattern in password_lower:
            return True
    return False

# CREATIVE ENHANCEMENT 2: Password Improvement Suggestions
def suggest_improvements(password):
    """
    Provides specific suggestions to improve password strength.
    This is a creative enhancement to help users create better passwords.
    
    Parameters:
    - password: The password to analyze
    
    Returns:
    - List: List of improvement suggestions
    """
    suggestions = []
    
    if not word_has_character(password, UPPER):
        suggestions.append("Add uppercase letters (A-Z)")
    if not word_has_character(password, LOWER):
        suggestions.append("Add lowercase letters (a-z)")
    if not word_has_character(password, DIGITS):
        suggestions.append("Add numbers (0-9)")
    if not word_has_character(password, SPECIAL):
        suggestions.append("Add special characters (!@#$%^&*)")
    
    if len(password) < 10:
        suggestions.append(f"Make it longer (current: {len(password)}, recommended: 10+)")
    
    if has_common_patterns(password):
        suggestions.append("Avoid common patterns like '123', 'abc', or 'password'")
    
    return suggestions

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
    # Check if password is in dictionary (case insensitive)
    if word_in_file(password, "wordlist.txt"):
        print("Password is a dictionary word and is not secure.")
        return 0
    
    # Check if password is in top passwords list (case sensitive)
    if word_in_file(password, "toppasswords.txt", case_sensitive=True):
        print("Password is a commonly used password and is not secure.")
        return 0
    
    # CREATIVE ENHANCEMENT: Check for common patterns
    if has_common_patterns(password):
        print("Password contains common patterns and may not be secure.")
        # Don't return 0 here, just warn but continue evaluation
    
    # Check password length
    if len(password) < min_length:
        print("Password is too short and is not secure.")
        return 1
    
    # Check if password is long enough to be strong
    if len(password) >= strong_length:
        print("Password is long, length trumps complexity this is a good password.")
        return 5
    
    # Calculate complexity and determine strength
    complexity = word_complexity(password)
    strength = 1 + complexity
    return strength

def main():
    """
    Main program loop that handles user interaction.
    Continuously asks for passwords to test until user enters 'q' or 'Q' to quit.
    Enhanced with creative features: pattern detection and improvement suggestions.
    """
    print("Password Strength Checker - Enhanced Version")
    print("Enter 'q' or 'Q' to quit the program")
    print("-" * 50)
    
    while True:
        # Get password input from user
        password = input("Enter a password to test: ")
        
        # Check if user wants to quit
        if password.lower() == "q":
            print("Thank you for using the Password Strength Checker!")
            break
        
        # Check password strength
        strength = password_strength(password)
        print(f"Password strength: {strength}/5")
        
        # CREATIVE ENHANCEMENT: Show improvement suggestions if password is weak
        if strength < 4:
            suggestions = suggest_improvements(password)
            if suggestions:
                print("\nSuggestions for improvement:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"  {i}. {suggestion}")
        
        print("-" * 50)

if __name__ == "__main__":
    main()