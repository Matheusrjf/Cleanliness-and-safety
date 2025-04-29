import tkinter as tk
from tkinter import filedialog, messagebox
import cleaner
import secure_delete
import startup_manager
import vulnerability_scanner

def run_cleaner():
    cleaner.clean_temp()
    messagebox.showinfo("Limpeza", "Limpeza de arquivos temporários concluída.")

def run_secure_delete():
    file_path = filedialog.askopenfilename()
    if file_path:
        secure_delete.secure_delete(file_path)

def run_startup_manager():
    output = startup_manager.list_startup_programs()
    messagebox.showinfo("Programas de Inicialização", output)

def run_vulnerability_scan():
    issues = vulnerability_scanner.scan_vulnerabilities()
    messagebox.showinfo("Vulnerabilidades", "\n".join(issues) if issues else "Nenhuma vulnerabilidade crítica encontrada.")

app = tk.Tk()
app.title("CCleaner Seguro - Python Edition")
app.geometry("400x300")

tk.Label(app, text="Ferramentas de Segurança", font=("Arial", 14)).pack(pady=10)

tk.Button(app, text="🧹 Limpeza Profunda", command=run_cleaner, width=30).pack(pady=5)
tk.Button(app, text="🗑️ Exclusão Segura de Arquivo", command=run_secure_delete, width=30).pack(pady=5)
tk.Button(app, text="⚙️ Programas de Inicialização", command=run_startup_manager, width=30).pack(pady=5)
tk.Button(app, text="🔍 Scan de Vulnerabilidades", command=run_vulnerability_scan, width=30).pack(pady=5)

app.mainloop()