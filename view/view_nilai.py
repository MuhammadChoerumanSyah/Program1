data = []
data = {}

print("PROGRAM MENAMPILKAN DAFTAR NILAI MAHASISWA")
while True:
    print("\n")
    menu = input("(T) Tambah_data, (C) Cetak hasil pencarian, (L) Cek daftar nilai: ")
    print("\n")

     # Tambah
    if menu.lower() == 't':
        print("Masukkan data mahasiswa")
        print("...")
        nama = input("Masukkan nama: ")
        nim = input("Masukkan NIM: ")
        nilai_tugas = int(input("Masukkan nilai tugas: "))
        nilai_uts = int(input("Masuukkan nilai UTS: "))
        nilai_uas = int(input("Masukkan nilai UAS: "))
        nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100
        data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir]
        print('\nData berhasil di tambah!')
        print("============================================================================")
        print("| No |           Nama          |     NIM   |TUGAS  | UTS   | UAS   | AKHIR |")
        print("============================================================================")
        no = 1
        for tabel in data.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                (no, tabel[0],
                tabel[1], tabel[2],
                tabel[3], tabel[4], tabel[5]))
    
    # Cek Daftar Nilai
    elif menu.lower() == 'l':
        print("Mencetak Daftar Nilai")
        print("============================================================================")
        print("| No |           Nama          |   Nim     | Tugas | UTS   | UAS   |  Akhir|")
        print("============================================================================")
        no = 1
        for tabel in data.values():
            print("| {0:2} | {1:14} | {2:9} | {3:5} | {4:5} | {5:5} | {6:5} |".format
                 (no, tabel[0],
                  tabel[1],tabel[2],
                  tabel[3], tabel[4], tabel[5]))
            no += 1
            
     # Cetak hasil pencarian   
    elif menu.lower() == 'c':
        print("Mencetak hasi pencarian: ")
        print("=================================================")
        nama = input("Masukkan nama untuk mencari data:")
        if nama in data.keys():
            print('\nResult')
            print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}"
                  .format(nama, data[nama][1],
                                data[nama][2], data[nama][3],
                                data[nama][4], data[nama][5]))
        else:
            print("'{} tidak ditemukan.".format(nama))