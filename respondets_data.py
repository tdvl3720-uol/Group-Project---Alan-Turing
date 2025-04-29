import os

# Folder where your files are
source_folder = "data"

# Loop through files a1.txt to a25.txt
for i in range(1, 26):
    old_name = f"a{i}.txt"
    new_name = f"answers_respondent_{i}.txt"

    old_path = f"{source_folder}/{old_name}"
    new_path = f"{source_folder}/{new_name}"

    if os.path.exists(old_path):
        os.rename(old_path, new_path)
        print(f" Renamed: {old_name} → {new_name}")
    else:
        print(f" File not found: {old_name}")
