###################F13#################################
# Fungsi untuk memvalidasi sebuah variabel Integer atau bukan
def is_integer(s:int):
    try:
        int(s)
        return True
    except ValueError:
        return False

# Fungsi untuk menampilkan monster pada file monster.csv
def tampilkan_monster(monster:str):
    print("ID\t|Type\t\t|ATK Power\t|DEF Power\t|HP")
    for i in range (1, len(monster)):
        print(f"{monster[i][0]}\t|{monster[i][1]}\t\t|{monster[i][2]}\t\t|{monster[i][3]}\t\t|{monster[i][4]}")
    print()

# Fungsi untuk menambahkan monster
def tambah_monster(monster:str):
    print("==============================")
    print("Memulai pembuatan monster baru")

    new_type = input(">>> Masukkan Type / Nama: ")

    # Memvalidasi apakah type monster sudah pernah digunakan sebelumnya atau belum
    existing_type = []
    for i in range (len(monster)):
        existing_type.append(monster[i][1])

    while new_type in existing_type:
        print("Nama sudah terdaftar, coba lagi!")
        print() 
        new_type = input(">>> Masukkan Type / Nama : ")
    
    
    # Memvalidasi nilai atk power
    while True:
        new_atk_power = input(">>> Masukkan ATK Power : ")
        if is_integer(new_atk_power):
            new_atk_power = int(new_atk_power)
            break
        else:
            print("Masukkan input bertipe Integer, coba lagi!")
            print()

    # Memvalidasi nilai def power
    while True:
        new_def_power = input(">>> Masukkan DEF Power (0-50) : ")
        if is_integer(new_def_power):
            new_def_power = int(new_def_power)
            if 0<=new_def_power<=50:
                break
            else:
                print("DEF Power harus bernilai 0-50, coba lagi!")
                print()
        else:
            print("Masukkan input bertipe Integer, coba lagi!")
            print()

    # Memvalidasi nilai hp
    while True:
        new_hp = input(">>> Masukkan HP : ")
        if is_integer(new_hp):
            new_hp = int(new_hp)
            print()
            break
        else:
            print("Masukkan input bertipe Integer, coba lagi!")
            print()

    # Hasil rekap data monster yang baru
    print("Monster baru berhasil dibuat!")
    print(f"Type : {new_type}")
    print(f"ATK Power : {new_atk_power}")
    print(f"Def Power : {new_def_power}")
    print(f"HP : {new_hp}")

    konfirmasi = input(">>> Tambahkan Monster ke database (Y/N) : ")

    # Selama jawaban bukan Y atau N, user akan diminta untuk menginput ulang
    while konfirmasi != "Y" and konfirmasi != "N":
        print("Jawaban hanya dapat berupa yes (Y) atau no (N)")
        print()
        konfirmasi = str(input(">>> Tambahkan Monster ke database (Y/N) : "))

    # Jika jawabannya Y (Yes), maka monster akan ditambahkan ke file monster.csv
    if konfirmasi == "Y":
        monster.append([len(monster), new_type, new_atk_power, new_def_power, new_hp])
        print("Monster baru berhasil ditambahkan!")

    # Jika jawabannya N (No), monster tidak akan ditambahkan ke file monster.csv
    elif konfirmasi == "N":
        print("Monster gagal ditambahkan!")
    return monster

# Fungsi utama monster management
def monster_management(role:str, monster:str):
    if role == "Admin":
        print("")
        print("█▀ █▀▀ █░░ ▄▀█ █▀▄▀█ ▄▀█ ▀█▀    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄░█ █▀▀    █▀▄ █    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀ ")
        print("▄█ ██▄ █▄▄ █▀█ █░▀░█ █▀█ ░█░    █▄▀ █▀█ ░█░ █▀█ █░▀█ █▄█    █▄▀ █    █▄▀ █▀█ ░█░ █▀█ █▄█ █▀█ ▄█ ██▄ ")
        print("")
        print("█▀█ ▄▀█ █▀█ ▄▀█   █▀▄▀█ █▀█ █▄░█ █▀ ▀█▀ █▀▀ █▀█   █ █ █")
        print("█▀▀ █▀█ █▀▄ █▀█   █░▀░█ █▄█ █░▀█ ▄█ ░█░ ██▄ █▀▄   ▄ ▄ ▄")
        print("")
        print("")
        quit = False
        while quit == False:
            print("1. Tampilkan semua Monster")
            print("2. Tambah Monster baru")
            print("3. Keluar")

            n = input('>>> Pilih Aksi : ')

            # Jika memilih aksi 1, maka list monster akan ditampilkan
            if n == '1':
                tampilkan_monster(monster)
                print() 
                print("█▀ █▀▀ █░░ ▄▀█ █▀▄▀█ ▄▀█ ▀█▀    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄░█ █▀▀    █▀▄ █    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀ ")
                print("▄█ ██▄ █▄▄ █▀█ █░▀░█ █▀█ ░█░    █▄▀ █▀█ ░█░ █▀█ █░▀█ █▄█    █▄▀ █    █▄▀ █▀█ ░█░ █▀█ █▄█ █▀█ ▄█ ██▄ ")
                print("")
                print("█▀█ ▄▀█ █▀█ ▄▀█   █▀▄▀█ █▀█ █▄░█ █▀ ▀█▀ █▀▀ █▀█   █ █ █")
                print("█▀▀ █▀█ █▀▄ █▀█   █░▀░█ █▄█ █░▀█ ▄█ ░█░ ██▄ █▀▄   ▄ ▄ ▄")
                print("")
            
            # Jika memilih aksi 2, maka akan menuju fungsi tambah_monster
            elif n == '2':
                tambah_monster(monster)
                print() 
                print("█▀ █▀▀ █░░ ▄▀█ █▀▄▀█ ▄▀█ ▀█▀    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄░█ █▀▀    █▀▄ █    █▀▄ ▄▀█ ▀█▀ ▄▀█ █▄▄ ▄▀█ █▀ █▀▀ ")
                print("▄█ ██▄ █▄▄ █▀█ █░▀░█ █▀█ ░█░    █▄▀ █▀█ ░█░ █▀█ █░▀█ █▄█    █▄▀ █    █▄▀ █▀█ ░█░ █▀█ █▄█ █▀█ ▄█ ██▄ ")
                print("")
                print("█▀█ ▄▀█ █▀█ ▄▀█   █▀▄▀█ █▀█ █▄░█ █▀ ▀█▀ █▀▀ █▀█   █ █ █")
                print("█▀▀ █▀█ █▀▄ █▀█   █░▀░█ █▄█ █░▀█ ▄█ ░█░ ██▄ █▀▄   ▄ ▄ ▄")
                print("")

            # Jika memilih aksi selain 1 dan 2, user akan diminta untuk menginput ulang jawaban yang sesuai dengan opsi
            elif n == '3':
                quit = True
                print("Terimakasih telah mengunjungi monster management.")
            else :
                print("Nomor tidak ada di pilihan, silahkan coba lagi.")
                print()
    else:
        print("Anda bukan seorang Admin. Anda tidak dapat mengakses monster management.")
    return monster