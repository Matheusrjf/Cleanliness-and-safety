import os
import shutil
import tempfile

def clean_temp():
    temp_dir = tempfile.gettempdir()
    for root, dirs, files in os.walk(temp_dir):
        for f in files:
            try:
                os.remove(os.path.join(root, f))
            except:
                pass
        for d in dirs:
            try:
                shutil.rmtree(os.path.join(root, d), ignore_errors=True)
            except:
                pass
    print("Arquivos temporários limpos.")