import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

# Define file types 
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.dng'],
    'Videos': ['.mov', '.mp4', '.avi', '.mkv', '.wmv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.rar', '.zip', '.7z', '.zipx'],
    'Setup': ['.exe', '.msi'],
    'Documents': {
        'Word': ['.docx'],
        'Powerpoint': ['.pptx'],
        'PDF': ['.pdf'],
    }
}

# Selecting folder
def select_folder():
    folder_path = filedialog.askdirectory()
    return folder_path

# Scanning top level items only
def scan_top_level_items(folder_path):
    top_level_items = []
    with os.scandir(folder_path) as entries:
        for entry in entries:
            top_level_items.append(entry.path)
    return top_level_items

# Getting category with priority handling and debugging
def get_category(path):
    if os.path.isfile(path):
        ext = os.path.splitext(path)[1]
        # Check for Setup files first
        if ext.lower() in file_types['Setup']:
            print(f"File {path} categorized as Setup")  # Debugging output
            return 'Setup', 'Setup'
        
        # Check other categories
        for category, subcategories in file_types.items():
            if isinstance(subcategories, dict):
                for subcategory, extensions in subcategories.items():
                    if ext.lower() in extensions:
                        print(f"File {path} categorized as {category}/{subcategory}")  # Debugging output
                        return category, subcategory
            else:
                if ext.lower() in subcategories:
                    print(f"File {path} categorized as {category}")  # Debugging output
                    return category, category
    elif os.path.isdir(path):
        main_category = get_folder_category(path)
        print(f"Directory {path} categorized as {main_category}")  # Debugging output
        return main_category, main_category
    print(f"File {path} categorized as Others")  # Debugging output
    return 'Others', 'Others'

# Getting folder category with debugging
def get_folder_category(folder_path):
    category_count = {category: 0 for category in file_types.keys()}
    
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            category, _ = get_category(file_path)
            if category in category_count:
                category_count[category] += 1
            print(f"File: {file_path}, Category: {category}")  # Debugging output

    main_category = max(category_count, key=category_count.get)
    
    if category_count[main_category] == 0:
        return 'Others'
    
    return main_category

# Organizing files and folders
def organize_files_folders(folder_path, items):
    for item in items:
        if item == folder_path:
            continue
        main_category, sub_category = get_category(item)
        
        main_category_path = os.path.join(folder_path, main_category)
        
        if main_category in file_types and isinstance(file_types[main_category], dict):
            if sub_category != 'Others' and sub_category != main_category:
                sub_category_path = os.path.join(main_category_path, sub_category)
                if not os.path.exists(sub_category_path):
                    os.makedirs(sub_category_path)
                destination = os.path.join(sub_category_path, os.path.basename(item))
            else:
                if not os.path.exists(main_category_path):
                    os.makedirs(main_category_path)
                destination = os.path.join(main_category_path, os.path.basename(item))
        else:
            if not os.path.exists(main_category_path):
                os.makedirs(main_category_path)
            destination = os.path.join(main_category_path, os.path.basename(item))
        
        try:
            shutil.move(item, destination)
            print(f"Moved {item} to {destination}")  # Debugging output
        except Exception as e:
            print(f'Error moving {item}: {e}')

# Organizing
def organize():
    folder_path = select_folder()
    if folder_path:
        items = scan_top_level_items(folder_path)
        organize_files_folders(folder_path, items)
        messagebox.showinfo("Success", f'Files and Folders organized in {folder_path}')
    else:
        messagebox.showwarning("No folder selected", "Please select a folder to organize.")

# UI/UX
def create_ui():
    root = tk.Tk()
    root.title("File and Folder Organizer")
    
    canvas = tk.Canvas(root, width=300, height=200)
    canvas.pack()

    label = tk.Label(root, text="Select a folder to organize:")
    canvas.create_window(150, 80, window=label)
    
    organize_button = tk.Button(root, text="Browse", command=organize)
    canvas.create_window(150, 120, window=organize_button)
    
    root.mainloop()

if __name__ == "__main__":
    create_ui()
