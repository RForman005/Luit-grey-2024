import os  # Import the os module to interact with the file system

# Create an empty list to store file details
file_details = []

# Get the list of files in the current directory using os.listdir()
# The '.' indicates the current directory
for file_name in os.listdir(): 

# Check if the item is a file (not a directory)
    if os.path.isfile(file_name):  
        
# Get the size of the file in bytes using os.path.getsize()
        file_size = os.path.getsize(file_name)
        
# Append the file details as a dictionary to the list
        file_details.append({'name': file_name, 'size': file_size})

# Print the list of dictionaries to verify the output
print(file_details)