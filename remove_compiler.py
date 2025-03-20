import os
import json
import glob

def remove_compiler_field(directory_path):
    """
    Removes the 'compiler' field from all JSON files in the specified directory.
    
    Args:
        directory_path (str): Path to the directory containing JSON files
    """
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, "*.json"))
    
    print(f"Found {len(json_files)} JSON files in {directory_path}")
    
    for file_path in json_files:
        try:
            # Read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            # Remove the compiler field if it exists
            if 'compiler' in data:
                del data['compiler']
                print(f"Removed 'compiler' field from {os.path.basename(file_path)}")
                
                # Write the updated JSON back to the file
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=2)
            else:
                print(f"No 'compiler' field found in {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    print("Processing complete!")

if __name__ == "__main__":
    # You can change this to the path of your metadata directory
    metadata_dir = "metadata"
    
    # Check if the directory exists
    if not os.path.isdir(metadata_dir):
        print(f"Directory '{metadata_dir}' not found. Please provide a valid directory path.")
    else:
        remove_compiler_field(metadata_dir) 