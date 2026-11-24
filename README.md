# File Organizer

A beginner-friendly Python script that organizes files into folders based on their file extensions.

## Features

- Organizes files into folders by extension (such as `.rtf`, `.pdf`, or `.jpg`)
- Checks whether the entered folder path is valid
- Skips hidden files, such as `.DS_Store`
- Skips files without extensions
- Avoids overwriting files with the same name
- Displays messages showing which files were moved or skipped

## How to Use

1. Make sure Python 3 is installed.
2. Download or clone this repository.
3. Open a terminal in the project folder.
4. Run:

   ```bash
   python3 file_organizer.py
   ```

5. Enter the full path of the folder you want to organize.

**Important:** Test the script on a practice folder first. It moves files into subfolders, so your original folder structure will change.

## Technologies

- Python 3
- Python standard libraries: `os` and `shutil`

## About This Project

I built this project to practise Python fundamentals, file handling, loops, conditions, and basic error prevention.

## Example

Before organizing:

- notes.rtf
- report.rtf
- photo.jpg

After organizing:

- rtf/
  - notes.rtf
  - report.rtf
- jpg/
  - photo.jpg
