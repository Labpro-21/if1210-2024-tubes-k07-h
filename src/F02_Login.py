#########################F02#####################
def login(user:str, status:bool):
    #masukkan inputan
    print('''             
 █░░ █▀█ █▀▀ █ █▄░█
 █▄▄ █▄█ █▄█ █ █░▀█
    ''')

    if status == True:
        print("Login gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
        return status, user[0], user[1], user[3], user[4]
    existing_user = []
    for i in range (len(user)):
        existing_user.append(user[i][1])

    while status == False: #belum login
        print("========== LOGIN ==========")
        username = input("Username: ")
        password = input("Password: ")
        #mengecek inputan user
        if username not in existing_user:
            print()
            print("Username tidak terdaftar!")
            status = False
            role = 'NaN'
            user_id = 'NaN'
            username = 'NaN'
            owca = 'NaN'
            
        else:
            for i in range(1, len(user)):
                if username == user[i][1] and password == user[i][2]:
                    print()
                    print(f"Selamat datang, {user[i][3]} {user[i][1]}!")
                    print()
                    print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                    status = True
                    role = user[i][3]
                    user_id = user[i][0]
                    username = user[i][1]
                    owca = int(user[i][4])
                    return status, user_id, username, role, owca
                    
                elif i == len(user) -1: #artinya sudah dicek sampai terakhir
                    print()
                    print("Password salah!")
                    status = False
                    role = 'NaN'
                    user_id = 'NaN'
                    username = 'NaN'
                    owca = 'NaN'
                    
                    
    