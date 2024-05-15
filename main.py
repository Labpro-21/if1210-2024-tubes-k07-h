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
    from src.F08_Battle import battle
    from src.F10_ShopCurrency import shop
    from src.F12_ShopManagement import shop_management
    from src.F13_MonsterManagement import monster_management
    from src.F14_Load import load

    #INISIASI KONDISI
    status = False #artinya belum login

    monster = csv_to_array('monster.csv')
    user = csv_to_array('user.csv')
    item_inventory = csv_to_array('item_inventory.csv')
    monster_inventory = csv_to_array('monster_inventory.csv')
    item_shop = csv_to_array('item_shop.csv')
    monster_shop = csv_to_array('monster_shop.csv')

    cmd = input(">>> ")
    if cmd == "REGISTER":
        register(status, user, monster, monster_inventory, item_inventory)
        cmd = input(">>> ")
    elif cmd == "LOGIN":
        login(user, status)
    elif cmd == "LOGOUT":
        logout()
    elif cmd == "HELP":
        help()
    elif cmd == "INVENTORY":
        inventory()
    elif cmd == "BATTLE":
        battle()
    elif cmd == "ARENA":
        arena()
    elif cmd == "SHOP":
        shop(monster_shop, item_shop, monster, monster_inventory, item_inventory)
    elif cmd == "SHOPMANAGEMENT":
        shop_management(item_shop, monster_shop, monster)
    elif cmd == "LABORATORY":
        laboratory()
    elif cmd == "MONSTER":
        monster_management(monster)
    elif cmd == "LOAD":
        load()
    elif cmd == "SAVE":
        save()
    elif cmd == "EXIT":
        exit()

    

main()