import os
import shutil

def rename_files(directory, criteria):
    """
    Rename files in a directory based on certain criteria.

    Parameters:
    - directory: The directory path where the files are located.
    - criteria: A function that takes a filename as input and returns the new filename.

    Returns:
    - None
    """
    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)
        new_filename = criteria(filename)
        new_path = os.path.join(directory, new_filename)
        os.rename(old_path, new_path)

def organize_files(directory, destination_folder):
    """
    Organize files into folders based on file extensions.

    Parameters:
    - directory: The directory path where the files are located.
    - destination_folder: The directory path where the organized folders will be created.

    Returns:
    - None
    """
    for filename in os.listdir(directory):
        file_extension = os.path.splitext(filename)[1]
        if file_extension:
            folder_path = os.path.join(destination_folder, file_extension[1:].upper())
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)
            shutil.move(os.path.join(directory, filename), os.path.join(folder_path, filename))

def search_files(directory, keyword):
    """
    Search for files containing a specific keyword.

    Parameters:
    - directory: The directory path where the files are located.
    - keyword: The keyword to search for in file names.

    Returns:
    - List of filenames containing the keyword.
    """
    found_files = []
    for filename in os.listdir(directory):
        if keyword in filename:
            found_files.append(filename)
    return found_files

# Example usage:
if __name__ == "__main__":
    # Step 1: Provide a directory path containing files to be managed
    directory_path = "path/to/your/directory"

    # Step 2: Rename files in the directory based on certain criteria
    rename_files(directory_path, lambda x: x.replace(" ", "_"))  # Example: Replace spaces with underscores

    # Step 3: Organize files into folders based on file extensions
    destination_folder = "path/to/organized/folder"
    organize_files(directory_path, destination_folder)

    # Step 4: Search for specific files containing a keyword
    keyword = "important"
    found_files = search_files(directory_path, keyword)
    print("Files containing '{}' keyword: {}".format(keyword, found_files))
