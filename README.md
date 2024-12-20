

# File Organizer Script

This script organizes files in a specified folder by moving them into subfolders based on their file extensions. It's a convenient way to clean up and categorize files in a directory.

## Features
- Automatically detects file extensions.
- Creates a folder for each file type (e.g., `.txt`, `.jpg`, `.pdf`) if it doesn't already exist.
- Moves files into corresponding folders based on their extensions.
- Skips files without extensions to avoid errors.

## Prerequisites
- Python 3.6 or higher
- A directory with files to organize

## How to Use
1. Clone this repository or copy the script into a local file.
2. Ensure Python is installed on your system.
3. Run the script:
   ```bash
   python file_organizer.py
   ```
4. Enter the full path of the folder you want to organize when prompted.

### Example
If your folder structure starts as:
```
C:\Users\marti\Downloads\
    file1.txt
    image1.jpg
    document1.pdf
    script.py
```
After running the script, it will be organized as:
```
C:\Users\marti\Downloads\
    txt\
        file1.txt
    jpg\
        image1.jpg
    pdf\
        document1.pdf
    py\
        script.py
```

## Error Handling
- If you input an invalid path, the script will throw an error. Ensure the path exists and is accessible.
- Files without extensions are ignored and left in the original folder.

## Customization
You can modify the script to:
- Handle files without extensions.
- Use a custom folder structure.
- Exclude specific file types.

## Troubleshooting
- **WinError 123**: Ensure no leading or trailing spaces are in the path you input.
- **FileNotFoundError**: Verify the specified folder exists.

## License
This script is open-source and free to use. Contributions and suggestions are welcome.

