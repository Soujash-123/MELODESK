import subprocess
import os
path = r"C:\Users\SOUJASH\Desktop\SYNTALIX\MACRO\Songs"
os.chdir(path)

def separate_audio(file_path, output_dir):
    command = ['spleeter', 'separate', '-p', 'spleeter:2stems', '-o', output_dir, file_path]
    print(command)
    try:
        subprocess.run(command, check=True)
        print("Audio separation completed successfully.")
        print(os.getcwd())
    except subprocess.CalledProcessError as e:
        print("Error occurred during audio separation:", e)

# Usage example
for i in list(os.listdir()):
    if ".mp3" in i or ".wav" in i:
        output_dir = 'output'
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        separate_audio(i, output_dir)
        
