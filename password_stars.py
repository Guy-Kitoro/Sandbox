def main():
    # Set the minimum length for the password
    MIN_LENGTH = 8

    while True:
        # Ask the user for a password
        password = input("Enter your password (at least {} characters long): ".format(MIN_LENGTH))

        # Check if the password meets the minimum length requirement
        if len(password) >= MIN_LENGTH:
            # Print asterisks as long as the password
            print('*' * len(password))
            break  # Exit the loop if the password is valid
        else:
            print("Password too short. Please try again.")

if __name__ == "__main__":
    main()
