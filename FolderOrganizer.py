# importing important libraries
import os
from shutil import move

# Defining Global Variable
NewDir = input("Enter Directory Name: ")
os.chdir(NewDir)
    
''' file types which are supported to sort '''
# supported image files types
image_extensions = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", 
                    ".raw", ".arw", ".cr2", ".nrw", ".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", 
                    ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# supported Video files types
video_extensions = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",
                    ".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# supported Audio files types
audio_extensions = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# supported Document files types
document_extensions = [".doc", ".docx", ".odt", ".pdf", ".xls", ".xlsx", ".ppt", ".pptx", ".csv", ".rtf"]
# supported code types
code_extensions = [".py", ".c", ".cpp", ".java", ".cs", ".js", ".ts", ".php", ".html", ".css",".scss", 
                   ".swift", ".kt", ".rb", ".go", ".rust", ".lua", ".pl", ".asm", ".sh", ".bat", ".md"]
# supported archive and compressed files
archive_extensions = [".zip", ".rar", ".tar", ".gz", ".bz2", ".7z", ".xz", ".lz", ".lzma", ".Z", ".iso"]
# supported data files
data_extensions = [".json", ".xml", ".yaml", ".db", ".sql", ".txt", ".sqlite"]
# supported backup files
backup_extensions = ['.bak', '.backup']
# supported fonts files
font_extensions = ['.ttf', '.otf', '.woff', '.woff2']
# supported executables files
excecutable_extensions = ['.exe', '.dmg', '.app', '.deb', '.rpm']
# supported system and config files
sysConfig_extensions = ['.ini', '.cfg', '.conf']

def create_folder(type):
    os.mkdir(f'{type} Files')

def make_unique(fileType, file):
    filename, extension = os.path.splitext(file)
    count = 1
    while os.path.exists(f'{NewDir}/{fileType}/{file}'):
        file = f"{filename}{str(count)}{extension}"
        count+=1
    return file
        
def image_files(file):
    newName = make_unique('Image Files', file)
    os.rename(file, newName)
    move(newName,"Image Files")

def video_files(file):
    newName = make_unique('Video Files', file)
    os.rename(file, newName)
    move(newName,"Video Files")

def audio_files(file):
    newName = make_unique('Audio Files', file)
    os.rename(file, newName)
    move(newName,"Audio Files")

def document_files(file):
    newName = make_unique('Document Files', file)
    os.rename(file, newName)
    move(newName,"Document Files")

def code_files(file):
    newName = make_unique('Code Files', file)
    os.rename(file, newName)
    move(newName,"Code Files")

def archive_files(file):
    newName = make_unique('Compressed Files', file)
    os.rename(file, newName)
    move(newName,"Compressed Files")
    
def data_files(file):
    newName = make_unique('Data Files', file)
    os.rename(file, newName)
    move(newName,"Data Files")

def backup_files(file):
    newName = make_unique('Backup Files', file)
    os.rename(file, newName)
    move(newName,"Backup Files")

def font_files(file):
    newName = make_unique('Font Files', file)
    os.rename(file, newName)
    move(newName,"Font Files")

def excecutable_files(file):
    newName = make_unique('Excecutables Files', file)
    os.rename(file, newName)
    move(newName,"Ececutables Files")

def sysConfig_files(file):
    newName = make_unique('SysConfig Files', file)
    os.rename(file, newName)
    move(newName,"SysConfig Files")

def other_files(file):
    newName = make_unique('Other Files', file)
    os.rename(file, newName)
    move(newName,"Other Files")

def mainController():
    for files in os.listdir():
        name, ext = os.path.splitext(files)
        # Handling Folders
        if ext == '':
            continue 
        
        # Handling Image Files
        if ext in image_extensions:
            if not os.path.exists("Image Files"):
                create_folder("Image")
            image_files(files)
        
        # Handling Video Files
        elif ext in video_extensions:
            if not os.path.exists("Video Files"):
                create_folder("Video")
            video_files(files)
            
        # Handling Audio Files
        elif ext in audio_extensions:
            if not os.path.exists("Audio Files"):
                create_folder("Audio")
            audio_files(files)
            
        # Handling Document Files
        elif ext in document_extensions:
            if not os.path.exists("Document Files"):
                create_folder("Document")
            document_files(files)
        
        # Handling Code Files
        elif ext in code_extensions:
            if not os.path.exists("Code Files"):
                create_folder("Code")
            code_files(files)
            
        # Handling Archive Files
        elif ext in archive_extensions:
            if not os.path.exists("Compressed Files"):
                create_folder("Compressed")
            archive_files(files)
            
        # Handling Data Files
        elif ext in data_extensions:
            if not os.path.exists("Data Files"):
                create_folder("Data")
            data_files(files)
            
        # Handling Backup Files
        elif ext in backup_extensions:
            if not os.path.exists("Backup Files"):
                create_folder("Backup")
            backup_files(files)
            
        # Handling Font Files
        elif ext in font_extensions:
            if not os.path.exists("Fonts Files"):
                create_folder("Fonts")
            font_files(files)
            
        # Handling Excecutable Files
        elif ext in excecutable_extensions:
            if not os.path.exists("Excecutable Files"):
                create_folder("Excecutable")
            excecutable_files(files)
            
        # Handling System/Config Files
        elif ext in sysConfig_extensions:
            if not os.path.exists("SysConfig Files"):
                create_folder("SysConfig")
            sysConfig_files(files)
            
        # Handling Other Files
        else:
            if not os.path.exists("Other Files"):
                create_folder("Other")
            other_files(files)

# Driver Code        
if __name__=='__main__':
    mainController()