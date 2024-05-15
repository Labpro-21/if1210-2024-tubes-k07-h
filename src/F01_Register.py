##############F01################
def register(status, user, monster, monster_inventory, item_inventory):
    if status == False:
        #masukkan inputan
        username = input("Masukan username: ")
        password = input("Masukkan password: ")

        existing_user = []
        for i in range (len(user)):
            existing_user.append(user[i][1])

        while username in existing_user:
            print(f"Username {username} sudah terpakai, silahkan gunakan username lain!")
            print() 
            username = input("Masukan username: ")
            password = input("Masukkan password: ")

        #mengecek validasi username
        condition = True
        for i in range (len(username)): 
            if 48 <= ord(username[i]) <= 57 or 65 <= ord(username[i]) <= 90 or 97 <= ord(username[i]) <= 122 or ord(username[i]) == 95 or ord(username[i]) == 45:
                condition = True
            else:
                condition = False
                print ("Username hanya boleh berisi alfabet, angka, underscore, dan strip!")
                break
        

        if condition:
            print("Silahkan pilih salah satu monster sebagai monster awalmu.")
            for i in range (1, len(monster)):
                print(f"{monster[i][0]}. {monster[i][1]}")
            monster_awal = int(input("Monster pilihanmu: "))
            print(f"Selamat datang Agent {username}. Mari kita mengalahkan Dr. Asep Spakbor dengan {monster[monster_awal][1]}!")
            user.append([len(user), username, password, 'Agent', '0'])
            monster_inventory.append([len(user), monster_awal, '1'])
            item_inventory.append([len(item_inventory), '-', '-'])
    else:
        print("Register gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan register.")
    return ''