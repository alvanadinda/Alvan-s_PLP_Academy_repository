# File Read & Write Challenge

def read_and_modify_file():
    try:
        filename = input("Enter the filename to read: ").strip()
        with open(filename, 'r') as file:
            content = file.read()
        
        modified_content = content.lower()  # Modify content (example: convert to lowercase)
        
        new_filename = "modified_" + filename
        with open(new_filename, 'w') as file:
            file.write(modified_content)
        
        print(f"Modified content written to {new_filename}")
    
    except FileNotFoundError:
        print("Error: File not found. Please check the filename and try again.")
    except IOError:
        print("Error: Unable to read the file. Check file permissions.")

if __name__ == "__main__":
    read_and_modify_file()
