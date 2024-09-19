c1 = [1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1]
d1 = [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]
ls_array = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
pc2 = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]

def shift_left(arr, n):
    return arr[n:] + arr[:n]

c1s = c1[:]
d1s = d1[:]

for i in range(16):
    iteration_count = ls_array[i]
    c1s = shift_left(c1s, iteration_count)
    d1s = shift_left(d1s, iteration_count)

def permute_pc2(c, d, pc2):
    combined = c + d
    permuted_key = [combined[index - 1] for index in pc2]
    return permuted_key

key = permute_pc2(c1s, d1s, pc2)

print("Chave calculada:", key)
print("Comprimento da chave:", len(key))
