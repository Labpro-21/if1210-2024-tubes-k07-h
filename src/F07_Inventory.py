# program F07 - Inventory

def inventory (user_id:str ,owca:int ,monster_inventory:str ,item_inventory:str ,monster:str):
    import math
    # Print 2 baris pertama inventory list (User ID dan OWCA)
    user_id = int(user_id)
    print(f"INVENTORY LIST (User ID: {user_id})")
    print(f"Jumlah O.W.C.A. Coin-mu sekarang {owca}")

    # memproses data monster_inventory sebelum diprint
    monster_count = 0 # jumlah monster yang dimiliki
    monster_id = [] # matrix berisi id monster yang dimiliki dan levelnya
    for i in range(len(monster_inventory)): # menghitung jumlah monster pada inventory dan membuat matrix monster_id 
        if monster_inventory[i][0] == str(user_id):
            monster_count += 1
            monster_id.append([(monster_inventory[i][1]),(monster_inventory[i][2])])

    inventory_matrix = [] # menyimpan data inventory keseluruhan untuk bagian detail

    # melakukan print untuk bagian monster pada inventory dan mengisi inventory_matrix
    for i in range(len(monster)):
        for j in range(monster_count):
            if (monster[i][0]) == (monster_id[j][0]):
                print(f"{j+1}. Monster     (Name: {monster[i][1]}, Lvl: {monster_id[j][1]}, HP: {math.floor(int(monster[i][4])+int(monster[i][4])*((int(monster_id[j][1])-1)*10/100))})")
                inventory_matrix.append(monster[i])

    potion_count = 0 # banyak jenis potion yang dimiliki

    # print bagian potion pada inventory, menghitung jenis potion yang dimiliki, dan mengisi inventory_matrix
    for i in range(len(item_inventory)): 
        if item_inventory[i][0] == str(user_id):
            print(f"{potion_count+monster_count+1}. Potion      (Type: {item_inventory[i][1]}, Qty: {item_inventory[i][2]})")
            potion_count+=1
            inventory_matrix.append(item_inventory[i])

    print('Ketik "KELUAR" untuk keluar dari menu inventory')
    
    # bagian input pada inventory (pengguna mengetik command KELUAR untuk berhenti)
    keluar_inventory = False # variabel untuk menghentikan fungsi saat pengguna mengetik KELUAR

    while keluar_inventory == False:
        print("Ketikkan id untuk menampilkan detail item:")
        id_detail = str(input(">>> ")) # input id item yang diiginkan detailnya

        if id_detail == "KELUAR": # keluar dari fungsi bila input KELUAR
            print("Berhasil keluar dari menu inventory")
            keluar_inventory == True
            break

        id_detail = int(id_detail) # mengubah data menjadi int untuk index matrix

        # mencetak detail item dengan bantuan inventory_matrix yang sudah dibuat sebelumnya
        if id_detail <= monster_count:
            print("Monster")
            print(f"Name      : {inventory_matrix[id_detail-1][1]}")
            print(f"ATK Power : {math.floor(int(inventory_matrix[id_detail-1][2])+int(inventory_matrix[id_detail-1][2])*((int(monster_id[id_detail-1][1])-1)*10/100))}")
            print(f"DEF Power : {math.floor(int(inventory_matrix[id_detail-1][3])+int(inventory_matrix[id_detail-1][3])*((int(monster_id[id_detail-1][1])-1)*10/100))}")
            print(f"HP        : {math.floor(int(inventory_matrix[id_detail-1][4])+int(inventory_matrix[id_detail-1][4])*((int(monster_id[id_detail-1][1])-1)*10/100))}")
            print(f"Level     : {monster_id[id_detail-1][1]}")
        elif id_detail <= (monster_count + potion_count):
            print("Potion")
            print(f"Type     : {inventory_matrix[id_detail-1][1]}")
            print(f"Quantity : {inventory_matrix[id_detail-1][2]}")
        else: print("Id item tidak valid")

"""
Aplikasi
Inventory(1)
INVENTORY LIST (User ID: 1)
Jumlah O.W.C.A. Coin-mu sekarang 0
1. Monster     (Name: Hydra, Lvl: 2, HP: 440)
2. Monster     (Name: Medusa, Lvl: 1, HP: 300)
3. Potion      (Type: strength, Qty: 2)
Ketikkan id untuk menampilkan detail item:
>>> 1
Monster
Name      : Hydra
ATK Power : 60
DEF Power : 77
HP        : 440
Level     : 2
Ketikkan id untuk menampilkan detail item:
>>> 2
Monster
Name      : Medusa
ATK Power : 35
DEF Power : 60
HP        : 300
Level     : 1
Ketikkan id untuk menampilkan detail item:
>>> 3
Potion
Type     : strength
Quantity : 2
Ketikkan id untuk menampilkan detail item:
>>> KELUAR
"""