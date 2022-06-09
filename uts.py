class kontak:
    def __init__(self, name, nomer):
        self.name = name
        self.nomer = nomer

p1 = kontak("Nama : Johni", "nomer : 08123456789")
p2 =kontak("Nama : rian", "nomer : 08987654321")

namaKontak = ['Naufal', 'Hazim']
noTelepon = ['08123456789', '08987654321']

def tambahKontak():  
    namaKontak.append(input('Nama: '))
    noTelepon.append(input('No Telepon: '))
    print('Kontak berhasil ditambahkan')


print('Selamat datang!')
while True:
    print('---Menu---')
    print('1. Daftar Kontak')
    print('2. Tambah Kontak')
    print('3. Keluar')
    menu = int(input('Pilih Menu: '))
    if menu == 1:
        print(p1.name)
        print(p1.nomer)
        print(p2.name)
        print(p2.nomer)
    elif menu == 2:
        tambahKontak()
    elif menu == 3:
        print('Program selesai, sampai jumpa!')
        break
    else:
        print('Menu tidak tersedia')