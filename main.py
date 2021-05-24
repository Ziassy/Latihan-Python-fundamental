# list

# Tipe Data pada Python - List, Slicing, Tuple, Set, dan Dictionary

# LIST
# list beda dengan array, list ini tidak harus memiliki tipe data yang sama
# []

# list = [1, 2.2, 'pauziah', 'ziah']
# print(list[0]) # access index 0
# print(list[-1]) #access last index
# print(list[1:3]) #access index ke 1 dan 2 doang. 3 nya kaga
#
# # melakukan perubahan data element list
# ubahList = list[2]='ziah'
# print(ubahList)
#
# # penambahan list menggunakan append
# list.append(2)
# print(list)
#
# binatang = ['kucing', 'rusa', 'badak', 'gajah']
# # delete item list menggunakan del()
# del binatang[1]
# print(binatang)
#
# # SLICING pada string
# # mutable (bisa diubah)
#
# s = "Hello World!"
# print(s[4]) 		#ambil karakter kelima dari string s
# print(s[6:11]) 		#ambil karakter ketujuh hingga sebelas dari string s
# s = "Halo Dunia!"	#ubah isi string s menjadi "Halo Dunia!", seharusnya berhasil karena mutable
# print (s)

# TUPLE
# list yang tidak bisa diubah elementnya
# tupleT = (5, 'program tuple', 1 + 3j)
# print(tupleT[1])
# ()
#
# # SET
# # kumpulan item yang bersifat unik dan tanpa urutan (unordered collection)
# # pake kurawal dan di pisah koma
# # Pada Set kita dapat melakukan union dan intersection
# # sekaligus otomatis melakukan penghapusan data duplikat.
# # karena unordered jadinya gak bisa di akses kyak index
# contohSet = {1, 2, 2, 3, 3, 3}
# print(contohSet)  # {1, 2, 3}

# DICTIONARY
# kumpulan pasangan kunci-nilai (pair of key-value) yang bersipat tidak berurutan
# cara mengakses datanya kita harus mengetahui kuncinya (KEY)

# 1. Setiap elemen pair key-value dipisahkan dengan koma (,).
# 2. Key dan Value dipisahkan dengan titik dua (:).
# 3. Key dan Value dapat berupa tipe variabel/obyek apapun.
# {key: value}

# dictionari = {1: 'ini di sebut value', 'key': 2}
# print(type(dictionari))
# print("ambil VALUE dictionary[1] = ", dictionari[1])
# print("ambil KEY dictionary['key'] = ", dictionari['key'])
#
# # Konversi (conversion, cast) antar tipe data
# # int(), float(), str(), set(), tuple(), list(), dict()
# print(float(5))
# print(int(10.6))
# print(float('2.5'))
# print(str(25))
# print(set([1,2,3]))
# print(tuple({5,6,7}))
# print(list('hello'))
# print(dict([(3,26),(4,44)]))


# class Calculator:
#
#     def __init__(self, nilai=0):
#         self.nilai = nilai
#
#     def tambah_angka(self, angka1, angka2):
#         self.nilai = angka1 + angka2
#         if self.nilai > 9:
#             print('Kalkulator sederhana melebihi batas angka: {}'.format(self.nilai))
#         return self.nilai
#
# class CalculatorKali(Calculator):
#     """contoh mewarisi kelas kalkulator sederhana"""
#     def kali_angka(self, angka1, angka2):
#         self.nilai = angka1 * angka2
#         return self.nilai
#
#     def tambah_angka(self, angka1, angka2):
#         self.nilai = angka1 + angka2
#         return self.nilai
#
# kk = CalculatorKali()
# a = kk.kali_angka(2, 3) # sesuai dengan definisi class memiliki fitur kali_angka
# print(a)
#
# b = kk.tambah_angka(5, 6) # memiliki fitur tambah_angka karena mewarisi dari Kalkulator
# print(b)



# mylist = ["apple", "banana", "cherry"]
#
# fruits = 'Pauziah'
#
# mylist.append(fruits) # add single argument to list
# mylist.extend(["watermelon", "melon"]) # Add multiple argument to list
# print(mylist)

# test_dict = {'Name': nama, 'Age': umur, 'Geeks' : 3}
# print(type(test_dict))
#
# # get key and value using for loop
# print('Dict key-value are')
# for getDictionary in test_dict:
#     # getDictionary untuk mendapatkan key nya
#     # test_dict[getDictionary] untuk mendapatkan value nya
#     print(getDictionary, test_dict[getDictionary])

# ========= test dictionary =============
#
# exDictionary = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# getList = exDictionary['colors']
#
#
# print(getList[1])


# Data JSON
# DATA = [
#         {
#             "duration": 395,
#             "risetime": 1568082479
#         },
#         {
#             "duration": 640,
#             "risetime": 1568088118
#         },
#         {
#             "duration": 614,
#             "risetime": 1568093944
#         },
#         {
#             "duration": 555,
#             "risetime": 1568099831,
#         },
#         {
#             "duration": 595,
#             "risetime": 1568105674
#         }
#     ]
#
#
# for d in DATA:
#     # print(d)
#     d['message'] = "aku kwkwk"
#     # print(d)
#
# print(DATA)

rest_list = []

name = 'pauziah'
age = '19'
rest_list.append((name, age))

print(type(rest_list))
print(rest_list)
print(rest_list[1])







