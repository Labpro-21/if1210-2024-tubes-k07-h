
def register(status: bool, user:str, monster:str, monster_inventory:str, item_inventory:str):
    print('''                      
 █▀█ █▀▀ █▀▀ █ █▀ ▀█▀ █▀▀ █▀█
 █▀▄ ██▄ █▄█ █ ▄█ ░█░ ██▄ █▀▄
''')
    if status == True: #artinya sudah login
        print("Register gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan register.")
    elif status == False:
        existing_user = []
        for i in range (len(user)):
            existing_user.append(user[i][1])

        while status == False: #selama belum berhasil register
            print("========== REGISTER ==========")
            username = input("Masukan username: ")
            password = input("Masukkan password: ")
            if username in existing_user:
                print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
                print()
                status = False
            else: #username belum terdaftar
                #mengecek validasi username
                condition = True #inisiasi keadaan
                for i in range (len(username)): 
                    if 48 <= ord(username[i]) <= 57 or 65 <= ord(username[i]) <= 90 or 97 <= ord(username[i]) <= 122 or ord(username[i]) == 95 or ord(username[i]) == 45:
                        condition = True
                        status = True #sudah valid maka berhasil register
                    else:
                        condition = False
                        status = False
                        print ("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
                        break
        

        while condition:
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            print()
            for i in range (1, len(monster)):
                print(f"{monster[i][0]}. {monster[i][1]}")
            monster_awal = input("Monster pilihanmu: ")
            if ord('1') <= ord(monster_awal) <= ord(str(len(monster))):
                print("==================================")
                print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[int(monster_awal)][1]}!")
                user.append([len(user), username, password, 'Agent', '0'])
                monster_inventory.append([str(len(user)-1), monster_awal, '1'])
                item_inventory.append([str(len(user)-1), '-', '-'])
                return False, user, monster_inventory, item_inventory
            else:
                print("==================================")
                print("Tidak ada pilihan monster tersebut. Silahkan pilih monster yang lain.")
                print()
    