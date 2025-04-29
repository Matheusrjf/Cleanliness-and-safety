import os

def secure_delete(file_path, passes=3):
    if os.path.isfile(file_path):
        length = os.path.getsize(file_path)
        with open(file_path, "ba+", buffering=0) as delfile:
            for _ in range(passes):
                delfile.seek(0)
                delfile.write(os.urandom(length))
        os.remove(file_path)
        print(f"{file_path} deletado com segurança.")
    else:
        print(f"{file_path} não encontrado.")