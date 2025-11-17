
import shutil
import os

def save_upload_file(upload_file, destination_folder="app/temp"):
    os.makedirs(destination_folder, exist_ok=True)
    file_path = os.path.join(destination_folder, upload_file.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(upload_file.file, buffer)
    return file_path
