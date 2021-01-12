# Program1
## UAS

## Tambah data 
• elif menu.lower() == 't': Ambil data 't' dari menu
    • nama = input("Masukkan nama: ") lalu tambahkan input nama, nim, nilai tugas, nilai uts, nilai uas 
    • nilai_akhir = (nilai_tugas)*30/100 + (nilai_uts)*35/100 + (nilai_uas)*35/100 untuk nilai akhir diambil dari perhitungan 3 komponen nilai(nilai_tugas:30%, nilai_uts:35%, nilai_uas:35%)
    • data[nama] = [nama, nim, nilai_tugas, nilai_uts, nilai_uas, nilai_akhir] kita akan masukkan data yang tadi kita input ke dalam 'data[nama]' • lalu cetak print()

Input:
![Input](foto/inputtambah.png)

## Ubah data 
 • elif menu.lower() == 'u': Ambil data 'u' dari menu
 • nama = input("Masukkan nama untuk mengubah data: ") kita akan menginput data yang nanti akan diubah 
 • if nama in data.keys(): print("Mau mengubah apa?") jika 'nama' dari didalam 'data' maka akan mengembalikan daftar menggunakan daftar menggunakan fungsi 'keys()' 
 • sub_data = input("(semua), (Nama), (NIM),(Tugas), (UTS), (UAS) : ") membuat menu diubah didalam sub_data 
 • if sub_data.lower() =="semua": ambil kata kunci 'semua di dalam sub_data jika 'semua' maka input data[nama][1] = input("Ubah NIM: ")data[nama][2] = int(input("Ubah Nilai Tugas: ")) data[nama][3] = int(input("Ubah Nilai UTS: ")) data[nama][4] = int(input("Ubah Nilai UAS: ")) data[nama][5] = data[nama][2] *30/100 + data[nama][3] + data[nama][4] = int (input("ubah Nilai UAS:")) 
 • data[nama][5] = data[nama][2] *30/100 + data[nama][3]*35/100 + data[nama][4]*35/100 kita dapatkan nilai akhir dengan diambil dari perhitungan 3 komponen nilai(tugas: 30%, uts: 35%, uas: 35%), ket: [5] = nilai_akhir, dimana[0] = nama 
 • lalu cetak print("\Berhasil ubah data!") • Jika kita ingin mengubah data tertentu maka elif sub_data.lower() == "nim":data[nama][1] = input("NIM:") dan berlaku juga untuk nilai tugas, UTS, dan UAS 
 • lalu cetak print("\Berhasil ubah data!") 
 • else:print("'{}' tidak ditemukan.".format(nama)) jika kita salah dalam memasukkan nama untuk mengubah data maka akan muncul 'nama tidak ditemukan'

Input:
![Input1](foto/inputubah.png)
![Input2](foto/inputubah1.png)


 ## Hapus data 
 • elif menu.lower() 'h': Ambil data 'c' dari menu 
 • nama = input("Masukkan nama untuk menghapus sub_data : ") kita akan menginput data yang nanti akan dihapus 
 • if nama in data.keys(): kita mengambil list 'nama' didalam 'data' menggunakan pengkondisian 
 • del data[nama] hapus semua nam yang ada didalam 'data' 
 • jika sudah maka cetak print("sub_data '{}' berhasil dihapus.".format(nama)) 
 • else:print("'{} tidak ditemukan.".format(nama)) jika data yang kita akan input salah/tidak ditemukan maka akan tercetak 'nama tidak ditemukan'

 Input:
![Input3](foto/inputhapus.png)


 ## Cari data 
 • elif menu.lower() == 'c': Ambil data 'c' dari menu 
 • nama = input("Masukkan nama untuk mencari data:") kita akan menginput data yang nanti akan dicari 
 • if nama in data.keys(): kita mengambil list 'nama' didalam 'data' menggunakan pengkondisian 
 • maka cetak print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}" untuk menampilkan data yang tersedia 
 • else:print("'{} tidak ditemukan.".format(nama)) jika data yang kita akan input salah/tidak ditemukan maka akan tercetak 'nama tidak ditemukan'

 Input:
![Input4](foto/inputcari.png)

 
 # Output
 Tambah data:
 ![output](foto/outputtambahdata.png)

 Ubah data:
 ![output1](foto/outputubah.png)

 Hapus data:
 ![output2](foto/outputhapus.png)

 Cari data:
 ![output3](foto/caridata.png)

 ## Mencetak daftar nilai
 if c.lower() == 'i':  Kita menggunakan kondisi percabangan if, ambil data dari menu lalu kita akan mengubah perintah 'i' yang kita input menjadi huruf kecil dengan fungsi lower()
• lalu cetak print()
Input:
![input](foto1/inputdaftarnilai.png)

 Output:
 ![output](foto1/inputnilai.png)
 

# Nama : Muhammad Choeruman Syah
# Kelas : TI.20.A1

![foto](foto/TUGASPRAKTIKUM.png)
Pada tugas LAB 6, saya diminta untuk membuat sebuah program menambahkan data ke sebuah list dengan sistem library root yang nantinya akan seperti ini.
# Berikut inputannya
from data import data

print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
    if c.lower() == 't':
        print("=======Tambah Data=======")
        nama = input("Nama                :  ")
        nim = input("Nim                 :  ")
        tugas = int(input("Masukan Nilai Tugas :  "))
        uts = int(input("Masukan Nilai UTS   :  "))
        uas = int(input("Masukan Nilai UAS   :  "))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim, tugas, uts, uas, akhir
    elif c.lower() == 'u':
        print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim = input('Nim                 :  ')
            tugas = int(input("Masukan Nilai Tugas :  "))
            uts = int(input("Masukan Nilai UTS   :  "))
            uas = int(input("Masukan Nilai UAS   :  "))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Data Nilai Tidak Ada".format(nama))

    elif c.lower() == 'l':
        print("=======Daftar Nilai Mahasiswa=======")
        print("================================================================================================")
        print(" |NO   |     NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        i = 0
        for x in data.items():
            i += 1
            print(
                " | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1],
                                                                                                x[1][2], x[1][3],
                                                                                                x[1][4], i))
            print("============================================================================================")

    elif c.lower() == 'h':
        print("=======Hapus Data Mahasiswa=======")
        nama = input("Nama :  ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data Nilai Tidak Ada".format(nama))

    elif c.lower() == 'k':
        print("Keluar")
        break

# Dan Setelah Kita Menemukan Hasil Nya Mari Saya Jelaskan Perinciannya

* Langkah Pertama Yang Harus Lakukan Adalah kita membuat variable list kosong.
```python
from data import data
•	Setelah itu kita membuat kondisi perulangan dan statement yang akan dijalankan ketika perulangan terjadi. Dan Ini inputannya
print("PROGRAM MENAMPILKAN DAFATR NILAI MAHASISWA")
while True:
    print("")
    c =input("(L)lihat, (T)ambah, (U)bah, (H)apus, (K)eluar : ")
•	Berikutnya tambahkan inputan Fungsi Tambahkan
if c.lower() == 't':
print("=======Tambah Data=======")
        nama = input("Nama                :  ")
        nim = input("Nim                 :  ")
        tugas = int(input("Masukan Nilai Tugas :  "))
        uts = int(input("Masukan Nilai UTS   :  "))
        uas = int(input("Masukan Nilai UAS   :  "))
        akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
        data[nama] = nim, tugas, uts, uas, akhir
•	Tambahkan inputan Fungsi Ubah
elif c.lower() == 'u':
print('=======Ubah Data Mahasiswa=======')
        nama = input('Nama                :  ')
        if nama in data.keys():
            nim = input('Nim                 :  ')
            tugas = int(input("Masukan Nilai Tugas :  "))
            uts = int(input("Masukan Nilai UTS   :  "))
            uas = int(input("Masukan Nilai UAS   :  "))
            akhir = (0.30 * tugas) + (0.35 * uts) + (0.35 * uas)
            data[nama] = nim, tugas, uts, uas, akhir
        else:
            print("Data Nilai Tidak Ada".format(nama))
•	Tambahkan inputan Fungsi Tampilkan
elif c.lower() == 'l':
 print("=======Daftar Nilai Mahasiswa=======")
        print("================================================================================================")
        print(" |NO   |       NAMA      |    NIM    |     TUGAS    |     UTS     |       UAS    |    AKHIR     | ")
        print("================================================================================================")
        i = 0
        for x in data.items():
            i += 1
            print(
                " | {6:2}  |  {0:12s} | {1:9s} | {2:11}  | {3:11} | {4:11}  |  {5:11} |".format(x[0], x[1][0], x[1][1],
                                                                                                x[1][2], x[1][3],
                                                                                                x[1][4], i))
            print("============================================================================================")
•	Tambahkan inputan Fungsi Hapus
elif c.lower() == 'h':
print("=======Hapus Data Mahasiswa=======")
        nama = input("Nama :  ")
        if nama in data.keys():
            del data[nama]
        else:
            print("Data Nilai Tidak Ada".format(nama))
•	Tambahkan inputan Fungsi Keluar
elif c.lower() == 'k':
print("Keluar")
        break




Output :
![output](foto/output.png)

Flowchart :
![flowchart](flowchart/Doc1.docx)


## Cetak hasil pencarian
 • elif menu.lower() == 'c': Ambil data 'c' dari menu 
 • nama = input("Masukkan nama untuk mencari data:") kita akan menginput data yang nanti akan dicari 
 • if nama in data.keys(): kita mengambil list 'nama' didalam 'data' menggunakan pengkondisian 
 • maka cetak print("Nama: {0}\nNIM : {1}\nNilai Tugas: {2}\nUTS: {3}\nUAS: {4}\nNilai akhir: {5}" untuk menampilkan data yang tersedia 
 • else:print("'{} tidak ditemukan.".format(nama)) jika data yang kita akan input salah/tidak ditemukan maka akan tercetak 'nama tidak ditemukan'
 Input:
 ![input](foto1/inputcetakhasil.png)
 Output:
 ![output](foto1/cetakhasilpencarian.png)

 ## Mencetak daftar nilai
  elif menu.lower() == 'l': Kita menggunakan kondisi percabangan if, ambil data dari menu lalu kita akan mengubah perintah 'l' yang kita input menjadi huruf kecil dengan fungsi lower()
• lalu cetak print()
Input:
![input](foto1/inputcekdaftar.png)
Output:
![output1](foto1/cetakdaftarnilai.png)