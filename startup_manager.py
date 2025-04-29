import winreg

def list_startup_programs():
    output = ""
    locations = [
        (winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run"),
        (winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
    ]
    for root, path in locations:
        try:
            registry = winreg.OpenKey(root, path)
            output += f"\nStartup em {path}:\n"
            for i in range(1024):
                try:
                    name, value, _ = winreg.EnumValue(registry, i)
                    output += f"{name}: {value}\n"
                except:
                    break
        except:
            continue
    return output if output else "Nenhum programa de inicialização encontrado."