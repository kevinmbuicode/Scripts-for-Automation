import os
import shutil
import zipfile
import datetime

def backup_data(source_directory, backup_directory):
    """
    Backup data from a source directory to a backup directory.

    Parameters:
    - source_directory: The directory path of the data to be backed up.
    - backup_directory: The directory path where the backup archive will be stored.

    Returns:
    - None
    """
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    backup_filename = f"backup_{timestamp}.zip"
    backup_path = os.path.join(backup_directory, backup_filename)

    # Copy source directory contents to temporary directory before archiving
    temp_directory = os.path.join(backup_directory, "temp")
    shutil.copytree(source_directory, temp_directory)

    # Create backup archive from temporary directory
    with zipfile.ZipFile(backup_path, "w") as zipf:
        for root, _, files in os.walk(temp_directory):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, temp_directory))

    # Remove temporary directory after backup
    shutil.rmtree(temp_directory)

def restore_data(backup_archive, restore_directory):
    """
    Restore data from a backup archive to a restore directory.

    Parameters:
    - backup_archive: The path of the backup archive to restore from.
    - restore_directory: The directory path where the data will be restored.

    Returns:
    - None
    """
    with zipfile.ZipFile(backup_archive, "r") as zipf:
        zipf.extractall(restore_directory)

# Example usage:
if __name__ == "__main__":
    # Step 1: Specify source and backup directories
    source_directory = "path/to/source/directory"
    backup_directory = "path/to/backup/directory"

    # Step 2: Backup data
    backup_data(source_directory, backup_directory)

    # Step 3: Restore data (optional)
    # Specify the backup archive and restore directory to restore data if needed
    # backup_archive = "path/to/backup/archive.zip"
    # restore_directory = "path/to/restore/directory"
    # restore_data(backup_archive, restore_directory)
