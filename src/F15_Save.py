import os
import time

def arr_to_csv(arr:str, path):
    #menyalin data dari list of dictionary to file csv
    file = open(path, 'w')
    for i in range (len(arr)):
        cur_str = ''
        cur_sub = arr[i]
        for j in range (len(cur_sub)):
            if j != len(cur_sub) -1:
                cur_str += str(cur_sub[j]) + ','
            else:
                cur_str += str(cur_sub[j])
        file.write(cur_str + '\n')


def saving_to_folder(user:str, monster:str, monster_inventory:str, item_inventory:str, monster_shop:str, item_shop:str):
    folder = input("Masukkan nama folder: ")
    print ("Saving...")
    time.sleep(3)

    data_path = os.path.join(os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), os.pardir)), 'data')
    isExist = os.path.exists(os.path.join(data_path, folder))

    #periksa apakah folder sudah ada
    if isExist == False:
        os.makedirs(os.path.join(data_path, folder))
        print(f"Membuat folder data/{folder}...")

    cur_dir = os.path.join(data_path, folder)
    arr_to_csv(user, os.path.join(cur_dir, 'user.csv'))
    arr_to_csv(monster, os.path.join(cur_dir, 'monster.csv'))
    arr_to_csv(monster_inventory, os.path.join(cur_dir, 'monster_inventory.csv'))
    arr_to_csv(item_inventory, os.path.join(cur_dir, 'item_inventory.csv'))
    arr_to_csv(monster_shop, os.path.join(cur_dir, 'monster_shop.csv'))
    arr_to_csv(item_shop, os.path.join(cur_dir, 'item_shop.csv'))   
    print(f"Perubahan berhasil di simpan dalam folder {folder}")
