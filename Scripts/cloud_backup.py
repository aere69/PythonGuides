from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def backup_to_google_drive(file_path):
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)
    file = drive.CreateFile({'title': 'backup_file.txt'})
    file.Upload()
    print("Backup uploaded successfully!")

file = '/path/to/your/file.txt' 
backup_to_google_drive(file)