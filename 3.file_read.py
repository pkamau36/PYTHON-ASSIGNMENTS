def file_read_write():
    # Ask user for input file
    filename = input("Enter the filename to read: ")

    try:
        # Try opening the file
        with open(filename, "r") as file:
            content = file.read()

        # Modify content
        modified_content = content.upper()

        # Save new version
        output_file = "modified_" + filename
        with open(output_file, "w") as file:
            file.write(modified_content)

        print(f" File was processed successfully! New file is now saved as : {output_file}")

    except FileNotFoundError:
        # The File does not exist
        print("❌ Error: The file is non-existent.")
    except PermissionError:
        #  The File exists but cannot be read (no access)
        print("❌ Error: You cannot read this file.Seek Administrator help.")

#call function
file_read_write()