# File Organizer with UI

This project is a simple file organizer with a graphical user interface (GUI) built using Python's `tkinter` library. It helps to organize files in a directory by categorizing them into predefined categories based on their file extensions.

## Features

- **File Type Categorization**: Categorizes files into images, videos, music, archives, setup files, and various types of documents.
- **Graphical User Interface**: Easy-to-use GUI for selecting folders and organizing files.
- **Customizable**: The file types and categories can be easily customized.

## File Types Supported

- **Images**: `.jpg`, `.jpeg`, `.png`, `.gif`, `.dng`
- **Videos**: `.mov`, `.mp4`, `.avi`, `.mkv`, `.wmv`
- **Music**: `.mp3`, `.wav`, `.aac`
- **Archives**: `.rar`, `.zip`, `.7z`, `.zipx`
- **Setup**: `.exe`, `.msi`
- **Documents**:
  - **Word**: `.docx`
  - **PowerPoint**: `.pptx`
  - **PDF**: `.pdf`

## Getting Started

### Prerequisites

Make sure you have Python installed on your system. This project uses the `tkinter` library which is included with standard Python installations.

### Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/your-repo-name.git
    ```

2. Navigate to the project directory:

    ```sh
    cd your-repo-name
    ```

3. Install the required packages (if any):

    ```sh
    pip install -r requirements.txt
    ```

### Running the Application

Run the Python script to start the application:

```sh
python file_organizery_with_ui.py
```

## Usage

1. Click on the "Select Folder" button to choose the directory you want to organize.
2. The script will scan the top-level items in the selected folder.
3. Files will be categorized based on their extensions and moved to corresponding subfolders.

## Customization

You can customize the file categories and extensions by modifying the `file_types` dictionary in the script.

```python
file_types = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.dng'],
    'Videos': ['.mov', '.mp4', '.avi', '.mkv', '.wmv'],
    'Music': ['.mp3', '.wav', '.aac'],
    'Archives': ['.rar', '.zip', '.7z', '.zipx'],
    'Setup': ['.exe', '.msi'],
    'Documents': {
        'Word': ['.docx'],
        'PowerPoint': ['.pptx'],
        'PDF': ['.pdf'],
    }
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Acknowledgements

- This project uses the `tkinter` library for the GUI.
- Inspired by various file organization tools available online.
