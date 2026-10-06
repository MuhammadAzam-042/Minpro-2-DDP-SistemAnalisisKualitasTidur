import pwinput
from prettytable import PrettyTable

def lihat(data_tidur):
    tabel = PrettyTable()
    tabel.field_names = ["NO", "HARI", "JAM TIDUR"]
    i = 1
    for h in hari:
        tabel.add_row([i, h, f"{data_tidur[h]} Jam"])
        i += 1
    print(tabel)

def menambah(data_tidur):
    print("\n==Menambah Data Jam Tidurmu jika ada jam yang kosong/belum terisi==")
    tidur_kosong = False
    for h in hari:
        if data_tidur[h] == 0:
            tidur_kosong = True
            tambah_jam = input(f"masukan data jam ke hari yang data jam yang kosong untuk hari {h}: ")
            while not tambah_jam.isdigit():
                print("Input tidak valid! Silakan masukkan angka bulat saja.")
                tambah_jam = input(f"masukan data jam ke hari yang data jam yang kosong untuk hari {h}: ")
            data_tidur[h] = int(tambah_jam)
    if not tidur_kosong:
        print("Semua hari sudah diisi dengan data jam kamu")

def ubah(data_tidur):
    print("\n==Pilih Hari Yang Ingin Diubah==")
    tabel = PrettyTable()
    tabel.field_names = ["NO", "HARI", "JAM TIDUR"]
    i = 1
    for h in hari:
        tabel.add_row([i, h, f"{data_tidur[h]} Jam"])
        i += 1
    print(tabel)

    nomor_hari = input("Masukkan nomor hari (1-7): ")
    if nomor_hari.isdigit() and 1 <= int(nomor_hari) <= 7:
        hari_terpilih = hari[int(nomor_hari) - 1]
        jam_baru = input(f"Masukkan jam tidur baru untuk hari {hari_terpilih}: ")

        while not jam_baru.isdigit():
            print("Input tidak valid! Silakan masukkan angka bulat saja.")
            jam_baru = input(f"Masukkan jam tidur baru untuk hari {hari_terpilih}: ")

        data_tidur[hari_terpilih] = int(jam_baru)
        print(f"Data jam tidur hari {hari_terpilih} berhasil diubah menjadi {jam_baru} jam!")
    else:
        print("Nomor hari tidak valid!")

def hapus(data_tidur):
    print("\n==Pilih hari yang ingin di-reset (dihapus)==")
    tabel = PrettyTable()
    tabel.field_names = ["NO", "HARI", "JAM TIDUR"]
    i = 1
    for h in hari:
        tabel.add_row([i, h, f"{data_tidur[h]} Jam"])
        i += 1
    print(tabel)
    
    nomor_hari = input("Masukkan nomor hari (1-7): ")
    if nomor_hari.isdigit() and 1 <= int(nomor_hari) <= 7:
        hari_terpilih = hari[int(nomor_hari) - 1]
        data_tidur[hari_terpilih] = 0
        print(f"Data jam tidur hari {hari_terpilih} berhasil di-reset menjadi 0 jam!")
    else:
        print("Nomor hari tidak valid!")

def menentukan_kualitas_tidur(rata_rata):
    if rata_rata < 5:
        print("Kualitas tidurmu sangat buruk minggu ini!")
        print("Tidur kurang dari 5 jam dapat memicu penurunan fungsi otak, microsleep, risiko hipertensi, dan penurunan daya tahan tubuh.")
        print("Jadi, tidur yang cukup ya!")

    elif 5 <= rata_rata < 6:
        print("Kualitas tidurmu kurang cukup minggu ini!")
        print("Tidur 5-6 jam Sering menyebabkan kantuk di siang hari, emosi tidak stabil, dan fokus berkurang jika terjadi terus-menerus.")
        print("Tidur yang cukup ya!")

    elif 6 <= rata_rata < 7 and 8 <= rata_rata < 10:
        print("Kualitas tidurmu cukup minggu ini!")
        print("Rata-rata jam tidur ini, Bagi beberapa orang dengan kebutuhan metabolisme atau aktivitas tertentu, meski tidak sepenuhnya optimal.")
        print("Lanjutkan!")

    elif 7 <= rata_rata <= 8:
        print("Kualitas tidurmu sangat baik minggu ini!")
        print("Rata-rata jam tidur ini, Mengoptimalkan pemulihan fisik, konsentrasi, daya ingat, serta kesehatan jantung dan mental.")
        print("Lanjutkan!")

    elif rata_rata >= 10:
        print("Kualitas tidurmu sangat buruk dan berlebihan minggu ini!")
        print("Tidur lebih dari 10 jam bisa menandakan adanya gangguan kesehatan (seperti depresi atau sleep apnea) dan memicu rasa lemas/pusing.")
        print("Silahkan konsultasikan ke dokter!")

database_user = {
    "ariana": {"password": "123", "role": "pengguna premium"},
    "joko": {"password": "321", "role": "pengguna biasa"}
}

hari = ("SENIN", "SELASA", "RABU", "KAMIS", "JUMAT", "SABTU", "MINGGU")

print("====LOGIN ANALISIS KUALITAS JAM TIDUR====")

role_aktif=""
while True:
    username = input("Masukan username anda: ")
    password = pwinput.pwinput("Masukan password anda: ")
    if username in database_user and database_user[username]["password"] == password:
        role_aktif = database_user[username]["role"]
        print(f"\nLogin berhasil! Anda masuk sebagai {role_aktif}.")
        break
    else:
        print("username atau password anda salah! silahkan masukan lagi.")

while True:
    print("Analisis akan dilakukan selama seminggu, jadi 7 hari kedepan silakan masukan jam tidur anda perhari.")
    data_tidur = {}

    for h in hari:
        input_tidur = input(f"Kamu tidur berapa jam di hari {h} ini?: ")
        while not input_tidur.isdigit():
            print("Input tidak valid! Silakan masukkan angka bulat saja.")
            input_tidur = input(f"Kamu tidur berapa jam di hari {h} ini?: ")
        data_tidur[h]=int(input_tidur)

    while True:
        if role_aktif == "pengguna premium":
            print("\n===KELOLA DATA TIDUR MINGGU INI===")
            print("Ketik '1' untuk ingin melihat datamu")
            print("Ketik '2' untuk memasukan jam tidurmu")
            print("Ketik '3' untuk mengubah jam tidur di hari tertentu")
            print("Ketik '4' untuk menghapus jam tidur di hari tertentu")
            print("Ketik '5' untuk lanjut menganalisis jam tidurmu")

            pilihan = input("pilih menu (1-5): ")
            if pilihan == "1":
                lihat(data_tidur)
            elif pilihan == "2":
                menambah(data_tidur)
            elif pilihan == "3":
                ubah(data_tidur)
            elif pilihan == "4":
                hapus(data_tidur)
            elif pilihan == "5":
                break
            else:
                print("Pilihan tidak valid! pilih menu (1-5)")

        elif role_aktif == "pengguna biasa":
            print("\n===KELOLA DATA TIDUR MINGGU INI===")
            print("Ketik '1' untuk ingin melihat datamu")
            print("Ketik '2' untuk lanjut menganalisis jam tidurmu")

            pilihan = input("pilih menu (1/2): ")
            if pilihan == "1":
                lihat(data_tidur)
            elif pilihan == "2":
                break
            else:
                print("Pilihan tidak valid! pilih menu (1-2)")

    total_tidur = 0
    for h in hari:
        total_tidur += data_tidur[h]
    rata_rata = total_tidur / 7

    print(f"Rata-rata jam tidur anda minggu ini: {rata_rata} jam/hari.")
    menentukan_kualitas_tidur(rata_rata)

    ulang = input("Apakah Anda ingin memulai analisis lagi? (ya/tidak): ")
    if ulang != "ya":
        print("Terima kasih telah menggunakan program sistem analisis kualitas jam tidur!")
        break
