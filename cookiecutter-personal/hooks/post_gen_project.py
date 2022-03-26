import os
import subprocess

MESAGE_COLOR="\x1b[34m"
RESERT_ALL="\x1b[0m"

print(f"{MESAGE_COLOR} Almost done!!")
print(f"Inicializando un git repositorio...{RESERT_ALL}")

subprocess.call(["git","init"])
subprocess.call(["git","add", "."])
subprocess.call(["git","commit","-m","Initial Commit"])

print(f"{MESAGE_COLOR} El mundo esta en tus manos{RESERT_ALL}")
