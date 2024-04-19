# 📁 Folder Organizer
This Python script organizes files within a folder by sorting them into specific categories like images, videos, audio files, documents, and more. It uses the 'os' and 'shutil' libraries to interact with the file system and rearrange files within the input folder based on their file extensions.

## 🛠️ How It Works
The script scans a specified folder ('input_folder') and identifies the type of each file by its extension. It then organizes these files into respective subfolders within the same 'input_folder'.
## 📂 Supported File Types
Currently, the script categorizes files based on their extensions into the following categories:

• 🖼️ Images Files (.jpg, .png, .gif, .bmp, etc.)                                                                             
• 🎥 Videos Files (.mp4, .avi, .mov, .mkv, etc.)                                                                             
• 🎵 Audio Files(.mp3, .wav, .m4a, .ogg, etc.)                                                                             
• 📄 Documents Files (.pdf, .docx, .csv, .pptx, etc.)                                                                        
• 💻 Code Files (.py, .java, .cpp, .js, .html, .css, etc.)                                                                   
• 📊 Data Files (.txt, .json, .db, .sql, etc.)                                                                             
• 🗃️ Archives Files (.zip, .rar, .tar.gz, .7z, etc.)                                                                         
• 📦 Others Files (Backup Files, Font Files, Excecutable Files, System/Config Files)                                   

## 🧰 Requirements
• Python 3.x                                                                                                                 
• os library (comes with Python)                                                                                             
• shutil library (comes with Python)
## 🚀 How to Use
1. Clone this repository to your local machine:
```bash
git clone https://github.com/IamRudraPatel/Folder-Organizer
```
2. Navigate to the project directory:
```bash
cd Folder-Organizer
```
3. Run the script:
```bash
python FolderOrganizer.py
```
4. Type/Paste path of your folder which you want to sort.

## 🎨 Customization
Feel free to modify the script to support additional file types or customize the folder structure according to your needs.
## ℹ️ Note
• Make sure to provide the correct path to your desired folder.                                                              
• The script will create subfolders within the 'input_folder' and organize files accordingly.
## 🙌 Contributors
• Rudra Patel
## 📝 License
This project is licensed under the [MIT](https://choosealicense.com/licenses/mit/) License. Feel free to use, modify, and distribute this code for any purpose.

Thank you for using Folder Organizer! 📁🔖
