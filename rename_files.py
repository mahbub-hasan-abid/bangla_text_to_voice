import os

# 🔧 Change this to your folder path
folder_path = r"F:\BdApps\audios\sorborno"

# Get list of files in the folder
files = sorted(os.listdir(folder_path))

# Filter out only files (ignore folders)
files = [f for f in files if os.path.isfile(os.path.join(folder_path, f))]

# Rename files to 1.ext, 2.ext, ...
for i, filename in enumerate(files, start=1):
    old_path = os.path.join(folder_path, filename)
    extension = os.path.splitext(filename)[1]
    new_filename = f"{i}{extension}"
    new_path = os.path.join(folder_path, new_filename)
    os.rename(old_path, new_path)

print("✅ All files renamed successfully!")
