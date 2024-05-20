import sys
from src.F15_Save import saving_to_folder
def keluar(user, monster, monster_inventory, item_inventory, monster_shop, item_shop): #keluar program
    quit = False
    while quit == False:
        validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
        if validasi == "n" or validasi == "N":
            print('''
        ███████╗███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗
        ██╔════╝██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║
        ███████╗█████╗  █████╗       ╚████╔╝ ██║   ██║██║   ██║██║
        ╚════██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██║   ██║╚═╝
        ███████║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝██╗
        ╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝                                                           
        ''')
            sys.exit()
        elif validasi == "y" or validasi == "Y":
            saving_to_folder(user, monster, monster_inventory, item_inventory, monster_shop, item_shop)
            print('''
        ███████╗███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗
        ██╔════╝██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║
        ███████╗█████╗  █████╗       ╚████╔╝ ██║   ██║██║   ██║██║
        ╚════██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██║   ██║╚═╝
        ███████║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝██╗
        ╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝                                                           
        ''')
            sys.exit()                                          
        else: #inputan tidak velid
            quit = False
