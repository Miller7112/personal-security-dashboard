"""
import hashlib:  Used for hashing the password
import requests: Used for making API requests

Check if a password has been leaked using HIBP's free API.

Process:
Using sha1 hashing algorithm: 
- Takes input and generates 40-character hexadecimal hash
- Prefix: First 5 characters is sent to HIBP API to check breach
- Suffix: Remaining 35 characters are stored locally

K-Anonymity:
- By hashing, the actual password is hidden, providing privacy while 
still allowing checks against leaks.

Returns:
- A message indicating whether the password has been found in breaches or is safe.
"""

import hashlib
import requests

def check_password_breach(password):
    sha1_password = hashlib.sha1(password.encode()).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]

    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    if response.status_code == 200:
        hashes = response.text.splitlines()
        found = False
        # print(f"Checking password: {password}\n")
        # print(f"SHA-1 Hash: {sha1_password}")
        # print(f"Searching for prefix: {prefix}\n")
        # print("Leaked Passwords with the Same Prefix:\n")
        
        for line in hashes:
            leaked_suffix, count = line.split(":")

            if leaked_suffix == suffix:
                found = True
                print(f"Your password was found in {count} breaches!")
                # print(f"   Raw Data: {prefix}{leaked_suffix}:{count}")
                print("Consider changing it immediately!\n")

        if not found:
            print("Password is safe (not found in breaches).")
    else:
        print("Error: Could not check password.")

password = input("Enter password to check: ")
check_password_breach(password)
22