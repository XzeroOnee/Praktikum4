# NAMA : AGUS SETIAWAN
# NIM : 312310597

print("=================Akses List===================")
list1 = ["a", "b", "c", "d", "e"]
print("Tampilkan element ke-3:", list1[3])
print("Ambil nilai element 2-4:", list1[2:5])
print("Ambil element terakhir:", list1[-1])
print( 44*"=", "\n")

print("=================Ubah Element===================")
list2 = [1, 2, 3, 4, 5]
print(list2)
list2[4] = "Element 4"
print(list2)

print()

list3 = ["Satu", "Dua", "Tiga", "Empat", "Lima"]
print("sebelum di ubah :", list3)
list3[0:6] = [1, 2, 3, 4, 5]
print("Setelah diubah:", list3, "\n")

print("=================Tambah list Element===================")
lista = [1, 2, 3, 4, 5]
print("ListA\n", lista)
listb = [6, 7, 8]
listb.insert(2, lista[0:2])
print("ListB Sesudah di tambahkan:\n", listb, "\n")

listb.append("Timey")
print("ListB :\n", listb, "\n")

listb.extend([10, 12, 14])
print("Menambahkan ListB dengan 3 nilai:\n", listb,"\n")

listN = lista + listb
print("Gabungan listA & ListB:\n", listN)