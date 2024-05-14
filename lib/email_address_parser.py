import re

class EmailAddressParser:
    '''A simple email address parser'''

    def __init__(self, email_string):
        self.email_string = email_string

    def parse(self):
        '''Parse email addresses from the provided string'''
        email_regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        return re.findall(email_regex, self.email_string)

if __name__ == "__main__":
    # Example usage
    email_string = "talk@talk.com john.jones@flatironschool.com alexa@amazon.com"
    parser = EmailAddressParser(email_string)
    parsed_emails = parser.parse()
    print("Parsed emails:", parsed_emails)
