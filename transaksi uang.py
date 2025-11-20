# Variabel Global
dataCatatan = ["Uang Jajan", "Biaya Sekolah", "Tabungan"]
pilihan = ''

# Fungsi Aplikasi
def daftarCatatan():
    return dataCatatan
def tambahCatatan(catatanBaru):
    catatan = dataCatatan
    catatan.append(catatanBaru)
    return catatan

# Aplikasi Utama
print("Hello Selamat Datang Di Aplikasi Bundahara Digital")
# Loop utama aplikasi / Main Application Loop
for x in range(10):
    print("################################################################")
    print("Silahkan Pilih Menu Dibawah Ini:")
    print("1. Lihat Daftar Catatan")
    print("2. Tambah Catatan Baru")
    pilihan = input("Masukkan pilihan Anda (1/2): ")
    print("############~~")
    if pilihan == '1':
        catatan = daftarCatatan()
        print("Daftar Catatan Anda:")
        for idx, nama in enumerate(catatan, start=1):
            print(f"{idx}. {nama}")
    elif pilihan == '2':
        catatanBaru = input("Masukkan nama catatan baru: ")
        catatan = tambahCatatan(catatanBaru)
        print("Catatan berhasil ditambahkan. Daftar Catatan Anda sekarang:")
        for idx, nama in enumerate(catatan, start=1):
            print(f"{idx}. {nama}")
    elif pilihan.lower() == 'exit':
        print("Terima kasih telah menggunakan aplikasi Bundahara Digital. Sampai jumpa!")
        break

    if x == 9:
        print("Anda telah mencapai batas maksimum penggunaan aplikasi dalam satu sesi. Silakan mulai ulang aplikasi jika ingin melanjutkan.")

