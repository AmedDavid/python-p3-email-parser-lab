# your code goes here!

import re

class EmailAddressParser:
    def __init__(self, addresses: str):
        self.addresses = addresses

    def parse(self):
        # Split by commas or whitespace
        parts = re.split(r'[, ]+', self.addresses)

        # Simple regex for validating emails
        email_pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')

        # Filter valid emails only
        valid_emails = [email for email in parts if email_pattern.match(email)]

        # Return unique sorted emails
        return sorted(set(valid_emails))
