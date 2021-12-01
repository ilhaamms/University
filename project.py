import os;
import time;

class University:

    namaMahasiswa = [];
    nimMahasiswa = [];
    prodiMahasiswa = [];
    countMahasiswa = 0;

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
        try:
            menu = int(input('\n[-] Masukan Pilihan Anda : '));
            
            if menu == 1:
                os.system('cls');
                self.lihatDataMhs();
            elif menu == 2:
                os.system('cls');
                self.inputDataMahasiswa();
            else:
                print('\n[!] Pilihan Anda Salah!');
                time.sleep(1.5);
                os.system('cls');
                self.menu();
        except ValueError:
            print('\n[!] Harap Masukan Angka!');
            time.sleep(1.5);
            os.system('cls');
            self.menu();
        except KeyboardInterrupt:
            print('\n\n[!]Tidak Boleh Mencet Ctrl + C');    
            time.sleep(1.5);
            os.system('cls');
            self.menu();

    def lihatDataMhs(self):
        print('Data Mahasiswa')
        print('Jumlah data mahasiswa : ', University.countMahasiswa)
        print('='*40)
        
        for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
            print('\nNama  : ', nameMhs)
            print('Nim   : ', nimMhs)
            print('Prodi : ', prodiMhs)
            University.countMahasiswa += 1;

    def inputDataMahasiswa(self):
        dataFirst = 1;
        print('\tInput Data Mahasiswa');
        print('='*40);
        try:
            dataInputMhs = int(input('Masukan Jumlah Yang Akan Diinput : '));
        except ValueError:
            print('\nHarap Masukan Angka!');
            time.sleep(1.5);
            os.system('cls');
            self.inputDataMahasiswa();

        except KeyboardInterrupt:
            print('\n\nTidak Boleh Mencet Ctrl + C');    
            time.sleep(1.5);
            os.system('cls');
            self.inputDataMahasiswa();
        else:
            while dataFirst <= dataInputMhs:
                print('\nData Mahasiswa Ke-', dataFirst);
                print('='*25);
                nama  = input('Masukan Nama  : ');
                nim   = input('Masukan Nim   : ');
                prodi = input('Masukan Prodi : ');
            
                University.namaMahasiswa.append(nama);
                University.nimMahasiswa.append(nim);
                University.prodiMahasiswa.append(prodi);

                dataFirst += 1;

            print('\nData Berhasil Tersimpan!!');
            time.sleep(1.5);
            self.menu();

obj_mahasiswa = University('Mahasiswa', 'Dosen');

obj_mahasiswa.menu();