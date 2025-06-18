from Crypto.Cipher import Salsa20
import os

def encrypt(paths, file_names, key):
    # Ensure key is bytes
    key_bytes = key.encode('utf-8') if isinstance(key, str) else key
    
    for i, current_path in enumerate(paths):
        try:
            # Read the original file
            with open(current_path, 'rb') as f:
                data = f.read()
            
            # Create cipher object and encrypt the data
            cipher = Salsa20.new(key=key_bytes)
            encrypted_data = cipher.nonce + cipher.encrypt(data)
            
            # Extract directory and filename components
            directory = os.path.dirname(current_path)
            filename = os.path.basename(current_path)
            base, ext = os.path.splitext(filename)
            
            # Create encrypted filename (preserving extension)
            encrypted_filename = f"{base}_encrypted{ext}"
            encrypted_path = os.path.join(directory, encrypted_filename)
            
            # Write the encrypted data
            with open(encrypted_path, 'wb') as f:
                f.write(encrypted_data)
                
            print(f"Encrypted: {file_names[i]} → {encrypted_filename}")
        except Exception as e:
            print(f"Error encrypting {file_names[i]}: {str(e)}")


def decrypt(paths, file_names, key):
    # Ensure key is bytes
    key_bytes = key.encode('utf-8') if isinstance(key, str) else key
    
    for i, current_path in enumerate(paths):
        try:
            # Extract directory and filename components
            directory = os.path.dirname(current_path)
            filename = os.path.basename(current_path)
            base, ext = os.path.splitext(filename)
            
            # Create encrypted filename path
            encrypted_filename = f"{base}_encrypted{ext}"
            encrypted_path = os.path.join(directory, encrypted_filename)
            
            # Check if encrypted file exists
            if not os.path.exists(encrypted_path):
                print(f"Encrypted file not found: {encrypted_filename}")
                continue
                
            # Read the encrypted file
            with open(encrypted_path, 'rb') as f:
                encrypted_data = f.read()
                
            # Extract nonce and encrypted data
            nonce = encrypted_data[:8]  # Salsa20 uses 8-byte nonce
            ciphertext = encrypted_data[8:]
            
            # Create cipher object and decrypt
            cipher = Salsa20.new(key=key_bytes, nonce=nonce)
            decrypted_data = cipher.decrypt(ciphertext)
            
            # Create decrypted filename (preserving extension)
            decrypted_filename = f"{base}_decrypted{ext}"
            decrypted_path = os.path.join(directory, decrypted_filename)
            
            # Write the decrypted data
            with open(decrypted_path, 'wb') as f:
                f.write(decrypted_data)
                
            print(f"Decrypted: {encrypted_filename} → {decrypted_filename}")
        except Exception as e:
            print(f"Error decrypting {file_names[i]}: {str(e)}")

def main():
    paths_files = [
        './0_starting/subject/0_starting.pdf',
        './1_array/subject/1_array.pdf',
        './1_array/subject/animal.jpeg',
        './1_array/subject/landscape.jpg',
        './2_datatable/subject/2_datatable.pdf',
        './2_datatable/subject/income_per_person_gdppercapita_ppp_inflation_adjusted.csv',
        './2_datatable/subject/life_expectancy_years.csv',
        './2_datatable/subject/population_total.csv',
        './3_oop/subject/3_oop.pdf',
        './4_dod/subject/4_dod.pdf'
    ]

    # Files names
    file_names = [x[x.rfind('/') + 1:] for x in paths_files]
    # print(F)

    print("Enter `e` to encrypt, `d` to decrypt files :")
    
    x = ''
    valid_choice = ['e', 'd']

    while x not in valid_choice:
        x = input("Choice: ").lower().strip()
    
    key = input("Enter your key (must be 32 characters long): ").strip()
    
    # Ensure key is correct length (32 bytes)
    key_bytes = key.encode('utf-8')
    if len(key_bytes) < 32:
        # Pad the key to 32 bytes by repeating it
        key_bytes = (key_bytes * ((32 // len(key_bytes)) + 1))[:32]
    else:
        # Take the first 32 bytes
        key_bytes = key_bytes[:32]

    if x == 'e':
        encrypt(paths_files, file_names, key_bytes)
    else:
        decrypt(paths_files, file_names, key_bytes)


if __name__ == "__main__":
    main()