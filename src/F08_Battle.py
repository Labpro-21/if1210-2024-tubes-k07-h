#prekondisi agar semua variable valid
import os
import time
import argparse
import sys
import math

def lcg(a=48271, c=0, m=2**31-1, seed=None):
    x0 = seed

    if seed is None:
        x0 = int(os.getpid() + time.time()) #pakai ini supaya nilainya lebih random
    else:
        x0 = seed

    x_prev = (a * x0 + c) % m #formula lcg
    return a, c, m, x0, x_prev

def generate_number(a, c, m, x0, num_range=None):
    x_prev = (a * x0 + c) % m

    if num_range is None:
        return x_prev
    else:
        return int((x_prev / (m - 1)) * (num_range[1] - num_range[0]) + num_range[0])

# inisiasi parameter LCG 
a, c, m, x0, x_prev = lcg()
def csv_to_array(file):
    raw_lines = file.readlines()
    lines = [raw_line.replace("\n", "") for raw_line in raw_lines]
    #mengubah data menjadi matriks 2x2
    newArr = []
    for line in lines:
        array_of_something = line.split(";")
        newArr.append(array_of_something)

    return newArr

monster_file = open("D:\TubesDaspro\monster.csv")
monster = csv_to_array(monster_file)

item_inventory_file = open("D:\TubesDaspro\item_inventory.csv")
item_inventory = csv_to_array(item_inventory_file)

monster_inventory_file = open("D:\TubesDaspro\monster_inventory.csv")
monster_inventory = csv_to_array(monster_inventory_file)

#pre kondisi semua csv telah valid dan dirubah ke bentuk array

def monster_inv():
    # memproses data monster_inventory sebelum diprint
    for i in range(1, len(monster_inventory)):
        print(f"{i} {monster[int(monster_inventory[i][1])][1]}")
    return monster_inventory
def potion_inv():
    # memproses data item_inventory sebelum diprint
    for i in range(1, len(item_inventory)):
        print(f"{i} {item_inventory[i][1]} (Qty : {item_inventory[i][2]})")
    return item_inventory

##########################BATTLE###############################    
def battle():
    print('''
                       
    █▄▄ ▄▀█ ▀█▀ ▀█▀ █░░ █▀▀
    █▄█ █▀█ ░█░ ░█░ █▄▄ ██▄                                                  
''')
    print ("""           
           _/\----/\   
          /         \     /\.
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__
""")
    level_mons = generate_number(a, c, m, x0, [1, 5])
    random_number = generate_number(a, c, m, x0, [4, 8])
    print(f"RAWRR, Monster {monster[random_number][1]} telah muncul!!")
    print()
    #jika level diatas 1, maka base attribute akan bertambah sesuai ketentuan
    hp_monster = math.floor(int(monster[random_number][4])*(1+(level_mons-1)*0.1))
    atk_monster = math.floor(int(monster[random_number][2])*(1+(level_mons-1)*0.1))
    def_monster = math.floor(int(monster[random_number][3])*(1+(level_mons-1)*0.1))
    print(f"Nama        : {monster[random_number][1]}")
    print(f"ATK Power   : {atk_monster}")
    print(f"DEF Power   : {def_monster}")
    print(f"HP          : {hp_monster}")
    print(f"Level       : {level_mons}")
    print()
    print("========== MONSTER LIST ==========")

    #ini monster punya agent
    monster_inv()

    figth = False
    monster_figth = input("Pilih monster untuk bertarung: ")
    while not figth:
        for i in range (1, len(monster_inventory)):
            if monster_figth == monster[i][0]:
                index_monster_agent = i
                print('''
          /\----/\_   
         /         \   /|
        |  | O    O | / |
        |  | .vvvvv.|/  /
       /   | |     |   /
      /    | `^^^^^   /
     | /|  |         /
      / |    ___    |
         \  |   |   |
         |  |   |   |
          \._\   \._\ 

            ''')
                print(f"RAWRR, Agent X mengeluarkan monster {monster[i][1]}")
                print()
                level_mons_agent = generate_number(a, c, m, x0, [1, 5])
                #jika level diatas 1, maka base attribute akan bertambah sesuai ketentuan
                hp_monster_agent = math.floor(int(monster[i][4])*(1+(level_mons_agent-1)*0.1))
                atk_monster_agent = math.floor(int(monster[i][2])*(1+(level_mons_agent-1)*0.1))
                def_monster_agent = math.floor(int(monster[i][3])*(1+(level_mons_agent-1)*0.1))
                print(f"Nama        : {monster[i][1]}")
                print(f"ATK Power   : {atk_monster_agent}")
                print(f"DEF Power   : {def_monster_agent}")
                print(f"HP          : {hp_monster_agent}")
                print(f"Level       : {level_mons_agent}")
                print()
                figth = True
                break
            elif i == 3:
                print("Pilihan nomor tidak tersedia!")
                monster_figth = input("Pilih monster untuk bertarung: ")

    win = False
    count_figth = 1
    count_strength = 0
    count_resilience = 0
    count_healing = 0
    while not win:
        #giliran monster agent
        print(f"============ TURN {count_figth} ({monster[index_monster_agent][1]}) ============")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")
        choice_figth = input("Pilihan perintah: ")
        if choice_figth == '1':
            print()
            print(f"SCHWINKKK, {monster[index_monster_agent][1]} menyerang {monster[random_number][1]}")
            print()
            #attack didapat dari rgn dalam rentang +- 30% ATK power
            #def power akan menurunkan serangan musuh rentang 0-50%
            hp_monster -= math.floor((1-def_monster/100)*(generate_number(a, c, m, x0, [0.7*int(atk_monster_agent), 1.3*int(atk_monster_agent)])))
            if hp_monster <= 0:
                hp_monster = 0
                print(f"Nama        : {monster[random_number][1]}")
                print(f"ATK Power   : {atk_monster}")
                print(f"DEF Power   : {def_monster}")
                print(f"HP          : {hp_monster}")
                print(f"Level       : {level_mons}")
                print()
                win = True
                print(f"Selamat, Anda berhasil mengalahkan monster {monster[random_number][1]} !!!")
                OC_win = generate_number(a, c, m, x0, [30, 50])
                print(f"Total OC yang diperoleh {OC_win}")
                break
            else:
                print(f"Nama        : {monster[random_number][1]}")
                print(f"ATK Power   : {atk_monster}")
                print(f"DEF Power   : {def_monster}")
                print(f"HP          : {hp_monster}")
                print(f"Level       : {level_mons}")
                print()
            #giliran monster random
            print(f"============ TURN {count_figth} ({monster[random_number][1]}) ============")
            print(f"SCHWINKKK, {monster[random_number][1]} menyerang {monster[index_monster_agent][1]}")
            print()
            #attack didapat dari rgn dalam rentang +- 30% ATK power
            #def power akan menurunkan serangan musuh rentang 0-50%
            #pakai fungsi floor agar angka yang dihasilkan bulat
            hp_monster_agent -= math.floor((1-def_monster_agent/100)*(generate_number(a, c, m, x0, [0.7*int(atk_monster), 1.3*int(atk_monster)])))
            if hp_monster_agent <= 0:
                hp_monster_agent = 0
                print(f"Nama        : {monster[index_monster_agent][1]}")
                print(f"ATK Power   : {atk_monster_agent}")
                print(f"DEF Power   : {def_monster_agent}")
                print(f"HP          : {hp_monster_agent}")
                print(f"Level       : {level_mons_agent}")
                print()
                win = True
                print(f"Yahhh, Anda dikalahkan monster {monster[random_number][1]}. Jangan menyerah, coba lagi !!!")
                break
            else:
                print(f"Nama        : {monster[random_number][1]}")
                print(f"ATK Power   : {atk_monster_agent}")
                print(f"DEF Power   : {def_monster_agent}")
                print(f"HP          : {hp_monster_agent}")
                print(f"Level       : {level_mons_agent}")
                print()

            count_figth += 1

        elif choice_figth == '2':
            print("============ POTION LIST ============")
            potion_inv()
            print()
            perintah = int(input("Pilih perintah: "))
            print()
            if int(item_inventory[perintah][2]) == 0: #validasi apakah punya potion atau ngga di inventory
                    print("Wah, kamu sedang tidak memiliki ramuan ini, silahkan pilih ramuan lain!")
            else:
                if item_inventory[perintah][1] == "Strength Potion":
                    if count_strength > 0: #jika sudah pernah pakai maka ngga akan ngefek
                        print(f"Kamu mencoba memberikan ramuan ini kepada {monster[index_monster_agent][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                    else:
                        print(f"Setelah meminum ramuan ini, aura kekuatan terlihat mengelilingi {monster[index_monster_agent][1]} dan gerakannya menjadi lebih cepat dan mematikan.")
                        atk_monster_agent += math.floor(0.05*atk_monster_agent) #atk bertambah 50%
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                        count_strength += 1
                    #atk bertambah karena memakai strength potion
                elif item_inventory[perintah][1] == "Resilience Potion":
                    if count_resilience > 0: #jika sudah pernah pakai maka ngga akan ngefek
                        print(f"Kamu mencoba memberikan ramuan ini kepada {monster[index_monster_agent][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                    else:
                        print(f"Setelah meminum ramuan ini, muncul sebuah energi pelindung di sekitar {monster[index_monster_agent][1]} yang membuatnya terlihat semakin tangguh dan sulit dilukai.")
                        def_monster_agent += math.floor(0.05*def_monster_agent) #def power bertambah 50%
                        count_resilience += 1
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                    #def bertambah karena memakai resilience potion
                elif item_inventory[perintah][1] == "Healing Potion":
                    if count_healing > 0: #jika sudah pernah pakai maka ngga akan ngefek
                        print(f"Kamu mencoba memberikan ramuan ini kepada {monster[index_monster_agent][1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                    else:
                        print(f"Setelah meminum ramuan ini, luka-luka yang ada di dalam tubuh {monster[index_monster_agent][1]} sembuh dengan cepat. Dalam sekejap, {monster[index_monster_agent][1]} terlihat kembali prima dan siap melanjutkan pertempuran.")
                        hp_monster_agent += math.floor(0.25*hp_monster_agent) #hp bertambah 25%
                        count_healing += 1
                        item_inventory[perintah][2] = int(item_inventory[perintah][2]) - 1
                    #hp bertambah karena memakai healing potion

            #figth otomatis
            #giliran monster random
            print(f"============ TURN {count_figth} ({monster[random_number][1]}) ============")
            print(f"SCHWINKKK, {monster[random_number][1]} menyerang {monster[index_monster_agent][1]}")
            print()
            #attack didapat dari rgn dalam rentang +- 30% ATK power
            #def power akan menurunkan serangan musuh rentang 0-50%
            hp_monster_agent -= math.floor((1-def_monster_agent/100)*(generate_number(a, c, m, x0, [0.7*int(atk_monster), 1.3*int(atk_monster)])))
            if hp_monster_agent <= 0:
                hp_monster_agent = 0
                print(f"Nama        : {monster[index_monster_agent][1]}")
                print(f"ATK Power   : {atk_monster_agent}")
                print(f"DEF Power   : {def_monster_agent}")
                print(f"HP          : {hp_monster_agent}")
                print(f"Level       : {level_mons_agent}")
                print()
            else:
                print(f"Nama        : {monster[index_monster_agent][1]}")
                print(f"ATK Power   : {atk_monster_agent}")
                print(f"DEF Power   : {def_monster_agent}")
                print(f"HP          : {hp_monster_agent}")
                print(f"Level       : {level_mons_agent}")
                print()

            count_figth += 1
            

        elif choice_figth == '3': #kabur dari battle
            print("Anda berhasil kabur dari BATTLE!")
            break
    return ''