def main():
    from src.F08_Battle import battle
    from src.F14_Load import load
    from src.F12_ShopManagement import shop_management
    from src.csv_to_array import csv_to_array


    monster = csv_to_array('monster.csv')
    user = csv_to_array("user.csv")
    item_inventory = csv_to_array('item_inventory.csv')
    monster_inventory = csv_to_array('monster_inventory.csv')
    item_shop = csv_to_array('item_shop.csv')
    monster_shop = csv_to_array('monster_shop.csv')

    #DEFAULT SHOP
    #default monster di shop
    monster_in_shop = []
    for i in range (len(monster_shop)):
        monster_in_shop.append(monster[i])

    #default potion di shop
    item_in_shop = []
    for i in range (3):
        item_in_shop.append(item_shop[i])

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
        shop()
    elif cmd == "SHOPMANAGEMENT":
        shop_management(item_in_shop, monster_in_shop, item_shop, monster_shop)
    elif cmd == "LABORATORY":
        laboratory()
    elif cmd == "MONSTER":
        monster()
    elif cmd == "LOAD":
        load()
    elif cmd == "SAVE":
        save()
    elif cmd == "EXIT":
        exit()

    

main()