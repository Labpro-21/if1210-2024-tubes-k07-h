def laboratory(user_id, monster_inventory, monster, role, owca):
    if role == "Agent":
        print("Selamat datang di Lab Dokter Asep !!!")
        print("============ MONSTER LIST ============")
        for i in range (1, len(monster_inventory)):
            if monster_inventory[i][0] == user_id:
                print(f"{monster[i][0]}. {monster[i][1]} (Level: {monster_inventory[i][2]})")

        print("============UPGRADEPRICE============")
        print("1. Level 1 -> Level 2: 200 OC")
        print("2. Level 2 -> Level 3: 300 OC")
        print("3. Level 3 -> Level 4: 400 OC")
        print("4. Level 4 -> Level 5: 500 OC")
        option = input(">>> Pilih monster: ")
        if monster_inventory[int(option)][2] == '1' or '2' or '3' or '4':
            print(f"{monster[int(option)][1]} akan di-upgrade ke level {int(monster_inventory[int(option)][2]) +1}.")
            print(f"Harga untuk melakukan upgrade {monster[int(option)][1]} adalah {100* int(monster_inventory[int(option)][2])} OC.") #harga 100 kali lipat dari level tujuan
            validasi = input(">>> Lanjutkan upgrade (Y/N): ")
            if (validasi == 'Y' or 'y') and (owca >= 100*(int(monster_inventory[int(option)][2]))):
                print(f"Selamat, {monster[int(option)][1]} berhasil di-upgrade ke level {int(monster_inventory[int(option)][2]) +1}!")
                monster_inventory[int(option)][2] = int(monster_inventory[int(option)][2])+ 1
            elif (validasi == 'Y' or 'y') and (owca < 100*(int(monster_inventory[int(option)][2]))):
                print(f"OWCA kamu tidak mencukupi.")
            else:
                print("Kamu tidak melakukan upgrade apa pun.")
        else: #jika level sudah 5
            print(" Maaf,monster yang Anda pilih sudah memiliki level maksimum")

    else:
        print("Anda bukan seorang Agent, Anda tida dapat mengakses Laboratory")
