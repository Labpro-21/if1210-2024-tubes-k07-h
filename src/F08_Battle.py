import math

def printstats(monster_array, monster_level):
    print(f"Name      : {monster_array[1]}")
    print(f"ATK Power : {monster_array[2]}")
    print(f"DEF Power : {monster_array[3]}")
    print(f"HP        : {monster_array[4]}")
    print(f"Level     : {monster_level}")
    

def battle(enemy_level,user_id,isarena,OC_arena,ally_array,ally_level,monster,monster_inventory,item_inventory,user):
    from src.F00_RNG import LCGRNG
    #MONSTER MUNCUL
    lcg = LCGRNG()
    enemy_id = lcg.generate_number([1, len(monster)])
    enemy_array = []
    for i in range (len(monster)):
        if monster[i][0] == str(enemy_id):
            for j in range(5):
                enemy_array.append(monster[i][j])

    if enemy_level == 0:
        enemy_level = lcg.generate_number([1,5])
    for i in range(2,len(enemy_array)):
        enemy_array[i] = math.floor(int(enemy_array[i])+int(enemy_array[i])*(enemy_level-1)*10/100)

    print("""
           _/\----/\   
          /         \     /\ 
         |  O    O   |   |  |
         |  .vvvvv.  |   |  |
         /  |     |   \  |  |
        /   `^^^^^'    \ |  |
      ./  /|            \|  |_
     /   / |         |\__     /
     \  /  |         |   |__|
      `'   |  _      |
        _.-'-' `-'-'.'_
   __.-'               '-.__""")
    print(f"RAWRRR, Monster {enemy_array[1]} telah muncul !!!")
    printstats(enemy_array,enemy_level)
    print("")

    if isarena != True:
        print("============ MONSTER LIST ============")
        monster_pick = []
        monster_no = 1
        for i in range(len(monster_inventory)):
            if monster_inventory[i][0] == str(user_id):
                for j in range(len(monster)):
                    if monster[j][0] == monster_inventory[i][1]:
                        print(f"{monster_no}. {monster[j][1]}")
                        monster_no += 1
                        monster_pick.append([monster_inventory[i][1], monster_inventory[i][2]])
        
        monster_pick_input = int(input("Pilih monster untuk bertarung: "))
        while (monster_pick_input >= monster_no) or (monster_pick_input < 1):
            print("")
            print("Pilihan nomor tidak tersedia!")
            print("")
            monster_pick_input = int(input("Pilih monster untuk bertarung: "))

        ally_array = []
        for i in range(len(monster)):
            if monster[i][0] == str(monster_pick[monster_pick_input-1][0]):
                for j in range(5):
                    ally_array.append(monster[i][j])
                ally_level = int(monster_pick[monster_pick_input-1][1])
                break
        
        for i in range(2,len(ally_array)):
            ally_array[i] = math.floor(int(ally_array[i])+int(ally_array[i])*(ally_level-1)*10/100)
        
        ally_maxhp = ally_array[4]

        print("""
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
""")
        print(f"RAWRRR, Agent X mengeluarkan monster {ally_array[1]} !!!")
        printstats(ally_array,ally_level)
    
    damage_dealt = 0
    damage_received = 0
    potion_used = [0,0,0]
    turn = 1
    over = False
    while over != True:
        print(f"============ TURN {turn} ({ally_array[1]}) ============")
        print("")
        print("1. Attack")
        print("2. Use Potion")
        print("3. Quit")
        
        command = int(input("Pilih perintah: "))
        while (command > 3) or (command < 1):
            print("")
            print("Pilihan nomor tidak tersedia!")
            print("")
            command = int(input("Pilih perintah: "))

        if command == 1:
            print("")
            print(f"SCHWINKKK, {ally_array[1]} menyerang {enemy_array[1]} !!!")
            print("")
            #Perhitungan ATK
            atk_rng = lcg.generate_number([-30, 30])
            atk = ally_array[2] + ally_array[2] * atk_rng/100
            atk_def = atk * enemy_array[3] / 100
            init_health = enemy_array[4]
            enemy_array[4] = math.floor(enemy_array[4] - atk + atk_def)
            atk_res = init_health - enemy_array[4]
            print(f"Attack {atk} + ({atk_rng})%, Reduced by {atk_def} ({enemy_array[3]}%), Attack result {atk_res}.")
            if enemy_array[4] <= 0:
                enemy_array[4] = 0
            damage_dealt += atk_res
            
            printstats(enemy_array,enemy_level)
            print("")

            if enemy_array[4] == 0 and isarena == False:
                print(f"Selamat, Anda berhasil mengalahkan monster {enemy_array[1]}")
                print("")
                OWCA = lcg.generate_number([15,30])
                print(f"Total OC yang diperoleh : {OWCA}")
                user[int(user_id)][4] = int(user[int(user_id)][4]) + OWCA
                over = True
                break

            elif enemy_array[4] == 0 and isarena == True:
                print(f"Selamat, Anda berhasil mengalahkan monster {enemy_array[1]}")
                print("")
                print(f"STAGE CLEARED! Anda akan mendapatkan {OC_arena} OC pada sesi ini!")
                over = False
                return [over, damage_dealt, damage_received]

            print(f"============ TURN {turn} ({enemy_array[1]}) ============")
            print("")
            print(f"SCHWINKKK, {enemy_array[1]} menyerang {ally_array[1]} !!!")
            print("")
            #Perhitungan ATK
            atk_rng = lcg.generate_number([-30, 30])
            atk = enemy_array[2] + enemy_array[2] * atk_rng/100
            atk_def = atk * ally_array[3] / 100
            init_health = ally_array[4]
            ally_array[4] = math.floor(ally_array[4] - atk + atk_def)
            atk_res = init_health - ally_array[4]
            print(f"Attack {atk} + ({atk_rng})%, Reduced by {atk_def} ({ally_array[3]}%), Attack result {atk_res}.")
            if ally_array[4] <= 0:
                ally_array[4] = 0
            damage_received += atk_res

            printstats(ally_array,ally_level)
            print("")

            if ally_array[4] == 0:
                print(f"Yahhh, Anda dikalahkan monster {enemy_array[1]}. Jangan menyerah, coba lagi !!!")
                over = True
                return [over, damage_dealt, damage_received]
            
            turn += 1
        elif command == 2:
            print("")
            print("============ Potion ============")
            potion_matrix = []
            potion_count = 0
            for i in range(len(item_inventory)): 
                if item_inventory[i][0] == str(user_id) and int(item_inventory[i][2]) != 0:
                    if item_inventory[i][1] == "Strength Potion":
                        print(f"{potion_count+1}. {item_inventory[i][1]} (Qty: {item_inventory[i][2]}) - Increases ATK Power")
                    elif item_inventory[i][1] == "Healing Potion":
                        print(f"{potion_count+1}. {item_inventory[i][1]} (Qty: {item_inventory[i][2]}) - Restores Health")
                    elif item_inventory[i][1] == "Resilience Potion":
                        print(f"{potion_count+1}. {item_inventory[i][1]} (Qty: {item_inventory[i][2]}) - Increases DEF Power")
                    potion_count+=1
                    potion_matrix.append(item_inventory[i])
            print(f"{potion_count+1}. Cancel")
            if potion_count == 0:
                print("Anda tidak memiliki Potion dalam inventory!")
            else:
                potion_pick = int(input("Pilih perintah: "))
                while (potion_pick > potion_count+1) or (potion_pick < 1):
                    print("")
                    print("Pilihan nomor tidak tersedia!")
                    print("")
                    potion_pick = int(input("Pilih perintah: "))

                while potion_pick != (potion_count + 1):
                    if potion_matrix[potion_pick-1][1] == "Strength Potion":
                        if potion_used[potion_pick-1] == 0:
                            ally_array[2] = math.floor(ally_array[2] + ally_array[2]*5/100)
                            potion_used[potion_pick-1] += 1
                            print("Potion Berhasil Digunakan")
                            for i in range(len(item_inventory)):
                                if item_inventory[i][0] == user_id and item_inventory[i][1] == "Strength Potion":
                                    item_inventory[i][2] = int(item_inventory[i][2]) -1 

                        else:
                            print(f"Kamu mencoba memberikan ramuan ini kepada {ally_array[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            break
                    elif potion_matrix[potion_pick-1][1] == "Resilience Potion":
                        if potion_used[potion_pick-1] == 0:
                            ally_array[3] = math.floor(ally_array[3] + ally_array[3]*5/100)
                            potion_used[potion_pick-1] += 1
                            print("Potion Berhasil Digunakan")
                            for i in range(len(item_inventory)):
                                if item_inventory[i][0] == user_id and item_inventory[i][1] == "Resilience Potion":
                                    item_inventory[i][2] = int(item_inventory[i][2]) -1 
                        else:
                            print(f"Kamu mencoba memberikan ramuan ini kepada {ally_array[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            break
                    elif potion_matrix[potion_pick-1][1] == "Healing Potion":
                        if potion_used[potion_pick-1] == 0:
                            ally_array[4] = math.floor(ally_array[4] + ally_maxhp*25/100)
                            if ally_array[4] >= ally_maxhp:
                                ally_array[4] = ally_maxhp
                            potion_used[potion_pick-1] += 1
                            print("Potion Berhasil Digunakan")
                            for i in range(len(item_inventory)):
                                if item_inventory[i][0] == user_id and item_inventory[i][1] == "Healing Potion":
                                    item_inventory[i][2] = int(item_inventory[i][2]) -1 
                        else:
                            print(f"Kamu mencoba memberikan ramuan ini kepada {ally_array[1]}, namun dia menolaknya seolah-olah dia memahami ramuan tersebut sudah tidak bermanfaat lagi.")
                            break

                    print(f"============ TURN {turn} ({enemy_array[1]}) ============")
                    print("")
                    print(f"SCHWINKKK, {enemy_array[1]} menyerang {ally_array[1]} !!!")
                    print("")
                    #Perhitungan ATK
                    atk_rng = lcg.generate_number([-30, 30])
                    atk = enemy_array[2] + enemy_array[2] * atk_rng/100
                    atk_def = atk * ally_array[3] / 100
                    init_health = ally_array[4]
                    ally_array[4] = math.floor(ally_array[4] - atk + atk_def)
                    atk_res = init_health - ally_array[4]
                    print(f"Attack {atk} + ({atk_rng})%, Reduced by {atk_def} ({ally_array[3]}%), Attack result {atk_res}.")
                    if ally_array[4] <= 0:
                        ally_array[4] = 0

                    damage_received += atk_res

                    printstats(ally_array,ally_level)
                    print("")

                    if ally_array[4] == 0:
                        print(f"Yahhh, Anda dikalahkan monster {enemy_array[1]}. Jangan menyerah, coba lagi !!!")
                        return [over, damage_dealt, damage_received]

                    turn += 1
                    break

        else: #Command == 3
            if isarena == False:
                over = True
                print("Anda berhasil kabur dari BATTLE!")
                break
            elif isarena == True:
                over = True
                print("GAME OVER! Anda mengakhiri sesi latihan!")
                return [over, damage_dealt, damage_received]
