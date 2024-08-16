import os

def remove_zone_identifier_files(start_path):
    for root, dirs, files in os.walk(start_path):
        for file in files:
            if file.lower().endswith("zone.identifier"):
                file_path = os.path.join(root, file)
                os.remove(file_path)
                print(f"Removed: {file_path}")

# Call the function starting from the current directory
remove_zone_identifier_files('.')