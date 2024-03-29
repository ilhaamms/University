import os; #import for clear
import time; #import for sleep
import sys; #import for exit
from prettytable import PrettyTable


# class university
class University:
# tes

    # empty list for data mahasiswa
    namaMahasiswa = [];
    nimMahasiswa = [];
    prodiMahasiswa = [];

    # empty list for chekcing data mahasiswa keyboard intterupt
    tempNamaMhs = [];
    tempNimMhs = [];
    tempProdiMhs = [];
    
    # using pretytable for neat(rapih) a data
    global tabelSiswa
    tabelSiswa = PrettyTable(["Nama", "Nim", "Prodi"])

    # constructor must(wajib) have self in parameter
    def __init__(self, nama, nim, prodi):
        self.nama = nama;
        self.nim = nim;
        self.prodi = prodi;

    # method menu, and all method must(wajib) have self in parameter
    def menu(self):
        os.system('cls');
        print('\t\tUniversitas Indonesia');
        print('='*55);
        print('[1] Lihat Data Mahasiswa');
        print('[2] Input Data Mahasiswa');
        print('[3] Cari Data Mahasiswa');
        print('[4] Hapus Data Mahasiswa');
        print('[5] Ubah Data Mahasiswa');
        print('[6] Exit');
        
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
                self.ubahDataMahasiswa();
            elif menu == 6:
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
            print('\nBelum ada data yang diinput')
            
            try:
                addDataMahasiswa = input('\nTambah data mahasiswa (Y/N) ? : ');
            except KeyboardInterrupt:
                print('\n[!]Tidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);
                self.lihatDataMhs();
            # blcok else ekesepsi for block not anything error
            else:
                if addDataMahasiswa == 'y' or addDataMahasiswa == 'Y':
                    self.inputDataMahasiswa();
                elif addDataMahasiswa == 'n' or addDataMahasiswa == 'N':
                    self.menu();
                else:
                    print('\t[!]Jangan Masukan Angka Atau Huruf Lain Selain Y/N !');
                    time.sleep(1.5);
                    self.lihatDataMhs();
        else:
            # sort table data by name
            tabelSiswa.sortby = 'Nama'
            # print variabel tabelsiswa for show all data in table
            print(tabelSiswa)

            try:
                addDataMahasiswa = input('\nTambah data mahasiswa (Y/N) ? : ');
            except KeyboardInterrupt:
                print('\n[!]Tidak Boleh Mencet Ctrl + C');
                time.sleep(1.5);
                self.lihatDataMhs();
            else:
                if addDataMahasiswa == 'y' or addDataMahasiswa == 'Y':
                    self.inputDataMahasiswa();
                elif addDataMahasiswa == 'n' or addDataMahasiswa == 'N':
                    self.menu();
                else:
                    print('\t[!]Jangan Masukan Angka Atau Huruf Lain Selain Y/N !');
                    time.sleep(1.5);
                    self.lihatDataMhs();

    # method chek input data User
    def cekDataUser(self):
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
        print('\n[!]Jangan Masukan Angka atau Huruf Selain Y/N!');
        time.sleep(1.5);
                
        tanya = input('\nInput Data Mahasiswa Lagi (Y/N) ? : ');
        if tanya == 'y' or tanya == 'Y':
            self.inputDataMahasiswa();
        else:
            self.menu();

    # method input data mahasiswa
    def inputDataMahasiswa(self):
        os.system('cls');
        dataFirst = 0;
        print('\tInput Data Mahasiswa');
        print('='*40);
        
        global dataInputMhs;
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
                self.nama  = input('Masukan Nama  : ');
                self.nim   = input('Masukan Nim   : ');
                self.prodi = input('Masukan Prodi : ');

                # append for adding list int last list
                University.tempNamaMhs.append(self.nama);
                University.tempNimMhs.append(self.nim);
                University.tempProdiMhs.append(self.prodi);
                
                dataFirst += 1;

            try:
                global question;
                print('\nData Berhasil Terinput')
                question = input('Simpan Data Mahasiswa (Y/N) ? : ');
            except KeyboardInterrupt:
                os.system('cls');

                print('\tInput Data Mahasiswa');
                print('='*40);
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

            # block else in block try except is if not error anything
            else:
                number = 1;
                if question == 'y' or question == 'Y':
                    
                    for tempNamaMhs, tempNimMhs, tempProdiMhs in zip(University.tempNamaMhs, University.tempNimMhs, University.tempProdiMhs):

                        tabelSiswa.add_row([tempNamaMhs.title(), tempNimMhs, tempProdiMhs.title()])
                        number += 1;

                    # adding two list with plus
                    University.namaMahasiswa = University.namaMahasiswa + University.tempNamaMhs; 
                    University.nimMahasiswa = University.nimMahasiswa + University.tempNimMhs; 
                    University.prodiMahasiswa = University.prodiMahasiswa + University.tempProdiMhs; 
                    
                    University.tempNamaMhs.clear();
                    University.tempNimMhs.clear();
                    University.tempProdiMhs.clear();

                    print('\nData Berhasil Tersimpan!!');
                    time.sleep(1.5);
                    question = input('Input Data Mahasiswa Lagi (Y/N) ? : ')
                    if question == 'y' or question == 'Y':
                        self.inputDataMahasiswa()
                    else:
                        self.menu()

                elif question == 'n' or question == 'N':

                    University.tempNamaMhs.clear();
                    University.tempNimMhs.clear();
                    University.tempProdiMhs.clear();

                    print('\nData Tidak Tersimpan!!');
                    time.sleep(1.5);

                    question = input('Input Data Mahasiswa Lagi (Y/N) ? : ')
                    if question == 'y' or question == 'Y':
                        self.inputDataMahasiswa()
                    else:
                        self.menu()

                else:
                    self.cekDataUser();

    # method cari data mahasiswa
    def cariDataMahasiswa(self):
        # declare variabel boolean for checking search data true or false
        benarSalah = False;
        os.system('cls');
        print('\t     Cari Data Mahasiswa');
        print('\tCari Data Berdasarkan Nama/Nim');
        print('='*50)
        
        search = input('Masukan Nama Mahasiswa : ');

        for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
            # search and name upper/capital with method upper()
            if search.upper() == nameMhs.upper() or search == nimMhs:
                print('\nNama  : ', nameMhs.title())
                print('Nim   : ', nimMhs.title())
                print('Prodi : ', prodiMhs.title())
                print('\nData Ditemukan!');
                
                # if name or nim true, break(out of loop)
                benarSalah = True;
                break;

        if benarSalah ==  True:
            try:
                tanya = input('\nCari data mahasiswa lagi (Y/N) ? : ');
            except KeyboardInterrupt:
                print('\n\n[!]Jangan Mencet Tombol Ctrl + C')
                time.sleep(1.5);
                self.cariDataMahasiswa();
            else:    
                if tanya == 'y' or tanya == 'Y':
                    self.cariDataMahasiswa();
                elif tanya == 'n' or tanya == 'N':
                    self.menu();
                else:
                    print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
                    time.sleep(1.5);
                    self.cariDataMahasiswa();
        else:
            print('\nData Tidak Ditemukan!');
            
            try:
                tanya = input('Cari data mahasiswa lagi (Y/N) ? : ');
                if tanya == 'y' or tanya == 'Y':
                    self.cariDataMahasiswa();
                elif tanya == 'n' or tanya == 'N':
                    self.menu();
                else:
                    print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
                    time.sleep(1.5);
                    self.cariDataMahasiswa();
            except KeyboardInterrupt:
                print('\n\n[!]Jangan Mencet Tombol Ctrl + C');
                time.sleep(1.5);
                self.cariDataMahasiswa();
    
    # method hapus data mahasiswa
    def hapusMhs(self):
        benarSalah = False;
        os.system('cls');
        print('\t      Hapus Data Mahasiswa')
        print('\tHapus Data Berdasarkan Nama/Nim');
        print('='*50)
        
        try:
            search = input('Masukan Nama/Nim Mahasiswa : ');
        except KeyboardInterrupt:
            print('\n\n[!]Jangan Mencet Tombol Ctrl + C');
            time.sleep(1.5);
            self.hapusMhs();
        else:
            # index for delete row
            index = 0
            for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
                if  search.upper() == nameMhs.upper() or search == nimMhs:
                    print('\nData Ditemukan !!')
                    print('='*25)
                    print('Nama  : ', nameMhs.title())
                    print('Nim   : ', nimMhs.title())
                    print('Prodi : ', prodiMhs.title())

                    benarSalah = True
                    break
                # loop variabel index for search index data mahasiswa
                index += 1    

            if benarSalah ==  True:        
                try:
                    question = input('\nHapus Data Mahasiswa (Y/N) ? : ')
                except KeyboardInterrupt:
                    time.sleep(1.5);
                    self.hapusMhs();
                else:
                    if question == 'y' or question == 'y':
                        tabelSiswa.del_row(index)
                        University.namaMahasiswa.remove(nameMhs);
                        University.nimMahasiswa.remove(nimMhs);
                        University.prodiMahasiswa.remove(prodiMhs);
                        
                        print('\nData Berhasil Dihapus!');
    
                        question = input('Hapus Data Mahasiswa Lagi (Y/N) ? : ')
                        if question == 'y' or question == 'Y':
                            self.hapusMhs()
                        elif question == 'n' or question == 'N':
                            self.menu()
                        else:    
                            print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
                            time.sleep(1.5);
                            self.hapusMhs();
                    elif question == 'n' or question == 'N':
                        print('\nHapus Data Dibatalkan')
                        
                        question = input('Coba Hapus Data Lagi (Y/N) ? : ')
                        if question == 'y' or question == 'Y':
                            self.hapusMhs()
                        elif question == 'n' or question == 'N':
                            self.menu()
                        self.menu()
                    else:
                        print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
            else:
                print('\nData Tidak Ditemukan!');
                try:
                    tanya = input('Coba Hapus data mahasiswa lagi (Y/N) ? : ');
                    if tanya == 'y' or tanya == 'Y':
                        self.hapusMhs();
                    elif tanya == 'n' or tanya == 'N':
                        self.menu();
                    else:
                        print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
                        time.sleep(1.5);
                        self.hapusMhs();
                except KeyboardInterrupt:
                    print('\n\n[!]Jangan Mencet Tombol Ctrl + C');
                    time.sleep(1.5);
                    self.hapusMhs();

    
    # method change data mahasiswa
    def ubahDataMahasiswa(self):
        benarSalah = False;
        os.system('cls');
        print('\t      Ubah Data Mahasiswa')
        print('\tUbah Data Berdasarkan Nama/Nim');
        print('='*50)
        
        try:
            change = input('Masukan Nama/Nim Mahasiswa : ');
        except KeyboardInterrupt:
            print('\n\n[!]Jangan Mencet Tombol Ctrl + C ')
            time.sleep(1.5);
            self.ubahDataMahasiswa();
        else:
            index = 0
            for nameMhs, nimMhs, prodiMhs in zip(University.namaMahasiswa, University.nimMahasiswa, University.prodiMahasiswa):
                if change.upper() == nameMhs.upper() or change == nimMhs:      

                    print('\nData Ditemukan!');
                    changeName = input('\nMasukan Nama Baru     : ');
                    changeNim  = input('Masukan Nim Baru      : ');
                    changeProdi  = input('Masukan Prodi Baru    : ');

                    # delete data now
                    University.namaMahasiswa.remove(nameMhs);
                    University.nimMahasiswa.remove(nimMhs)
                    University.prodiMahasiswa.remove(prodiMhs);
                    tabelSiswa.del_row(index)
                    
                    benarSalah = True;
                    break;
                index += 1

            if benarSalah ==  True:
                
                # add data new to data list temporary 
                University.tempNamaMhs.append(changeName);
                University.tempNimMhs.append(changeNim);
                University.tempProdiMhs.append(changeProdi);

                # sum data list in temporay to data list University
                University.namaMahasiswa  += University.tempNamaMhs
                University.nimMahasiswa   += University.tempNimMhs
                University.prodiMahasiswa += University.tempProdiMhs
                tabelSiswa.add_row([changeName.title(), changeNim.title(), changeProdi.title()])

                # clear all data in data list temporary
                University.tempNamaMhs.clear();
                University.tempNimMhs.clear();
                University.tempProdiMhs.clear();

                print('\nData Berhasil Diubah');
                tanya = input('\nUbah data mahasiswa lagi (Y/N) ? : ');
                
                if tanya == 'y' or tanya == 'Y':
                    self.ubahDataMahasiswa();
                elif tanya == 'n' or tanya == 'N':
                    self.menu();
                else:    
                    print('\n[!]Jangan Masukan Angka Atau Huruf Selain Y/N')
                    time.sleep(1.5);
                    self.ubahDataMahasiswa();
            else:
                print('\nData Tidak Ditemukan!');
                
                try:
                    question = input('\nUbah Data Mahasiswa Lagi (Y/N) ? : ')
                except KeyboardInterrupt:
                    self.menu();
                if question == 'y' or question == 'Y':
                    self.ubahDataMahasiswa();
                elif question == 'n' or question == 'N':
                    self.menu();
                else:
                    self.menu();


# in constructor have two parameter mahasiswa and dosen
# in create objek free insert in parameter string anything, because contsructor have two parameter
obj_mahasiswa = University('Nama', 'Nim', 'Prodi');

# fungsi utama main, sama seperti int main() pada c++
if __name__ == '__main__':
    
    # call method menu in objek obj_mahasiswa
    obj_mahasiswa.menu()
    
    # or
    # can wear(pakai) start for call
    # menu = obj_mahasiswa.menu()
    # menu.start()
