def main():
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
    from src.F14_Load import load
    from src.F16_Exit import keluar


    #INISIASI KONDISI
    status = False #artinya belum login
    role = 'NaN'
    exit = False
    username = 'NaN'

    monster = csv_to_array('monster.csv')
    user = csv_to_array('user.csv')
    item_inventory = csv_to_array('item_inventory.csv')
    monster_inventory = csv_to_array('monster_inventory.csv')
    item_shop = csv_to_array('item_shop.csv')
    monster_shop = csv_to_array('monster_shop.csv')

    while exit == False:
        cmd = input(">>> ")
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
            inventory(user_id,user,monster_inventory,item_inventory,monster)
        elif cmd == "BATTLE":
            battle(0,user_id,False,0,[],0,monster,monster_inventory,item_inventory,user)
        elif cmd == "ARENA":
            arena(user_id,monster_inventory,monster,user,item_inventory)
        elif cmd == "SHOP":
            if role == "Agent":
                shop(role, monster_shop, item_shop, monster, monster_inventory, item_inventory, owca)
            elif role == "Admin":
                shop_management(role, item_shop, monster_shop, monster)
        elif cmd == "LABORATORY":
            laboratory(user_id, monster_inventory, monster, role, owca)
        elif cmd == "MONSTER":
            monster_management(username, role, monster)
        elif cmd == "LOAD":
            load()
        elif cmd == "SAVE":
            save()
        elif cmd == "EXIT":
            keluar()

main()