from google.colab import drive # IMPORTANT: To run this code properly, you must execute it in Google Colab.
drive.mount('/content/drive')
import os, shutil, datetime

def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"📁 Folder created: {path}")

def move_file(file_path, dest_folder):
    try:
        shutil.move(file_path, dest_folder)
        print(f"✅ '{os.path.basename(file_path)}' moved to '{dest_folder}'")
    except Exception as e:
        print(f"❌ Error while moving '{file_path}': {e}")

def identify_type(file_name):
    file_type = file_name.lower()
    if any(file_type.endswith(ext) for ext in ['jpg', 'jpeg', 'png', 'gif']): return 'Images'
    elif any(file_type.endswith(ext) for ext in ['pdf', 'docx', 'doc', 'txt', 'xlsx', 'xls', 'gdoc', 'gsheet', 'gslides']): return 'Documents'
    elif any(file_type.endswith(ext) for ext in ['mp4', 'mov', 'avi']): return 'Videos'
    elif any(file_type.endswith(ext) for ext in ['mp3', 'wav']): return 'Music'
    else:
        return 'Others'

def organize_by_type(path):
    for root, _, files in os.walk(path):
        if any(root.endswith(p) for p in ['Images', 'Documents', 'Videos', 'Music', 'Others']): continue
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                file_type = identify_type(file)
                destination = os.path.join(path, file_type)
                create_folder(destination)
                move_file(full_path, destination)

def classify_size(size_bytes):
    mb = size_bytes / (1024 * 1024)
    if mb < 1: return 'Small'
    elif mb < 10: return 'Medium'
    elif mb < 100: return 'Large'
    else:
        return 'Huge'

def organize_by_size(path):
    for root, _, files in os.walk(path):
        if any(root.endswith(p) for p in ['Small', 'Medium', 'Large', 'Huge']): continue
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                size_category = classify_size(os.path.getsize(full_path))
                destination = os.path.join(path, size_category)
                create_folder(destination)
                move_file(full_path, destination)

def get_date_folder(full_path):
    modified_at = datetime.datetime.fromtimestamp(os.path.getmtime(full_path))
    return modified_at.strftime('%Y-%m')

def organize_by_date(path):
    for root, _, files in os.walk(path):
        if any(len(folder) == 7 and folder[4] == '-' for folder in root.split(os.sep)): continue
        for file in files:
            full_path = os.path.join(root, file)
            if os.path.isfile(full_path):
                date_folder = get_date_folder(full_path)
                destination = os.path.join(path, date_folder)
                create_folder(destination)
                move_file(full_path, destination)

def organize_by_keyword(path, keywords):
    # IMPORTANT: Ensure that 'keywords' list is not empty and contains relevant keywords
    # for the code to correctly categorize files based on their names.
    for root, _, files in os.walk(path):
        if any(root.endswith(palavra) for palavra in keywords) or root.endswith("Others"): continue
        for file in files:
            name = file.lower()
            full_path = os.path.join(root, file)
            if not os.path.isfile(full_path): continue
            found = False
            for keyword in keywords:
                if keyword.lower() in name:
                    destination = os.path.join(path, keyword)
                    create_folder(destination)
                    move_file(full_path, destination)
                    found = True
                    break
            if not found:
                destination = os.path.join(path, "Others")
                create_folder(destination)
                move_file(full_path, destination)

my_drive = "/content/drive/MyDrive"
# WARNING: uncomment to execute!
# organize_by_type(my_drive)
# organize_by_size(my_drive)
# organize_by_date(my_drive)
# organize_by_keyword(my_drive, ["prova", "lista", "trabalho"])  # customizable list/lista personalizável