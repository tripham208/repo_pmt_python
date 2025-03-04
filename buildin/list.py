list_a = [1, 2, 3, 4]

list_b = list_a[:]  # copy list

del list_b[0]  # del element with index 0

if __name__ == '__main__':
    list_b[1] = 5
    print(list_a, list_b)
