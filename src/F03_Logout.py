def logout(status):
    if status == True: #sudah login
        status = False
        user_id = 'NaN'
        username = 'NaN'
        role = 'NaN'
        owca = 'NaN'
        #keluar dari akun
    else:
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    return status, user_id, username, 0, 0
