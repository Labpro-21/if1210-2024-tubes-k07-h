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
    import sys

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
            regist_info = register(status, user, monster, monster_inventory, item_inventory)
            status = regist_info[0]
            user = regist_info[1]
            monster_inventory = regist_info[2]
            item_inventory = regist_info[3]
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
            if role == "Agent":
                inventory(user_id,owca,monster_inventory,item_inventory,monster)
            elif role == "Admin":
                print("Anda tidak dapat mengakses inventory karena Anda bukan seorang Agent.")
            else:
                print("Anda tidak dapat mengakses inventory karena belum login. Silahkan login terlebih dahulu.")
        elif cmd == "BATTLE":
            if role == "Agent":
                owca = battle(0,user_id,False,0,[],0,monster,monster_inventory,item_inventory,owca)
            elif role == "Admin":
                print("Anda tidak dapat mengakses battle karena Anda bukan seorang Agent.")
            else:
                print("Anda tidak dapat mengakses battle karena belum login. Silahkan login terlebih dahulu.")
        elif cmd == "ARENA":
            if role == "Agent":
                owca = arena(user_id,monster_inventory,monster,username,owca,item_inventory)
            elif role == "Admin":
                print("Anda tidak dapat mengakses arena karena Anda bukan seorang Agent.")
            else:
                print("Anda tidak dapat mengakses arena karena belum login. Silahkan login terlebih dahulu.")
        elif cmd == "SHOP":
            if role == "Agent":
                shop_info = shop(role, monster_shop, item_shop, monster, monster_inventory, item_inventory, owca)
                owca = shop_info[0]
                monster_shop = shop_info[1]
                item_shop = shop_info[2]
                monster_inventory = shop_info[3]
                item_inventory = shop_info[4]
            elif role == "Admin":
                shop_info = shop_management(role, item_shop, monster_shop, monster)
                item_shop = shop_info[0]
                monster_shop = shop_info[1]
            else:
                print("Anda tidak dapat mengakses shop karena belum login. Silahkan login terlebih dahulu.")
        elif cmd == "LABORATORY":
            lab_info = laboratory(user_id, monster_inventory, monster, role, owca)
            monster_inventory = lab_info[0]
            owca = lab_info[1]
        elif cmd == "MONSTER":
            monster = monster_management(username, role, monster)
        elif cmd == "SAVE":
            saving_to_folder(user, monster, monster_inventory, item_inventory, monster_shop, item_shop)
        elif cmd == "EXIT":
            exit_info = keluar()
            if exit_info == 2: # mau menyimpan
                saving_to_folder
                print('''
        ███████╗███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗
        ██╔════╝██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║
        ███████╗█████╗  █████╗       ╚████╔╝ ██║   ██║██║   ██║██║
        ╚════██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██║   ██║╚═╝
        ███████║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝██╗
        ╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝                                                           
        ''')
                sys.exit()
            else: #exit info = 1
                print('''
        ███████╗███████╗███████╗    ██╗   ██╗ ██████╗ ██╗   ██╗██╗
        ██╔════╝██╔════╝██╔════╝    ╚██╗ ██╔╝██╔═══██╗██║   ██║██║
        ███████╗█████╗  █████╗       ╚████╔╝ ██║   ██║██║   ██║██║
        ╚════██║██╔══╝  ██╔══╝        ╚██╔╝  ██║   ██║██║   ██║╚═╝
        ███████║███████╗███████╗       ██║   ╚██████╔╝╚██████╔╝██╗
        ╚══════╝╚══════╝╚══════╝       ╚═╝    ╚═════╝  ╚═════╝ ╚═╝                                                           
        ''')
            sys.exit()
        else:
            print("Maaf, fitur tersebut tidak tersedia. Mohon pilih fitur yang tersedia.")

import argparse
import os
import time

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
    print("Loading...")
    time.sleep(3)
    main(folder)

load()