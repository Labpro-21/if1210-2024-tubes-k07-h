####################F12###############################

def shop_management(role:str, item_shop:str, monster_shop:str, monster:str):
    if role == "Admin":
        #DEFAULT SHOP
        #default monster di shop
        monster_in_shop = []
        for i in range (len(monster_shop)):
            monster_in_shop.append(monster[i])

        #default potion di shop
        item_in_shop = []
        for i in range (3):
            item_in_shop.append(item_shop[i])

        #inisiasi kondisi
        quit = False
        print()
        print("█ █▀█ █▀█ ▄▀█ █▀ █░█ ▄▀█ █ █▀▄▀█ ▄▀█ █▀ █▀▀")
        print("█ █▀▄ █▀▄ █▀█ ▄█ █▀█ █▀█ █ █░▀░█ █▀█ ▄█ ██▄")
        print()
        print("█▀ █▀▀ █░░ ▄▀█ █▀▄▀█ ▄▀█ ▀█▀   █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄░█ █▀▀   █▄▀ █▀▀ █▀▄▀█ █▄▄ ▄▀█ █░░ █")
        print("▄█ ██▄ █▄▄ █▀█ █░▀░█ █▀█ ░█░   █▄▀ █▀█ ░█░ █▀█ █░▀█ █▄█   █░█ ██▄ █░▀░█ █▄█ █▀█ █▄▄ █")
        print()
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡠⠔⢊⠟⠉⠈⠑⣤⠊⠁⠈⠙⡝⠒⠤⡀⠀⠀⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⠀⢀⠔⠉⠀⠀⢈⠀⠀⢸⣷⢸⣾⡧⠀⠀⢸⠀⠀⠈⠳⣄⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⠀⡠⠋⢀⠴⠒⠉⠙⢆⣀⢀⣭⢿⢬⣁⢀⡠⠋⠉⠒⠦⡀⠈⢦⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⢠⠃⡴⠉⠒⠂⠤⢄⣀⠀⠸⣯⢊⣸⠃⢀⣀⡤⠤⠒⠒⠈⣆⠈⡆⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⣬⠊⠁⠭⠤⠤⠤⠤⠤⡍⠀⠈⢹⠁⠀⠡⠤⠤⠤⠤⠤⠭⠈⠑⣼⠀⠀⠀")
        print("⠀⠀⠀⠀⠀⡿⡀⠀⣀⣀⠀⠤⠤⠀⠂⠀⠀⠸⠀⠀⠐⠀⠤⠤⠤⠀⣀⠀⢀⢿⠀⠀⠀")
        print("⡠⠒⠂⠐⠢⣇⢹⠂⢥⠤⠤⠐⠒⠒⠈⠉⠉⠉⠉⠉⠉⠀⠒⠂⠠⢤⡄⠒⡏⢸⠀⠀⠀")
        print("⠃⠀⠀⠀⠀⢸⡼⡄⠈⢣⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠞⠀⢰⢀⠇⠀⠀⠀")
        print("⢣⡀⠀⠀⣀⠎⠛⣿⡀⠀⠙⣄⠀⡠⠤⠤⠤⣀⠤⠤⠤⢄⠀⣠⠊⠀⢀⢆⠎⠀⠀⠀⠀")
        print("⠀⠈⠉⠙⣄⠀⠀⠈⠻⣄⠀⠈⠙⢤⡀⠀⠀⠀⠀⠀⢀⡠⠟⠁⠀⣠⣮⠃⠀⠀⠀⠀⠀")
        print("⠀⠀⠀⠀⠈⠳⡀⠀⠀⢸⡓⢤⠤⣄⣈⣉⣐⣒⣂⣉⣁⣀⡠⠤⠴⢻⡅⠀⠀⠀⠀⠀⠀")
        print()
        action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
        while not quit: #selama user belum memilih keluar, maka akan melooping terus
            ########################LIHAT###############################
            #melihat semua hal yang ada di shop
            if action == "lihat" and quit == False: 
                option_lihat = input(">>>Mau lihat apa?(monster/potion):")

                if option_lihat == "monster":
                    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                    for i in range (1, len(monster_in_shop)):
                        print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_shop[i][1]}\t|{monster_shop[i][2]}\t")
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()

                elif option_lihat == "potion":
                    print("ID\t|Type\t\t\t|Stock\t|Price")
                    for i in range (1, len(item_in_shop)):
                        if i == 3:
                            print(f"{i}\t|{item_in_shop[i][0]}\t\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                        else:
                            print(f"{i}\t|{item_in_shop[i][0]}\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()
                else: #validasi masukan
                    print("Masukan tidak valid, periksa kembali masukan Anda! (╥﹏╥)")

            ########################TAMBAH###############################
            #menambahkan item atau monster ke dalam shop
            elif action == "tambah" and quit == False:
                option_tambah = input(">>>Mau nambahin apa?(monster/potion):")
                if option_tambah == "monster":
                    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t")
                    for i in range (len(monster_in_shop), len(monster)):
                        print(f"{monster[i][0]}\t|{monster[i][1]}\t\t|{monster[i][2]}\t\t|{monster[i][3]}\t\t|{monster[i][4]}\t")
                    id_monster = input(">>>Masukkan id monster: ")
                    stok_awal_monster = input(">>>Masukkan stok awal: ")
                    harga_monster = input(">>>Masukkan harga: ")
                    for i in range(1,len(monster)):
                        if id_monster == monster[i][0]:
                            print(f"{monster[i][1]} berhasil ditambahkan ke dalam shop! ٩(^ᗜ^ )و '- ")
                            monster_shop.append([id_monster, stok_awal_monster, harga_monster])
                            # append monster yang dipilih ke monster in shop
                            monster_in_shop.append(monster[i])
                            break
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()

                elif option_tambah == "potion":
                    print("ID\t|Type\t\t\t")
                    for i in range (len(item_in_shop), len(item_shop)):
                        print(f"{i}\t|{item_shop[i][0]}\t")
                    id_potion = input(">>>Masukkan id potion: ")
                    stok_awal_potion = int(input(">>>Masukkan stok awal: "))
                    harga_potion = int(input(">>>Masukkan harga: "))
                    for i in range(len(item_shop)):
                        if id_potion == str(i):
                            print(f"{item_shop[i][0]} berhasil ditambahkan ke dalam shop! ٩(^ᗜ^ )و '- ")
                            item_shop[i][1] = stok_awal_potion
                            item_shop[i][2] = harga_potion
                            #append potion ke item_in_shop
                            item_in_shop.append(item_shop[i])
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()
                else:
                    print(">>>Masukan tidak valid, periksa kembali masukan Anda! (╥﹏╥)")

            ########################UBAH###############################
            #mengubah stock dan harga dari monster atau item yang dijual di shop
            elif action == "ubah" and quit == False:
                option_ubah = input(">>>Mau ubah apa?(monster/potion):")
                if option_ubah == "monster":
                    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                    for i in range (1, len(monster_in_shop)):
                        print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_shop[i][1]}\t|{monster_in_shop[i][2]}\t")
                    #masukkan monster yang ingin diubah
                    id_monster = input(">>>Masukkan id monster: ")
                    stok_baru_monster = (input(">>>Masukkan stok baru: "))
                    harga_monster_baru = input(">>>Masukkan harga baru: ")
                    for i in range(1,len(monster)):
                        if id_monster == str(i):
                            print(f"{monster_in_shop[i][1]} berhasil diubah dengan stok baru sejumlah {stok_baru_monster} dan dengan harga baru {harga_monster_baru}! ٩(^ᗜ^ )و '- ")
                            monster_shop[i][1] = stok_baru_monster
                            monster_shop[i][2] = harga_monster_baru
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()

                elif option_ubah == "potion":
                    print("ID\t|Type\t\t\t|Stock\t|Price")
                    for i in range (1, len(item_in_shop)):
                        if i == 3:
                            print(f"{i}\t|{item_in_shop[i][0]}\t\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                        else:
                            print(f"{i}\t|{item_in_shop[i][0]}\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                    #masukkan monster yang ingin diubah
                    id_potion = input(">>>Masukkan id potion: ")
                    stok_baru_potion = (input(">>>Masukkan stok baru: "))
                    harga_potion_baru = input(">>>Masukkan harga baru: ")
                    for i in range(1,8):
                        if id_potion == str(i):
                            print(f"{item_shop[i][0]} berhasil diubah dengan stok baru sejumlah {stok_baru_potion} dan dengan harga baru {harga_potion_baru}! ٩(^ᗜ^ )و '- ")
                            item_shop[i][1] = stok_baru_potion
                            item_shop[i][2] = harga_potion_baru
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()
                else:
                    print("Masukan tidak valid, periksa kembali masukan Anda! (╥﹏╥)")

            ########################HAPUS###############################
            #menghapus monster atau item yang ada di shop
            elif action == "hapus" and quit == False:
                option_hapus = input(">>>Mau hapus apa? (monster/potion): ")
                if option_hapus == "monster":
                    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                    for i in range (1, len(monster_in_shop)):
                        print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_shop[i][1]}\t|{monster_shop[i][2]}\t")
                    #masukkan monster yang ingin dihapus
                    id_monster = input(">>>Masukkan id monster: ")
                    validasi = input(f">>>Apakah ingin menghapus {monster_in_shop[int(id_monster)][1]} dari shop (y/n)?")
                    if validasi == 'y':
                        print(f"{monster_in_shop[int(id_monster)][1]} telah berhasil dihapus dari shop! ദ്ദി（• ˕ •マ.ᐟ")
                        del monster_in_shop[int(id_monster)]#hapus dari matrixnya
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()
                elif option_hapus == 'potion':
                    print("ID\t|Type\t\t\t|Stock\t|Price")
                    for i in range (1, len(item_in_shop)):
                        print(f"{i}\t|{item_in_shop[i][0]}\t|{item_in_shop[i][1]}\t|{item_in_shop[i][2]}")
                    id_potion = input(">>>Masukkan id potion: ")
                    validasi = input(f">>>Apakah anda yakin ingin menghapus {item_in_shop[int(id_potion)][0]} dari shop (y/n)?")
                    if validasi == 'y':
                        print(f"{item_in_shop[int(id_potion)][0]} telah berhasil dihapus dari shop! ദ്ദി（• ˕ •マ.ᐟ")
                        del item_in_shop[int(id_potion)]#hapus dari matrixnya
                    print()
                    action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                    print()
                else:
                    print("Masukan tidak valid, periksa kembali masukan Anda! (╥﹏╥) ")

            ########################KELUAR###############################
            #ketika sudah tidak ingin membeli apapun, maka akan keluar dari program shop
            elif action == 'keluar':
                quit = True
                print(f"Dadah Mr.Yanto, sampai jumpa lagi! ヾ( ˃ᴗ˂ )◞ ")

            else:
                print("Masukan tidak valid, periksa kembali masukan Anda! (╥﹏╥)")
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
    elif role == "Agent":
        print("Anda bukan seorang Admin, Anda tidak dapat mengakses Shop Management.")
    return item_shop, monster_shop