
import os
import sys

proyect_slug = "{{cookiecutter.proyect_slug}}"

ERROR_COLOR = "\x1b[31m" 
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"

if proyect_slug.startswith("x"):
    print(f"{ERROR_COLOR}ERROR: {proyect_slug} no es un nombre valido para este proyecto.{RESET_ALL}")
    sys.exit(1)
print(f"{MESSAGE_COLOR} Excelente!!!")
print(f"Creando proyecto con {os.getcwd()}{RESET_ALL}")