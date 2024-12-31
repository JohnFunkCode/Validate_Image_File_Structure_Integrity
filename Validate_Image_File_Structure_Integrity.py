import os
from PIL import Image

Image.MAX_IMAGE_PIXELS = 500000000 # Largest file observed so far is 432,889,600
progress_counter = 0
progress_interval = 100

def validate_image_files_recursive(directory):
    """
    Recursively validate the structure of JPG files in a directory and its subdirectories.

    :param directory: Path to the root directory.
    """
    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist.")
        return

    valid_files = []
    invalid_files = []

    # Walk through the directory recursively
    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # if file_name.lower().endswith('.jpg') or file_name.lower().endswith('.jpeg'):
            if file_name.lower().endswith(('.jpg', '.jpeg', '.gif', '.tiff')):
                show_progress()
                try:
                    with Image.open(file_path) as img:
                        img.verify()  # Verify the file integrity
                    valid_files.append(file_path)
                except Exception as e:
                    invalid_files.append((file_path, str(e)))

    print(f"\nValidation complete for files under '{directory}'")
    print(f"Valid JPG files: {len(valid_files)}")
    for valid in valid_files:
        print(f"  - {valid}")

    print(f"Invalid JPG files: {len(invalid_files)}")
    for invalid, error in invalid_files:
        print(f"  - {invalid}: {error}")


def show_progress():
    global progress_counter
    progress_counter += 1
    if progress_counter % progress_interval == 0:
        print(".", end="")

# Set the directory path to validate
#directory_path = "/Volume/Directory/Subdirectory"
#directory_path = "/Volumes/T9/WWII Photo Catalog/Photos"
directory_path = "/Volumes/Photos/DadsPhotos"


if __name__ == "__main__":
    print(f"Validating image files in '{directory_path}' and its subdirectories")
    validate_image_files_recursive(directory_path)