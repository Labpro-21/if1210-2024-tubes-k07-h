import os
import time

# nilai a, c, dan m pilih salah satu dari wikipedia
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

# random angka berdasarkan range yang diminta
# contoh penggunaan
# print(generate_number(a, c, m, x0, [0, 3]))
