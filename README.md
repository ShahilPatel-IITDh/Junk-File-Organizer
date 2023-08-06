# Junk-File-Organizer

### This Python script is designed to automatically organize files in a specified folder based on their file extensions. It categorizes files into various predefined directories corresponding to their formats, providing a clean and organized file system.

## Categories and Supported File Extensions
The script supports the following categories and their corresponding file extensions:

**HTML**: .html5, .html, .htm, .xhtml
**JavaScript**: .js, .jsx, .mjs
**Images**: .jpeg, .jpg, .tiff, .gif, .bmp, .png, .bpg, .svg, .heif, .psd
**Videos**: .avi, .flv, .wmv, .mov, .mp4, .webm, .vob, .mng, .qt, .mpg, .mpeg, .3gp
**Documents**: .oxps, .epub, .pages, .docx, .doc, .fdf, .ods, .odt, .pwi, .xsn, .xps, .dotx, .docm, .dox, .rvg, .rtf, .rtfd, .wpd, .xls, .xlsx, .ppt, .pptx
**Archives**: .a, .ar, .cpio, .iso, .tar, .gz, .rz, .7z, .dmg, .rar, .xar, .zip
**Audio**: .aac, .aa, .aac, .dvf, .m4a, .m4b, .m4p, .mp3, .msv, .ogg, .oga, .raw, .vox, .wav, .wma
**Plaintext**: .txt, .in, .out
**PDF**: .pdf
**Python**: .py
**XML**: .xml
**Executable**: .exe
**Shell Script**: .sh

### How to Use
Run the Python script *organize_junk.py*.
When prompted, enter the *name* of the folder you want to search and organize within your **home** directory.
The script will search for the specified folder and apply the organization logic to the files within that folder.
The categorized files will be moved into respective directories based on their file formats.

### Code Explanation
The script consists of two main functions:

**organize_junk(folder_path)**: Organizes files in the specified folder based on their file extensions.

**folder_path (str)**: The path of the folder to organize.

**search_and_organize(folder_name)**: Searches for the specified folder in the user's home directory and applies the organize_junk logic.

**folder_name (str)**: The name of the folder to search and organize.

The script will display a message if the specified folder is not found.

### Important Notes
This script is designed to search and organize files within a specified folder. It will not search the entire PC to minimize potential security risks.
Exercise caution when running the script, and always create backups of important data before proceeding.
Feel free to use this script to keep your files organized and decluttered! Happy organizing!
