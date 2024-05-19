def arena (user_id,monster_inventory,monster,user,item_inventory):
    from src.F08_Battle import printstats,battle
    import math
    print("Selamat datang di Arena!!")
    print("")
    print("MONSTER LIST")

    # print monster list
    monster_list = []
    monster_stats = []
    monster_count = 0
    for i in range (len(monster_inventory)):
        if monster_inventory[i][0] == str(user_id):
            monster_count += 1
            monster_list.append(monster_inventory[i])
            for j in range(len(monster)):
                if monster[j][0] == monster_inventory[i][1]:
                    monster_stats.append(monster[i])
                    print(f"{monster_count}. {monster_stats[monster_count-1][1]}")
                    break

    monster_pick = int(input("Pilih monster untuk bertarung: "))
    pick_valid = False
    while pick_valid == False:
        if monster_pick > monster_count or monster_pick < 0:
            print("Pilihan nomor tidak tersedia!")
        else: break

    ally_array = []
    for i in range(5):
        ally_array.append(monster_stats[monster_pick-1][i])
    ally_level = monster_list[monster_pick-1][2]
    ally_restore = ally_array[4]

    for i in range(2,len(ally_array)):
        ally_array[i] = math.floor(int(ally_array[i])+int(ally_array[i])*(int(ally_level)-1)*10/100)    

    print(f"RAWRRR, Agent {user[int(user_id)][1]} mengeluarkan monster {ally_array[1]}")
    print()
    printstats(ally_array,ally_level)
    print("")
    isarena = True

    total_reward = 0
    total_stage = 0
    damage_dealt = 0
    damage_received = 0
    for i in range(5):
        print("")
        print(f"============= STAGE {i+1} =============")

        reward = [20, 50, 90, 140, 200]

        temp = battle(i+1,user_id,True,reward[i],ally_array,ally_level,monster,monster_inventory,item_inventory,user)

        if temp[0] == True:
            print("")
            damage_dealt += temp[1]
            damage_received += temp[2]
            break

        

        user[int(user_id)][3] = int(user[int(user_id)][4]) + reward[i]
        total_reward += reward[i]
        total_stage += 1
        damage_dealt += temp[1]
        damage_received += temp[2]

        ally_array[4] = int(ally_restore)

    print("============== STATS ==============")
    print(f"Total hadiah        : {total_reward} OC")
    print(f"Jumlah stage        : {total_stage}")
    print(f"Damage diberikan    : {damage_dealt}")
    print(f"Damage diterima     : {damage_received}")


    