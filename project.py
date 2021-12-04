import os;
import time;
import sys;

class University:

    namaMahasiswa = [];
    nimMahasiswa = [];
    prodiMahasiswa = [];

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
        print('[5] Exit');
        try:
            menu = int(input('\n[-] Masukan Pilihan Anda : '));
            
            if menu == 1:
                self.lihatDataMhs();
            elif menu == 2:
                self.inputDataMahasiswa();
            elif menu == 3:
                self.cariDataMahasiswa();
            elif menu == 4:
                self.hapusMhs();
            elif menu == 5:
                print('\n[-] Exit...');
                time.sleep(1.5);
                sys.exit();
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
        print('Jumlah data mahasiswa : ', len(University.namaMahasiswa))
        print('='*40)
        
        if University.namaMahasiswa == []:
            print('\nNo             Nama                                          Nim                               Prodi');
            print('='*170);
            print('\n\n                             \t\t\t\t\tBelum ada data yang diinput')
            
            try:
                addData = input('                           \t\t\t\t\tIngin input data (Y/N) ? : ');
                if addData == 'y' or addData == 'Y':
                    self.inputDataMahasiswa();
                else:
                    self.menu();
            except KeyboardInterrupt:
                print('\n\n                          \t\t\t\t        Tidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);
                self.lihatDataMhs();
        else:
            number = 1;
            print('\nNo             Nama                                          Nim                               Prodi');
            print('='*170);
            for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
                print('\n',number,   end='     ');
                print(nameMhs,  end='                            ');
                print(nimMhs,   end='                        ');
                print(prodiMhs, end='                 ');
                number += 1

            addDataMahasiswa = input('\n\nTambah data mahasiswa (Y/N) ? : ');
            if addDataMahasiswa == 'y' or addDataMahasiswa == 'Y':
                self.inputDataMahasiswa();
            else:
                self.menu();

    def inputDataMahasiswa(self):
        os.system('cls');
        dataFirst = 0;
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
            for dataMhs in range(dataFirst, dataInputMhs):
                print('\nData Mahasiswa Ke-', dataFirst + 1);
                print('='*25);
                nama  = input('Masukan Nama  : ');
                nim   = input('Masukan Nim   : ');
                prodi = input('Masukan Prodi : ');
            
                University.namaMahasiswa.append(nama);
                University.nimMahasiswa.append(nim);
                University.prodiMahasiswa.append(prodi);

                dataFirst += 1;
            
            try:
                question = input('\nInput data mahasiswa lagi (Y/N) ? : ')
            except KeyboardInterrupt:
                for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
                # for dataMhs in range(dataFirst, dataInputMhs):
                    University.namaMahasiswa.remove(nameMhs);
                    University.nimMahasiswa.remove(nimMhs);
                    University.prodiMahasiswa.remove(prodiMhs);

                print('Data Tidak Tersimpan!');
                print('\nTidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);

                question = input('Input Data Mahasiswa Lagi (Y/N) ? : ');
                if question == 'y' or question == 'Y':
                    self.inputDataMahasiswa();
                else:
                    self.menu();
            else:
                if question == 'y' or question == 'Y':
                    print('\nData Berhasil Tersimpan!!');
                    time.sleep(1.5);
                    self.inputDataMahasiswa();
                else:
                    print('\nData Berhasil Tersimpan!!');
                    time.sleep(1.5);
                    self.menu();

    def cariDataMahasiswa(self):
        benarSalah = False;
        os.system('cls');
        print('\tCari Data Berdasarkan Nama');
        print('='*50)
        
        search = input('Masukan Nama Mahasiswa : ');
        
        for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
            if search == nameMhs or search == nimMhs:
                print('\nNama  : ', nameMhs)
                print('Nim   : ', nimMhs)
                print('Prodi : ', prodiMhs)
                print('\nData Ditemukan!');
                
                benarSalah = True;
                break;

        if benarSalah ==  True:        
            tanya = input('\nCari data mahasiswa lagi (Y/N) ? : ');
            if tanya == 'y' or tanya == 'Y':
                self.cariDataMahasiswa();
            else:
                self.menu();
        else:
            print('\nData Tidak Ditemukan!');
                
            tanya = input('Cari data mahasiswa lagi (Y/N) ? : ');
            if tanya == 'y' or tanya == 'Y':
                self.cariDataMahasiswa();
            else:
                self.menu();
    
    def hapusMhs(self):
        benarSalah = False;
        os.system('cls');
        print('\tHapus Data Berdasarkan Nama/Nim');
        print('='*50)
        
        search = input('Masukan Nama/Nim Mahasiswa : ');
        
        for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
            if search == nameMhs or search == nimMhs:
                University.namaMahasiswa.remove(nameMhs);
                University.nimMahasiswa.remove(nimMhs);
                University.prodiMahasiswa.remove(prodiMhs);
                print('\nData Berhasil Dihapus!');
                
                benarSalah = True;
                break;

        if benarSalah ==  True:        
            tanya = input('\nHapus data mahasiswa lagi (Y/N) ? : ');
            if tanya == 'y' or tanya == 'Y':
                self.hapusMhs();
            else:
                self.menu();
        else:
            print('\nData Gagal Dihapus!');
                
            tanya = input('Hapus data mahasiswa lagi (Y/N) ? : ');
            if tanya == 'y' or tanya == 'Y':
                self.hapusMhs();
            else:
                self.menu();


obj_mahasiswa = University('Mahasiswa', 'Dosen');

obj_mahasiswa.menu();