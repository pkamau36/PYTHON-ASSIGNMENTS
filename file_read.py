def file_read_write():
    # Ask user for input file
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content (make it uppercase for demo)
        modified_content = content.upper()

        # Save new version
        output_file = "modified_" + filename
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f"✅ File processed successfully! Modified version saved as: {output_file}")

    except FileNotFoundError:
        # File does not exist
        print("❌ Error: The file is non-existent.")

    except PermissionError:
        #  File exists but cannot be read (no access)
        print("❌ Error: You cannot read this file.Seek Administrator help.")
        
#call function
file_read_write()
