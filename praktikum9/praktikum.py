# NAMA : AGUS SETIAWAN
# NIM : 312310597


data = []
no = 0


while True:
    nama = str(input("Nama: "))
    nim = int(input("NIM: "))
    tugas = float(input("Nilai Tugas: "))
    uts = float(input("Nilai UTS: "))
    uas = float(input("Nilai UAS: "))
    no += 1

    hasil = tugas * 0.3 + uts * 0.35 + uas * 0.35

    data.append([no, nama, nim, tugas, uts, uas, hasil])

    add_data = input("Tambah data? (y/t) ")
    if add_data.lower() == 't':
        break

print("="*90)
print("|{:^88}|".format("DAFTAR NILAI MAHASISWA"))
print("="*90)
print("|{:^5}|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|{:^17}|".format("NO", "NAMA", "NIM", "Tugas", "UTS", "UAS", "HASIL"))
print("="*90)

for item in data:
    print("|{:^5}|{:^20}|{:^10}|{:^10}|{:^10}|{:^10}|{:^17.2f}|".format(item[0], item[1], item[2], item[3], item[4], item[5], item[6]))
print("="*90)