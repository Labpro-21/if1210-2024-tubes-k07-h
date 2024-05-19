import os
import time

def arr_to_csv(csv:str, arr:str, folder:str):
    #menyalin data dari list of dictionary to file csv
    file = open(os.path.join(folder, csv), 'w')
    csv_data = '\n'.join([','.join(map(str, row)) for row in arr])
    file.write(csv_data)
    file.close()

def save(folder:str, user:str, monster:str, monster_inventory:str, item_inventory:str, monster_shop, item_shop:str):
    arr_to_csv('user.csv', user, folder)
    arr_to_csv('monster.csv', monster, folder)
    arr_to_csv('monster_inventory.csv', monster_inventory, folder)
    arr_to_csv('item_inventory.csv', item_inventory, folder)
    arr_to_csv('monster_shop.csv', monster_shop, folder)
    arr_to_csv('item_shop', item_shop, folder)

def saving_to_folder(user:str, monster:str, monster_inventory:str, item_inventory:str, monster_shop:str, item_shop:str):
    folder = input("Masukkan nama folder: ")

    #periksa apakah folder sudah ada
    if os.path.exists(folder):
        print("Saving...")
        time.sleep(3)
        print("Perubahan berhasil disimpan")
        save(folder, user, monster, monster_inventory, item_inventory, monster_shop, item_shop)

    else:
        print("Membuat folder baru")
        print("Saving...")
        os.makedirs(folder)
        time.sleep(3)
        print("Perubahan berhasil disimpan")
        save(folder, user, monster, monster_inventory, item_inventory, monster_shop, item_shop)
