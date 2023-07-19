import sys, os
import saludador.launcher.__version__ as __version__
import saludador.modules.files as files

from termcolor import colored

def main():
    print("[", colored("Iniciando GnuPG", "green"), f"] ver: {__version__}")
    # files.read_file("resources/textos/archivo.txt")

     
if __name__ == "__main__":
    sys.exit(main())
