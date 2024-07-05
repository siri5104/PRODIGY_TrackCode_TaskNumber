import re


def check_password_strength(password):
    

    length_criteria = len(password) >= 8
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    digit_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'[!@#$%^&*(),.?":{}|<>]', password) is not None

    criteria_met = sum([length_criteria, lowercase_criteria, uppercase_criteria, digit_criteria, special_char_criteria])

    if criteria_met == 5:
        return "Strong password."
    elif criteria_met == 4:
        return "Moderate password."
    elif criteria_met == 3:
        return "Weak password add more."
    else:
        return "Very weak password. Try adding more characters, including uppercase, lowercase, digits, and special characters."


def main():
    while True:
        password = input("Enter a password to check (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("bye")
            break

        strength_message = check_password_strength(password)
        print(strength_message)


if __name__ == "__main__":
    main()
