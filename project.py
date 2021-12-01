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

    def cariDataMahasiswa(self):
        os.system('cls');
        # University.namaMahasiswa.sort();
        print('\tCari Data Berdasarkan Nama');
        print('='*50)
        
        search = input('Masukan Nama Mahasiswa : ');
        
        for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
            if search == nameMhs:
                print('\nNama  : ', nameMhs)
                print('Nim   : ', nimMhs)
                print('Prodi : ', prodiMhs)
            else:
                print('\nData Tidak Ditemukan!');
                tanya = input('Cari data mahasiswa lagi (Y/N) ? : ');

                if tanya == 'y' or tanya == 'Y':
                    self.cariDataMahasiswa();
                else:
                    self.menu();

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
            elif menu == 3:
                os.system('cls');
                self.cariDataMahasiswa();

            else:
                print('\n[!] Pilihan Anda Salah!');
                time.sleep(2);
                self.menu();

        except ValueError:
            print('\n[!] Harap Masukan Angka!');
            time.sleep(1.5);
            self.menu();
        except KeyboardInterrupt:
            print('\n\n[!]Tidak Boleh Mencet Ctrl + C');    
            time.sleep(1.5);
            self.menu();

    def lihatDataMhs(self):
        os.system('cls');
        print('Lihat Data Mahasiswa')
        print('Jumlah data mahasiswa : ', University.countMahasiswa)
        print('='*40)
        
        if University.namaMahasiswa == []:
            print('\n\n     Belum ada data yang diinput')
            
            try:
                addData = input('   Ingin input data (Y/N) ? : ');
                if addData == 'y' or addData == 'Y':
                    self.inputDataMahasiswa();
                else:
                    self.menu();
            except KeyboardInterrupt:
                print('\n\n    Tidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);
                self.lihatDataMhs();
        else:
            # University.namaMahasiswa.sort();
            number = 1;
            print('\nNo \t\t\tNama \t\t\t Nim \t\t\t Prodi');
            print('='*100);
            for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
                print('\n',number,   end='\t\t\t');
                print(nameMhs,  end='\t\t\t');
                print(nimMhs,   end='\t\t\t');
                print(prodiMhs, end='\t\t\t');
                number += 1

            addDataMahasiswa = input('\n\nTambah data mahasiswa (Y/N) ? : ');
            if addDataMahasiswa == 'y' or addDataMahasiswa == 'Y':
                self.inputDataMahasiswa();
            else:
                self.menu();

    def inputDataMahasiswa(self):
        os.system('cls');
        dataFirst = 1;
        print('\tInput Data Mahasiswa');
        print('='*40);
        try:
            dataInputMhs = int(input('Masukan Jumlah Yang Akan Diinput : '));
        except ValueError:
            print('\nHarap Masukan Angka!');
            time.sleep(1.5);
            self.inputDataMahasiswa();

        except KeyboardInterrupt:
            print('\n\nTidak Boleh Mencet Ctrl + C');    
            time.sleep(1.5);
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
            question = input('Input data mahasiswa lagi (Y/N) ? : ')

            if question == 'y' or question == 'Y':
                self.inputDataMahasiswa();
            else:
                self.menu();

obj_mahasiswa = University('Mahasiswa', 'Dosen');

obj_mahasiswa.menu();