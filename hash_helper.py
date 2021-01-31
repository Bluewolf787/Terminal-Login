import hashlib
import os


# This function is used to hash a password
def hash_password(plaintext):
    salt = os.urandom(32) # Create a random salt
    key = hashlib.pbkdf2_hmac(
        'sha256',
        plaintext.encode('utf-8'),
        salt,
        100000
    )

    storage = salt + key # Store salt and key in on string as storage

    return storage


# This function is used to check if a entered password is the same as a password for a specific user
def check_password(plaintext, salt):
    key = hashlib.pbkdf2_hmac(
        'sha256',
        plaintext.encode('utf-8'),
        salt, # The salt from a specific user
        100000
    )

    return key # Return the new key