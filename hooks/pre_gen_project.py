# Librarys
import os
import sys
from cookiecutter.main import cookiecutter


# Terminal colors
ERROR_COLOR = "\x1b[31m"
MESSAGE_COLOR = "\x1b[34m"
RESET_ALL = "\x1b[0m"


select = {{ cookiecutter.ramo }}


ramos = {
    "MAT033": {
        "name_class": "Metodos cuantitativos para los negocios",
        "teacher": "Francisca Gonzalez"
    }}


if select not in ramos:
    print(f"{ERROR_COLOR}ERROR: {select} no hay información de ese ramo {RESET_ALL}")
    sys.exit(1)

cookiecutter('cookiecutter-pypackage/',
             extra_context={'name_class': ramos[select]["name_class"], 'teacher': ramos[select]["teacher"]})


print(f"{MESSAGE_COLOR} Plantilla creada!")
print(f"Ubicada dentro de: {os.getcwd()}{RESET_ALL} ")
