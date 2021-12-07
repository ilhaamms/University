import os; #import clear
import time; #import sleep
import sys; #import exit

# class university
class University:

    # empty list for data mahasiswa
    namaMahasiswa = [];
    nimMahasiswa = [];
    prodiMahasiswa = [];

    # empty list for chekcing data mahasiswa keyboard intterupt
    tempNamaMhs = [];
    tempNimMhs = [];
    tempProdiMhs = [];

    # constructor must(wajib) have self in parameter
    def __init__(self, mahasiswa, dosen):
        self.mahasiswa = mahasiswa;
        self.dosen = dosen;

    # method menu, and all method must(wajib) have self in parameter
    def menu(self):
        os.system('cls');
        print('\tUniversitas Muhammadiyah Prof Dr.Hamka');
        print('='*55);
        print('[1] Lihat Data Mahasiswa');
        print('[2] Input Data Mahasiswa');
        print('[3] Cari Data Mahasiswa');
        print('[4] Hapus Data Mahasiswa');
        print('[5] Exit');
        
        # try for checking error, and block try for statement 
        try:
            menu = int(input('\n[-] Masukan Pilihan Anda : '));
            
            if menu == 1:
                self.lihatDataMhs(); #call method with self
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

        # except for checking error tipe data 
        except ValueError:
            print('\n[!] Harap Masukan Angka!');
            time.sleep(1.5);
            self.menu();

        # except for checking error ctrl + c 
        except KeyboardInterrupt:
            print('\n\n[!]Tidak Boleh Mencet Ctrl + C');    
            time.sleep(1.5);
            self.menu();

    # method lihat data mahasiswa
    def lihatDataMhs(self):
        os.system('cls');
        print('Lihat Data Mahasiswa')
        print('Jumlah data mahasiswa : ', len(University.namaMahasiswa))
        print('='*40)
        
        # checking if list empty
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

    # method input data mahasiswa
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

                # append for adding list int last list
                University.tempNamaMhs.append(nama);
                University.tempNimMhs.append(nim);
                University.tempProdiMhs.append(prodi);

                dataFirst += 1;

            try:
                question = input('\nInput Data Mahasiswa Lagi (Y/N) ? : ');
            except KeyboardInterrupt:

                os.system('cls');
                
                print('Masukan Jumlah Yang Akan Diinput : ', dataInputMhs);
                number = 1;
                # showing all list using for loop with zip, and tempNamaMhs, tempNimMhs, tempProdiMhs is string in item data list
                for tempNamaMhs, tempNimMhs, tempProdiMhs in zip(University.tempNamaMhs, University.tempNimMhs, University.tempProdiMhs):
                    print('\nData Mahasiswa Ke-', number);
                    print('='*25);
                    print('\nMasukan Nama  : ', tempNamaMhs);
                    print('Masukan Nim   : ', tempNimMhs);
                    print('Masukan Prodi : ', tempProdiMhs);
                    number += 1;

                # method clear for empty item all data in list
                University.tempNamaMhs.clear();
                University.tempNimMhs.clear();
                University.tempProdiMhs.clear();

                print('\nData tidak tersimpan!!');
                print('\nTidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);
                
                tanya = input('\nInput Data Mahasiswa Lagi (Y/N) ? : ');
                if tanya == 'y' or tanya == 'Y':
                    self.inputDataMahasiswa();
                else:
                    self.menu();

            # block else in block try except is if not error
            else:
                if question == 'y' or question == 'Y':
                    
                    # adding two list with plus
                    University.namaMahasiswa = University.namaMahasiswa + University.tempNamaMhs; 
                    University.nimMahasiswa = University.nimMahasiswa + University.tempNimMhs; 
                    University.prodiMahasiswa = University.prodiMahasiswa + University.tempProdiMhs; 
                    
                    University.tempNamaMhs.clear();
                    University.tempNimMhs.clear();
                    University.tempProdiMhs.clear();

                    print('\nData Berhasil Tersimpan!!');
                    time.sleep(1.5);
                    self.inputDataMahasiswa();

                else:

                    University.namaMahasiswa = University.namaMahasiswa + University.tempNamaMhs; 
                    University.nimMahasiswa = University.nimMahasiswa + University.tempNimMhs; 
                    University.prodiMahasiswa = University.prodiMahasiswa + University.tempProdiMhs; 
                    
                    University.tempNamaMhs.clear();
                    University.tempNimMhs.clear();
                    University.tempProdiMhs.clear();

                    print('\nData Berhasil Tersimpan!!');
                    time.sleep(1.5);
                    self.menu();

    # method cari data mahasiswa
    def cariDataMahasiswa(self):
        # declare variabel boolean for checking search data true or false
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
                
                # if name or nim true, break
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
    
    # method hapus data mahasiswa
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


# in constructor have two parameter mahasiswa and dosen
# in create objek free insert in parameter string anything, because contsructor have two parameter
obj_mahasiswa = University('Mahasiswa', 'Dosen');

# call method menu in objek obj_mahasiswa
obj_mahasiswa.menu();