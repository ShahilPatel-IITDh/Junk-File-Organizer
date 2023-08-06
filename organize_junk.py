import os
from pathlib import Path

# Define the categories of files and their corresponding file extensions
DIRECTORIES = {
    "HTML": [".html5", ".html", ".htm", ".xhtml"],

    "JAVASCRIPT": [".js", ".jsx", ".mjs"], 

    "IMAGES": [".jpeg", ".jpg", ".tiff", ".gif", ".bmp", ".png", ".bpg", "svg",
               ".heif", ".psd"],

    "VIDEOS": [".avi", ".flv", ".wmv", ".mov", ".mp4", ".webm", ".vob", ".mng",
               ".qt", ".mpg", ".mpeg", ".3gp"],

    "DOCUMENTS": [".oxps", ".epub", ".pages", ".docx", ".doc", ".fdf", ".ods",
                  ".odt", ".pwi", ".xsn", ".xps", ".dotx", ".docm", ".dox",
                  ".rvg", ".rtf", ".rtfd", ".wpd", ".xls", ".xlsx", ".ppt",
                  "pptx"],

    "ARCHIVES": [".a", ".ar", ".cpio", ".iso", ".tar", ".gz", ".rz", ".7z",
                 ".dmg", ".rar", ".xar", ".zip"],

    "AUDIO": [".aac", ".aa", ".aac", ".dvf", ".m4a", ".m4b", ".m4p", ".mp3",
              ".msv", "ogg", "oga", ".raw", ".vox", ".wav", ".wma"],

    "PLAINTEXT": [".txt", ".in", ".out"],

    "PDF": [".pdf"],

    "PYTHON": [".py"],

    "XML": [".xml"],

    "EXE": [".exe"],

    "SHELL": [".sh"]
}

# Create a mapping of file extensions to their respective categories
FILE_FORMATS = {file_format: directory for directory, file_formats in DIRECTORIES.items()
                for file_format in file_formats}

def organize_junk(folder_path):
    """
    Organizes files in the specified folder based on their file extensions.

    Parameters:
        folder_path (str): The path of the folder to organize.
    """
    folder_path = Path(folder_path)
    for entry in os.scandir(folder_path):
        if entry.is_dir():
            continue

        file_path = Path(entry)
        file_format = file_path.suffix.lower()  # Retrieve the file extension in lowercase

        if file_format in FILE_FORMATS:
            directory_path = folder_path / FILE_FORMATS[file_format]
            directory_path.mkdir(exist_ok=True)  # Create the target directory if it doesn't exist
            file_path.rename(directory_path / file_path.name)  # Move the file to the appropriate directory

    for dir in os.scandir(folder_path):
        try:
            os.rmdir(dir)  # Attempt to remove any empty directories
        except:
            pass

def search_and_organize(folder_name):
    """
    Searches for the specified folder in the user's home directory and applies the organize_junk logic.

    Parameters:
        folder_name (str): The name of the folder to search and organize.
    """
    home_dir = Path.home()
    found_folders = [folder for folder in home_dir.glob("**/" + folder_name) if folder.is_dir()]

    if not found_folders:
        print(f"Folder '{folder_name}' not found.")
        return

    for folder in found_folders:
        print(f"Found folder: {folder}")
        organize_junk(folder)

if __name__ == "__main__":
    folder_name = input("Enter the folder name to search and organize: ")
    search_and_organize(folder_name)
    print("Files Organized!")