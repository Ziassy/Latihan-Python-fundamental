# list

# Tipe Data pada Python - List, Slicing, Tuple, Set, dan Dictionary

# LIST
# list beda dengan array, list ini tidak harus memiliki tipe data yang sama
list = [1, 2.2, 'pauziah', 'ziah']
print(list[0]) # access index 0
print(list[-1]) #access last index
print(list[1:3]) #access index ke 1 dan 2 doang. 3 nya kaga

# melakukan perubahan data element list
ubahList = list[2]='ziah'
print(ubahList)

# penambahan list menggunakan append
list.append(2)
print(list)

binatang = ['kucing', 'rusa', 'badak', 'gajah']
# delete item list menggunakan del()
del binatang[1]
print(binatang)

