import os
import shutil

# Define the file types and their corresponding folders
FILE_TYPES = {
    "Images": [".jpeg", ".jpg", ".png", ".gif", ".bmp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx", ".xlsx"],
    "Music": [".mp3", ".wav", ".flac"],
    "Archives": [".zip", ".rar", ".tar", ".gz"],
    "Others": []
}

def organize_directory(directory):
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"The directory {directory} does not exist.")
        return

    # Create folders for each file type if they don't exist
    for folder_name in FILE_TYPES.keys():
        folder_path = os.path.join(directory, folder_name)
        if not os.path.exists(folder_path):
            os.mkdir(folder_path)

    # Move files into their respective folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        if os.path.isfile(file_path):
            file_ext = os.path.splitext(filename)[1].lower()

            moved = False
            for folder_name, extensions in FILE_TYPES.items():
                if file_ext in extensions:
                    shutil.move(file_path, os.path.join(directory, folder_name, filename))
                    moved = True
                    break

            # Move files with unrecognized extensions to "Others" folder
            if not moved:
                shutil.move(file_path, os.path.join(directory, "Others", filename))

    print("Files have been organized successfully!")

if __name__ == "__main__":
    # Ask the user for the directory to organize
    target_directory = input("Enter the directory path you want to organize: ")
    
    # Call the function to organize the directory
    organize_directory(target_directory)
