import pkg_resources
import subprocess
import os
import time


# Check if watchdog is installed
try:
    pkg_resources.get_distribution('watchdog')
except pkg_resources.DistributionNotFound:
    # Install watchdog from the packaged .whl file
    libs_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "libs")
    watchdog_whl = [file for file in os.listdir(libs_path) if file.startswith("watchdog") and file.endswith(".whl")][0]
    subprocess.call([f"{os.sys.executable}", "-m", "pip", "install", os.path.join(libs_path, watchdog_whl)])

# Other imports (like those specific to your PDF monitoring and printing logic)
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# ... [rest of the imports and watchdog installation code]

# Define the directory where PDFs will be saved
WATCH_DIRECTORY = r"C:\Users\danie\OneDrive\Documents\pdfTestFolder"  # Directory to watch
FILE_EXTENSION = ".pdf"
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PDF_PRINTER_PATH = os.path.join(BASE_DIR, "PDFtoPrinter.exe")  # Path to your PDFtoPrinter.exe

class FileHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        elif event.src_path.endswith(FILE_EXTENSION):
            print(f"Detected a new PDF: {event.src_path}")
            print(f"Attempting to print using: {PDF_PRINTER_PATH}")

            try:
                result = subprocess.run([PDF_PRINTER_PATH, event.src_path], check=True, capture_output=True, text=True)
                print(f"Print command output: {result.stdout}")
            except subprocess.CalledProcessError as e:
                print(f"Print command failed with error: {e}")
                print(f"Error output: {e.stderr}")

            print(f"Print command sent for: {event.src_path}")


if __name__ == "__main__":
    print(f"Starting watchdog to monitor: {WATCH_DIRECTORY}")
    event_handler = FileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=WATCH_DIRECTORY, recursive=False)
    observer.start()

    print("Press Ctrl+C to exit...")
    
    try:
        while True:
            time.sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    
    observer.join()
    print("Exiting program.")
