import os;
import time;

class University:

    dataMahasiswa = [];

    def __init__(self, mahasiswa, dosen):
        self.mahasiswa = mahasiswa;
        self.dosen = dosen;

    def menu(self):
        os.system('cls');
        print('\tUniversitas Muhammadiyah Prof Dr.Hamka');
        print('='*55);
        print('[1] Lihat Data Mahasiswa');
        print('[2] Input Data Mahasiswa');
        print('[3] Cari Data Mahasiswa');
        print('[4] Hapus Data Mahasiswa');
        menu = int(input('\n[-] Masukan Pilihan Anda : '));
        
        if menu == 1:
            os.system('cls');
            self.lihatDataMhs();
        elif menu == 2:
            os.system('cls');
            self.inputDataMahasiswa();
            

    def lihatDataMhs(self):
        # i = 0;
        # while i <= len(University.dataMahasiswa):
        #     print('Nama  : ', University.dataMahasiswa[i]);
        #     i += 1;
        #     print('Nim   : ', University.dataMahasiswa[i]);
        #     i += 1;
        #     print('Prodi : ', University.dataMahasiswa[i]);
        print(University.dataMahasiswa);


    def inputDataMahasiswa(self):
        dataFirst = 1;
        print('Input Data Mahasiswa');
        print('='*40);
        dataInputMhs = int(input('Masukan Jumlah Yang Akan Diinput : '));

        while dataFirst <= dataInputMhs:
            print('\nData Mahasiswa Ke-', dataFirst);
            print('='*25);
            nama  = input('Masukan Nama : ');
            nim   = input('Masukan Nim : ');
            prodi = input('Masukan Prodi : ');
        
            University.dataMahasiswa.append(nama);
            University.dataMahasiswa.append(nim);
            University.dataMahasiswa.append(prodi);

            dataFirst += 1;

        print('\nData Berhasil Tersimpan!!');
        time.sleep(1.5);
        self.menu();

obj_mahasiswa = University('Mahasiswa', 'Dosen');

obj_mahasiswa.menu();