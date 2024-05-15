def main():
    from src.csv_to_array import csv_to_array
    from src.F08_Battle import battle
    from src.F10_ShopCurrency import shop
    from src.F12_ShopManagement import shop_management
    from src.F13_MonsterManagement import monster_management
    from src.F14_Load import load

    monster = csv_to_array('monster.csv')
    user = csv_to_array('user.csv')
    item_inventory = csv_to_array('item_inventory.csv')
    monster_inventory = csv_to_array('monster_inventory.csv')
    item_shop = csv_to_array('item_shop.csv')
    monster_shop = csv_to_array('monster_shop.csv')

    print(monster_shop)
    cmd = input(">>>")
    if cmd == "REGISTER":
        register()
    elif cmd == "LOGIN":
        login()
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