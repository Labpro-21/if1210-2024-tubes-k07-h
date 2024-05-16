#########################F02#####################
def login(user, status):
    #masukkan inputan

    username = input("Username: ")
    password = input("Password: ")

    existing_user = []
    for i in range (len(user)):
        existing_user.append(user[i][1])

    if status == False: #belum login
        #mengecek inputan user
        if username not in existing_user:
            print("Username tidak terdaftar!")
        else:
            for i in range(1, len(user)):
                if username == user[i][1] and password == user[i][2]:
                    print(f"Selamat datang, {user[i][3]} {user[i][1]}!")
                    print("Masukkan command 'help' untuk daftar command yang dapat kamu panggil.")
                    status = True
                    role = user[i][3]
                    user_id = user[i][0]
                    username = user[i][1]
                    owca = 0
                    break
                elif i == len(user) -1:
                    print("Password salah!")
                    break
    else:
        print("Login gagal!")
        print("Anda telah login dengan username Purry, silahkan lakukan “LOGOUT” sebelum melakukan login kembali.")
    
    return status, user_id, username, role, owca