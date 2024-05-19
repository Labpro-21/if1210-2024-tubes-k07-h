def main(folder):
    print('''

 ██████╗  █████╗ ███╗   ███╗███████╗    ███████╗████████╗ █████╗ ██████╗ ████████╗
██╔════╝ ██╔══██╗████╗ ████║██╔════╝    ██╔════╝╚══██╔══╝██╔══██╗██╔══██╗╚══██╔══╝
██║  ███╗███████║██╔████╔██║█████╗      ███████╗   ██║   ███████║██████╔╝   ██║   
██║   ██║██╔══██║██║╚██╔╝██║██╔══╝      ╚════██║   ██║   ██╔══██║██╔══██╗   ██║   
╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗    ███████║   ██║   ██║  ██║██║  ██║   ██║   
 ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝    ╚══════╝   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   
                                                                                  ''')
    from src.csv_to_array import csv_to_array
    from src.F01_Register import register
    from src.F02_Login import login
    from src.F03_Logout import logout
    from src.F04_MenuHelp import help
    from src.F07_Inventory import inventory
    from src.F08_Battle import battle
    from src.F09_Arena import arena
    from src.F10_ShopCurrency import shop
    from src.F11_Laboratory import laboratory
    from src.F12_ShopManagement import shop_management
    from src.F13_MonsterManagement import monster_management
    from src.F15_Save import saving_to_folder
    from src.F16_Exit import keluar

    #INISIASI KONDISI
    status = False #artinya belum login
    role = 'NaN'
    exit = False
    username = 'NaN'

    monster = csv_to_array(folder, 'monster.csv')
    user = csv_to_array(folder, 'user.csv')
    item_inventory = csv_to_array(folder, 'item_inventory.csv')
    monster_inventory = csv_to_array(folder, 'monster_inventory.csv')
    item_shop = csv_to_array(folder, 'item_shop.csv')
    monster_shop = csv_to_array(folder, 'monster_shop.csv')

    while exit == False:
        cmd = str.upper(input(">>> "))
        if cmd == "REGISTER":
            register(status, user, monster, monster_inventory, item_inventory)
        elif cmd == "LOGIN":
            user_info = login(user, status)
            status = user_info[0]
            user_id = user_info[1]
            username = user_info[2]
            role = user_info[3]
            owca = user_info[4]
        elif cmd == "LOGOUT":
            user_info = logout(status)
            status = user_info[0]
            user_id = user_info[1]
            username = user_info[2]
            role = user_info[3]
            owca = user_info[4]
        elif cmd == "HELP":
            help(status, role, username)
        elif cmd == "INVENTORY":
            inventory(user_id,owca,monster_inventory,item_inventory,monster)
        elif cmd == "BATTLE":
            owca = battle(0,user_id,False,0,[],0,monster,monster_inventory,item_inventory,owca)
        elif cmd == "ARENA":
            owca = arena(user_id,monster_inventory,monster,username,owca,item_inventory)
        elif cmd == "SHOP":
            if role == "Agent":
                shop(role, monster_shop, item_shop, monster, monster_inventory, item_inventory, owca)
            elif role == "Admin":
                shop_management(role, item_shop, monster_shop, monster)
        elif cmd == "LABORATORY":
            laboratory(user_id, monster_inventory, monster, role, owca)
        elif cmd == "MONSTER":
            monster_management(username, role, monster)
        elif cmd == "SAVE":
            saving_to_folder(user, monster, monster_inventory, item_inventory, monster_shop, item_shop)
        elif cmd == "EXIT":
            keluar()
        else:
            print("Maaf, fitur tersebut tidak tersedia. Mohon pilih fitur yang tersedia.")

import argparse
import os

def check(folder):
    data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    isExist = os.path.exists(os.path.join(data_path, folder))
    if isExist == False:
        raise argparse.ArgumentTypeError(f'Folder {folder} tidak ditemukan')
    return folder

def load():
    parser = argparse.ArgumentParser(description="Mengakses folder data")

    parser.add_argument('folder', type=check)

    args = parser.parse_args()

    folder = args.folder
    print()
    print("Selamat datang di OWCA")
    main(folder)

load()