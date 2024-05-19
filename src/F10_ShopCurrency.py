def shop(role:str, monster_shop:str, item_shop:str, monster:str, monster_inventory:str, item_inventory:str, owca:int):
    if role == "Agent": #kalau agent bisa beli di shop
        #DEFAULT SHOP
        #default monster di shop
        monster_in_shop = []
        for i in range (len(monster_shop)):
            monster_in_shop.append(monster[i])

        #default potion di shop
        item_in_shop = []
        for i in range (len(item_shop)):
            item_in_shop.append(item_shop[i])

        quit = False
        print("Irasshaimase! Selamat datang di SHOP!!")
        action = input(">>> Pilih aksi (lihat/beli/keluar): ")
        while not quit:
            if action == "lihat": #hanya menampilkan apa yang dijual di shop
                option_lihat = input(">>>Mau lihat apa? (monster/potion):")
                if option_lihat == "monster":
                    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                    for i in range (1, len(monster_in_shop)):
                        print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_shop[i][1]}\t|{monster_shop[i][2]}\t")
                    print()
                    action = input(">>>Pilih aksi (lihat/beli/keluar):")
                elif option_lihat == "potion":
                    print("ID\t|Type\t\t\t|Stock\t|Price")
                    for i in range (1, len(item_in_shop)):
                        print(f"{i}\t|{item_in_shop[i][0]}\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                    print()
                    action = input(">>>Pilih aksi (lihat/beli/keluar):")

            elif action == "beli": #melakukan pembelian di shop
                print (f"Jumlah O.W.C.A. Coin-mu sekarang {owca}")
                option_beli = input(">>>Mau beli apa? (monster/potion):")
                if option_beli == "monster":
                    beli_monster = int(input(">>> Masukkan id monster:"))
                    if owca >= int(monster_in_shop[int(beli_monster)][3]):
                        print(f"Berhasil membeli item {monster_in_shop[int(beli_monster)][1]}")
                        monster_inventory.append(monster_in_shop[beli_monster])
                        owca -= int(monster_in_shop[int(beli_monster)][3])
                        monster_shop[int(beli_monster)][1] = int(monster_shop[int(beli_monster)][1]) - 1
                    else:
                        print("OC-mu tidak cukup.")
                    action = input(">>>Pilih aksi (lihat/beli/keluar):")
                elif option_beli == "potion":
                    beli_potion = int(input(">>> Masukkan id potion: "))
                    jumlah_beli = int(input(">>> Masukkan jumlah: "))
                    if owca >= int(item_in_shop[beli_potion][2]) * jumlah_beli:
                        print(f"Berhasil membeli item: {jumlah_beli} {item_in_shop[beli_potion][0]}. Item sudah masuk ke inventory-mu")
                        item_inventory.append(item_shop[beli_potion])
                        owca -= int(item_in_shop[beli_potion][2]) * jumlah_beli
                        item_shop[beli_potion][1] = int(item_shop[beli_potion][1]) - jumlah_beli
                    else:
                        print("OC-mu tidak cukup.")
                    action = input(">>>Pilih aksi (lihat/beli/keluar):")

            elif action == "keluar": #keluar dari shop
                print("Mr. Yanto bilang makasih, belanja lagi ya nanti :)")
                quit = True
    elif role == "Admin": #kalau admin ngga bisa beli di shop
        print("Anda bukan seorang Agent, Anda tidak dapat mengakses Shop and Currency.")
    return owca, monster_shop, item_shop, monster_inventory, item_inventory