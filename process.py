import glob
import os
import shutil

inputs = glob.glob("inputs/*")

os.makedirs("outputs",exist_ok=True)

for filepath in inputs:
    output_path = filepath.replace("inputs","outputs")
    shutil.copyfile(filepath,output_path)
    print(filepath)

