#inisiasi keadaan

def help(status, role):
    print ('========== HELP ==========')
    print ()
    if status == True:
        if role == "Agent":
            print ("Halo Agent Purry. Kamu memanggil command HELP. Kamu memilih jalan yang benar, semoga kamu")
            print ("tidak tersesat kemudian. Berikut adalah hal-hal yang dapat kamu lakukan sekarang:")
            print ()
            print ("    1. Logout\t: Keluar dari akun yang sedang digunakan")
            print ("    2. Inventory\t: Melihat owca-dex yang dimiliki oleh Agent")
            print ("    3. Battle\t: Bertarung melawan monster secara random.")
            print ("    4. Arena\t: Arena berlatih untuk meningkatkan kemampuan agen dan para monster.")
            print ("    5. Shop\t: Tempat agen membeli monster dan potion")
            print ("    6. Laboratoty\t: Melakukan upgrade monster yang dimiliki.")

            print ()
            print ("Footnote:")
            print ("    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print ("    2. Jangan lupa untuk memasukkan input yang valid")
            cmd = input(">>> ")

        elif role == "Admin":
            print ("Selamat datang, Admin. Berikut adalah hal-hal yang dapat kamu lakukan:")
            print()
            print ("    1. Logout\t: Keluar dari akun yang sedang digunakan")
            print ("    2. Shop\t: Melakukan manajemen pada SHOP sebagai tempat jual beli peralatan Agent")
            print ("    3. Monster\t: Mengatur monster dalam database.")
            print ()
            print ("Footnote:")
            print ("    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
            print ("    2. Jangan lupa untuk memasukkan input yang valid")
            cmd = input(">>> ")

    else:
        print ("Kamu belum login sebagai role apapun. Silahkan login terlebih dahulu.")
        print ()
        print ("    1. Login\t: Masuk ke dalam akun yang sudah terdaftar")
        print ("    2. Register\t: Membuat akun baru")
        print ()
        print ("Footnote:")
        print ("    1. Untuk menggunakan aplikasi, silahkan masukkan nama fungsi yang terdaftar")
        print ("    2. Jangan lupa untuk memasukkan input yang valid")
        cmd = input(">>> ")
