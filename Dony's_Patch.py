import os
import binascii

while True:
    path = os.path.dirname(os.path.abspath(__file__))

# Get a list of all BIN files in the folder
    files = [f for f in os.listdir(path) if f.endswith('.bin')]

# Display the remaining BIN files to the user
    print("Select a BIN file to work on:")
    for i, file in enumerate(files):
        print(f"{i+1}. {file}")

# Prompt the user to select a file
    selected_file = files[int(input("Enter the number of the file you want to work on: "))-1]
    print(f"You selected: {selected_file}")

#prefix the file name with the original file name
    backup_file = os.path.splitext(selected_file)[0]+"_backup.bin"

# Create the "Backup" directory if it doesn't exist
    backup_directory = os.path.join(path, "Backup")
    if not os.path.exists(backup_directory):
        os.makedirs(backup_directory)

# Build the path to the backup file in the "Backup" directory
    backup_file = os.path.join(backup_directory, os.path.splitext(selected_file)[0]+"_backup.bin")

# Create a backup of the selected file
    with open(selected_file, "rb") as original, open(backup_file, "wb") as backup:
        backup.write(original.read())

# Open the selected file for reading
    with open(selected_file, "rb") as original:
    # Read the entire contents of the selected file
        original_data = original.read()

# Display current hex values of offsets
    offset1 = 0x001c9310
    offset2 = 0x001cc310
    current_value1 = original_data[offset1:offset1+16]
    current_value2 = original_data[offset2:offset2+16]
    print()
    print("Current value of offset 001c9310 in hex:", current_value1.hex())
    print("Current value of offset 001cc310 in hex:", current_value2.hex())

# Check UART status
    print()
    if current_value1.hex() == "ffffffffffffffffffffffffffffff01":
        print("             Uart Flag 1: Enabled")
    else:
        print("             Uart Flag 1: Uart Disabled")
    if current_value2.hex() == "ffffffffffffffffffffffffffffff01":
        print("             Uart Flag 2: Enabled")
    else:
        print("             Uart Flag 2: Uart Disabled")
        
 # Prompt user for option
    option = input("1. Patch\n2. Exit\nEnter option: ")
    if option == "1":
 # Replace the specified offsets with new hex values
        new_value1 = bytes.fromhex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF01")
        new_value2 = bytes.fromhex("FFFFFFFFFFFFFFFFFFFFFFFFFFFFFF01")
        patched_data = original_data[:offset1] + new_value1 + original_data[offset1+len(new_value1):offset2] + new_value2 + original_data[offset2+len(new_value2):]

 # Write the patched data to Original.bin
        with open(os.path.splitext(selected_file)[0]+"_Patched.bin", "wb") as original:
            original.write(patched_data)

 # Display new values
        current_value1 = patched_data[offset1:offset1+16]
        current_value2 = patched_data[offset2:offset2+16]
        print("\nOLD")
        print("Offset: 001c9310, Original value in hex:", binascii.hexlify(original_data[offset1:offset1+16]))
        print("Offset: 001cc310, Original value in hex:", binascii.hexlify(original_data[offset2:offset2+16]))
        print("\nNEW")
        print("Offset: 001c9310, Current value in hex:", binascii.hexlify(current_value1))
        print("Offset: 001cc310, Current value in hex:", binascii.hexlify(current_value2))
        input("\nPress any key to exit.")
    else:
        print("Invalid option.")
