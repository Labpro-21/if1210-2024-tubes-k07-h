import sys

def keluar(): #keluar program
    quit = False
    while quit == False:
        validasi = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
        if validasi == "n" or "N":
            return 1
        elif validasi == "y" or "Y":
            return 2                                                
        else: #inputan tidak velid
            quit = False