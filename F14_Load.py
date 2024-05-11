import argparse
import sys
import os

def load():
    parser = argparse.ArgumentParser()

    parser.add_argument('Parent_Folder', metavar = 'folder', type = str, help="Masukkan folder penyimpanan")

    args = parser.parse_args()

    folder = args.Parent_Folder

    print("Loading...")
    if not os.path.exists(folder):
        print("Folder '%s' tidak ditemukan!" %folder)
        sys.exit()
    elif not folder:
        print("Tidak ada nama folder yang diberikan!")
        sys.exit() 
    elif os.path.exists(folder):
        print("Folder ditemukan!")
        os.chdir(folder)
        print("Selamat datang di OWCA!")
    return''