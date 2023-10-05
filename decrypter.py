import os
import pyaes

# Define the root directory where the encrypted files are located
root_directory = r"C:\Users\alanv\Pictures"

# Define the decryption key (must be the same as used for encryption)
key = b"testeransomwares"

# Function to decrypt a file
def decrypt_file(encrypted_file_path, key):
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_data = encrypted_file.read()

    # Decrypt the file data using AES
    aes = pyaes.AESModeOfOperationCTR(key)
    decrypted_data = aes.decrypt(encrypted_data)

    # Remove the ".ransomwaretroll" extension to get the original file name
    original_file_path = encrypted_file_path[:-len(".ransomwaretroll")]

    # Write the decrypted data to the original file
    with open(original_file_path, 'wb') as original_file:
        original_file.write(decrypted_data)

    # Remove the encrypted file
    os.remove(encrypted_file_path)

# Walk through the root directory and decrypt ".ransomwaretroll" files
for root, dirs, files in os.walk(root_directory):
    for file in files:
        if file.endswith('.ransomwaretroll'):
            encrypted_file_path = os.path.join(root, file)
            decrypt_file(encrypted_file_path, key)



