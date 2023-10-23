# PDFtoPrinterWatchdog

Automatically print PDF files added to a specified directory. Built with Python using the `watchdog` library and `PDFtoPrinter.exe` utility.

## Table of Contents

- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Requirements

- Python (tested with version 3.x)
- PDFtoPrinter.exe (included in the project folder)

## Installation

1. **Clone the Repository**:  
   `git clone [Your Repository URL]`
   
2. **Using Command Prompt, Navigate to the Project Directory **:  
   `cd [Your Project Directory]`

3. **(Optional) Set Up a Virtual Environment**:  
   `python -m venv venv`  
   `source venv/bin/activate`  (On Windows, use: `venv\Scripts\activate`)

4. **Open the script and update the 'WATCH_DIRECTORY' variable to the directory path you want to monitor.
    WATCH_DIRECTORY = r"[Path_to_watch_directory]"  # Replace with your directory
   
5. **Run the Script**:  
   The script is set up to use the included `PDFtoPrinter.exe` utility by default. However, you can easily modify the script to specify a different directory to watch or use a different print utility.

## Usage

1. **From the Command Line**:  
   Navigate to the directory where the script is located and run:  
   `python PDFtoPrinterWatchdog.py`

2. **Note**: If the `watchdog` library isn't installed on your system, the script will attempt to install it during its first run. 
   After the installation, you'll need to run the script again to start monitoring the directory.
   
3. **Monitor and Print**:  
   With the script running, it will continuously monitor the specified directory. As soon as a new PDF is added to this directory, the script will detect it and send it to the printer.

## Troubleshooting

- Make sure `PDFtoPrinter.exe` is correctly located as specified in the script. If not, adjust the path in the script.
- If there's an issue with `watchdog` installation, the script will attempt to install it from a bundled `.whl` file. Ensure this file is available in the `libs` directory.
- If printing isn't working as expected, test the `PDFtoPrinter.exe` utility manually by running the following command in your command prompt (CMD):
`"[Your-directory-path]\PDFtoPrinter.exe" "[Folder-to-watch-directory-path]\file-name.pdf"`


## License

This project is under the MIT License. Check out the [LICENSE](./LICENSE) file for more details.


