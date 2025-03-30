
def tampilan_menu():
    print('\n==== program manajemen kontak ====')
    print("1. Tambah Kontak")
    print("2. Lihat Semua Kontak")
    print("3. Cari Kontak")
    print("4. Hapus Kontak")
    print("5. update contact")
    print("6. Keluar")

daftar_kontak = {}

def program():
    while True:
        tampilan_menu()
        
        try:
            pilih_menu = int(input('pilih menu dari 1 - 5 : '))
        except ValueError:
            print('tolong masukkan angka bukan string!!!')
            continue

        if pilih_menu == 1:
            print('-> tambah kontak')
            nama = input('masukkan nama anda ; ').strip()
            no_telp = input('masukkan no telepon anda ; ').strip()

            if nama in daftar_kontak:
                print('maaf data sudah ada, tidak bisa ditambah lagi')
            else: 
                daftar_kontak[nama] = no_telp
                print('data berhasil di masukkan ke daftar kontak')
        elif pilih_menu == 2:
            print('-> lihat semua kontak')
            for key, value in daftar_kontak.items():
                print(f'{key} : {value}')
        elif pilih_menu == 3:
            print('-> cari kontak')
            cari = input('masukan nama kontak yang ingin anda cari ').strip()
            print(daftar_kontak.get(cari, 'data tidak ada'))
        elif pilih_menu == 4:
            print('-> hapus kontak') 
            hapus = input('masukan nama kontak yang ingin di hapus ').strip()       
            
            if hapus in daftar_kontak:
                del daftar_kontak[hapus]
                print('data berhasil di hapus')
            else:
                print('maaf data tidak berhasil dihapus')
        elif pilih_menu == 5:
            print('-> update kontak')
            nama_sebelumnya = input('masukan nama kontak sebelum update ').strip()
            nama_baru = input('masukan nama kontak baru ').strip()
            no_baru = input('masukan nomor telefon baru ').strip()

            daftar_kontak[nama_baru] = daftar_kontak.pop(nama_sebelumnya) + no_baru
            print('data kontak berhasil di update')
            

        elif pilih_menu == 6:
            print('maksih telah menggunakan aplikasi kami')
            break        
        
program()
