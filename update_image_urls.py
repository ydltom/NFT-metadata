import os
import json
import glob

def update_image_urls(directory_path, base_url):
    """
    Updates the 'image' field in all JSON files in the specified directory
    to use the provided base URL plus the filename.
    
    Args:
        directory_path (str): Path to the directory containing JSON files
        base_url (str): Base URL to prepend to the image filename
    """
    # Find all JSON files in the directory
    json_files = glob.glob(os.path.join(directory_path, "*.json"))
    
    print(f"Found {len(json_files)} JSON files in {directory_path}")
    
    for file_path in json_files:
        try:
            # Extract the file number from the filename (e.g., "10.json" -> "10")
            file_number = os.path.splitext(os.path.basename(file_path))[0]
            
            # Construct the new image URL
            new_image_url = f"{base_url}{file_number}.png"
            
            # Read the JSON file
            with open(file_path, 'r') as file:
                data = json.load(file)
            
            # Update the image field
            if 'image' in data:
                old_image = data['image']
                data['image'] = new_image_url
                print(f"Updated {os.path.basename(file_path)}: {old_image} -> {new_image_url}")
                
                # Also update the URI in the properties.files array if it exists
                if 'properties' in data and 'files' in data['properties'] and len(data['properties']['files']) > 0:
                    for file_obj in data['properties']['files']:
                        if 'uri' in file_obj and file_obj['uri'].endswith('.png'):
                            file_obj['uri'] = f"{file_number}.png"
                
                # Write the updated JSON back to the file
                with open(file_path, 'w') as file:
                    json.dump(data, file, indent=2)
            else:
                print(f"No 'image' field found in {os.path.basename(file_path)}")
                
        except Exception as e:
            print(f"Error processing {file_path}: {str(e)}")
    
    print("Processing complete!")

if __name__ == "__main__":
    # Directory containing the metadata JSON files
    metadata_dir = "metadata"
    
    # Base URL for the images
    base_url = "https://ydltom.github.io/NFT-metadata/images/"
    
    # Check if the directory exists
    if not os.path.isdir(metadata_dir):
        print(f"Directory '{metadata_dir}' not found. Please provide a valid directory path.")
    else:
        update_image_urls(metadata_dir, base_url) 