#!/usr/bin/env python3

from email_address_parser import EmailAddressParser

if __name__ == '__main__':
    # 1. User Input
    email_string = input("Enter a string containing email addresses: ")

    # 2. Instantiate Parser
    parser = EmailAddressParser(email_string)

    # 3. Parse Email Addresses
    parsed_emails = parser.parse()

    # 4. Display Results
    if parsed_emails:
        print("Parsed email addresses:")
        for email in parsed_emails:
            print(email)
    else:
        print("No email addresses found in the input string.")
