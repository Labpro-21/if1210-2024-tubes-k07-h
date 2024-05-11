#prekondisi agar program dapat berjalan, sementara csv saya masukkan pada tiap filenya

def csv_to_array(file):
    raw_lines = file.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    #mengubah data menjadi matriks 2x2
    newArr = []
    for line in lines:
        array_of_something = line.split(";")
        newArr.append(array_of_something)

    return newArr

#OPEN CSV
#csv dari database monster
monster_file = open("D:\TubesDaspro\monster.csv")
monster = csv_to_array(monster_file)

monster_shop_file = open("D:\TubesDaspro\monster_shop.csv")
monster_shop = csv_to_array(monster_shop_file)

#csv dari database potion
potion_file = open("D:\TubesDaspro\item_shop.csv")
potion = csv_to_array(potion_file)



def shop():
    #menggabungkan csv monster dan monster shop agar elemen lengkap dalam satu array
    monster_full = []
    for i in range (8):
        monster_full.append(monster[i] + monster_shop[i])

    #DEFAULT SHOP
    #default monster di shop
    monster_in_shop = []
    for i in range (4):
        monster_in_shop.append(monster_full[i])

    #default potion di shop
    potion_in_shop = []
    for i in range (2):
        potion_in_shop.append(potion[i])

    #inisiasi kondisi
    quit = False
    print()
    print("Irasshaimase! Selamat datang kembali")
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
                    print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_in_shop[i][6]}\t|{monster_in_shop[i][7]}\t")
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()

            elif option_lihat == "potion":
                print("ID\t|Type\t\t\t|Stock\t|Price")
                for i in range (1, len(potion_in_shop)):
                    print(f"{i}\t|{potion_in_shop[i][0]}\t|{potion_in_shop[i][1]}\t|{potion_in_shop[i][2]}")
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
            else: #validasi masukan
                print("Masukan tidak valid, periksa kembali masukan Anda!")

        ########################TAMBAH###############################
        #menambahkan item atau monster ke dalam shop
        elif action == "tambah" and quit == False:
            option_tambah = input(">>>Mau nambahin apa?(monster/potion):")
            if option_tambah == "monster":
                for i in range (4, 8):
                    print(f"{monster_full[i][0]}\t|{monster_full[i][1]}\t\t|{monster_full[i][2]}\t\t|{monster_full[i][3]}\t\t|{monster_full[i][4]}\t|{monster_full[i][6]}\t|{monster_full[i][7]}\t")
                id_monster = input(">>>Masukkan id monster: ")
                stok_awal_monster = input(">>>Masukkan stok awal: ")
                harga_monster = input(">>>Masukkan harga: ")
                for i in range(1,8):
                    if id_monster == monster_full[i][0]:
                        print(f"{monster_full[i][1]} berhasil ditambahkan ke dalam shop!")
                        monster_full[i][6] = stok_awal_monster
                        monster_full[i][7] = harga_monster
                        # append monster yang dipilih ke monster in shop
                        monster_in_shop.append(monster_full[i])
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()

            elif option_tambah == "potion":
                print("ID\t|Type\t\t\t|Stock\t|Price")
                for i in range (2,4):
                    print(f"{i}\t|{potion[i][0]}\t|{potion[i][1]}\t|{potion[i][2]}")
                id_potion = input(">>>Masukkan id potion: ")
                stok_awal_potion = int(input(">>>Masukkan stok awal: "))
                harga_potion = int(input(">>>Masukkan harga: "))
                for i in range(1,4):
                    if id_potion == str(i):
                        print(f"{potion[i][0]} berhasil ditambahkan ke dalam shop!")
                        potion[i][1] = stok_awal_potion
                        potion[i][2] = harga_potion
                        #append potion ke potion_in_shop
                        potion_in_shop.append(potion[i])
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
            else:
                print(">>>Masukan tidak valid, periksa kembali masukan Anda!")

        ########################UBAH###############################
        #mengubah stock dan harga dari monster atau item yang dijual di shop
        elif action == "ubah" and quit == False:
            option_ubah = input(">>>Mau ubah apa?(monster/potion:)")
            if option_ubah == "monster":
                print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                for i in range (1, len(monster_in_shop)):
                    print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_in_shop[i][6]}\t|{monster_in_shop[i][7]}\t")
                #masukkan monster yang ingin diubah
                id_monster = input(">>>Masukkan id potion: ")
                stok_baru_monster = (input(">>>Masukkan stok baru: "))
                harga_monster_baru = input(">>>Masukkan harga baru: ")
                for i in range(1,8):
                    if id_monster == str(i):
                        print(f"{monster_in_shop[i][1]} berhasil diubah dengan stok baru sejumlah {stok_baru_monster} dan dengan harga baru {harga_monster_baru}!")
                        monster_in_shop[i][6] = stok_baru_monster
                        monster_in_shop[i][7] = harga_monster_baru
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()

            elif option_ubah == "potion":
                print("ID\t|Type\t\t\t|Stock\t|Price")
                for i in range (1, len(potion_in_shop)):
                    print(f"{i}\t|{potion_in_shop[i][0]}\t|{potion_in_shop[i][1]}\t|{potion_in_shop[i][2]}")
                #masukkan monster yang ingin diubah
                id_potion = input(">>>Masukkan id potion: ")
                stok_baru_potion = (input(">>>Masukkan stok baru: "))
                harga_potion_baru = input(">>>Masukkan harga baru: ")
                for i in range(1,8):
                    if id_potion == str(i):
                        print(f"{potion[i][0]} berhasil diubah dengan stok baru sejumlah {stok_baru_potion} dan dengan harga baru {harga_potion_baru}!")
                        potion[i][1] = stok_baru_potion
                        potion[i][2] = harga_potion_baru
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
            else:
                print("Masukan tidak valid, periksa kembali masukan Anda!")

        ########################HAPUS###############################
        #menghapus monster atau item yang ada di shop
        elif action == "hapus" and quit == False:
            option_hapus = input(">>>Mau hapus apa? (monster/potion): ")
            if option_hapus == "monster":
                print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP\t|Stock\t|Price")
                for i in range (1, len(monster_in_shop)):
                    print(f"{monster_in_shop[i][0]}\t|{monster_in_shop[i][1]}\t\t|{monster_in_shop[i][2]}\t\t|{monster_in_shop[i][3]}\t\t|{monster_in_shop[i][4]}\t|{monster_in_shop[i][6]}\t|{monster_in_shop[i][7]}\t")
                #masukkan monster yang ingin dihapus
                id_monster = input(">>>Masukkan id monster: ")
                validasi = input(f">>>Apakah ingin menghapus {monster_in_shop[int(id_monster)][1]} dari shop (y/n)?")
                if validasi == 'y':
                    print(f"{monster_in_shop[int(id_monster)][1]} telah berhasil dihapus dari shop!")
                    del monster_in_shop[int(id_monster)]#hapus dari matrixnya
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
            elif option_hapus == 'potion':
                print("ID\t|Type\t\t\t|Stock\t|Price")
                for i in range (1, len(potion_in_shop)):
                    print(f"{i}\t|{potion_in_shop[i][0]}\t|{potion_in_shop[i][1]}\t|{potion_in_shop[i][2]}")
                id_potion = input(">>>Masukkan id potion: ")
                validasi = input(f">>>Apakah anda yakin ingin menghapus {potion_in_shop[int(id_potion)][0]} dari shop (y/n)?")
                if validasi == 'y':
                    print(f"{potion_in_shop[int(id_potion)][0]} telah berhasil dihapus dari shop!")
                    del potion_in_shop[int(id_potion)]#hapus dari matrixnya
                print()
                action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
                print()
            else:
                print("Masukan tidak valid, periksa kembali masukan Anda!")

        ########################KELUAR###############################
        #ketika sudah tidak ingin membeli apapun, maka akan keluar dari program shop
        elif action == 'keluar':
            quit = True
            print(f"Dadah Mr.Yanto, sampai jumpa lagi!")

        else:
            print("Masukan tidak valid, periksa kembali masukan Anda!")
            print()
            action = input(">>>Pilih aksi (lihat/tambah/ubah/hapus/keluar):")
            print()
    return ''
shop()