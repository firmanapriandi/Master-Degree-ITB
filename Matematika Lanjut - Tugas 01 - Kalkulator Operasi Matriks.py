# REVISI
# PERBAIKAN INPUT PROGRAM
#
from termcolor import colored
import numpy

#MENDAPATKAN DIMENSI ATAU UKURAN ORDO MATRIX YG AKAN DIBUAT
class varOrdoMatrix:
    def __init__(self):
        StatusInput01 = False
        StatusInput02 = False
        StatusInput03 = False
        StatusInput04 = False

        while StatusInput01 == False :
            try:
                SizeRowA = int(input(colored("Masukkan Jumlah Baris Matrix A :",'blue')))
                self.SizeRowA = SizeRowA
                StatusInput01 = True
            except ValueError:
                print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka :",'red'))
                StatusInput01 = False
        while StatusInput02 == False:
            try:
                SizeColumnA = int(input(colored("Masukkan Jumlah Kolom Matrix A :",'blue')))
                self.SizeColumnA = SizeColumnA
                StatusInput02 = True
            except ValueError:
                print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka :",'red'))
                StatusInput02 = False
        while StatusInput03 == False :
            try:
                SizeRowB = int(input(colored("Masukkan Jumlah Baris Matrix B :",'blue')))
                self.SizeRowB = SizeRowB
                StatusInput03 = True
            except ValueError:
                print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka :",'red'))
                StatusInput03 = False
        while StatusInput04 == False :
            try:
                SizeColumnB = int(input(colored("Masukkan Jumlah Kolom Matrix B :",'blue')))
                self.SizeColumnB = SizeColumnB
                StatusInput04 = True
            except ValueError:
                print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka :",'red'))
                StatusInput04 = False

class getMatrixData:
    def __init__(self, SizeRowA, SizeRowB, SizeColumnA, SizeColumnB):
        print("\n")

        matrix_A = numpy.zeros(shape=(SizeRowA, SizeColumnA), dtype=float)
        matrix_B = numpy.zeros(shape=(SizeRowB, SizeColumnB), dtype=float)

        print(colored("Input Data Matrix A :", 'blue'))

        for barisA in range(SizeRowA):
            for kolomA in range(SizeColumnA):
                CondInMatrixA = False
                while CondInMatrixA == False:
                    try:
                        dataMatrixA = float(input("Masukan Input Untuk Baris "+str(barisA+1) +" Kolom "+str(kolomA+1)+" : "))
                        matrix_A[barisA,kolomA] = dataMatrixA
                        CondInMatrixA = True
                    except ValueError:
                        print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka",'red'))
                        CondInMatrixA = False

        print("\n")
        print(colored("Input Data Matrix B :", 'blue'))
        for barisB in range(SizeRowB):
            for kolomB in range(SizeColumnB):
                CondInMatrixB = False
                while CondInMatrixB == False :
                    try:
                        dataMatrixB = float(input("Masukkan Input Untuk Baris " + str(barisB+1) + " Kolom " + str(kolomB+1) + (" : ")))
                        matrix_B[barisB,kolomB] = dataMatrixB
                        CondInMatrixB = True
                    except ValueError:
                        print(colored("ERROR!!! Mohon Memasukkan Nilai Berupa Angka", 'red'))
                        CondInMatrixB = False
        self.matrix_A = matrix_A
        self.matrix_B = matrix_B

def PerkalianSkalar():
    InputOrdo = varOrdoMatrix()
    getMatrix = getMatrixData(InputOrdo.SizeRowA, InputOrdo.SizeRowB, InputOrdo.SizeColumnA, InputOrdo.SizeColumnB)

    InputNilaiSkalar = float(input(colored("\nMasukkan Nilai Skalar : \n", 'blue')))

    print(colored("Data Matriks A :",'yellow'))
    print(getMatrix.matrix_A)
    print(colored("Data Matrix B :",'yellow'))
    print(getMatrix.matrix_B)
    print("\n")

    print(colored("Hasil Matrix A Dikali Skalar",'green'))
    print(InputNilaiSkalar*getMatrix.matrix_A)
    print(colored("Hasil Matrix B Dikali Skalar",'green'))
    print(InputNilaiSkalar*getMatrix.matrix_B)

def PenjumlahanMatrix():
    InputOrdo = varOrdoMatrix()
    while InputOrdo.SizeRowA != InputOrdo.SizeRowB or InputOrdo.SizeColumnA != InputOrdo.SizeColumnB:
        print(colored('ERROR!!! Ordo Matrix A dan B tidak sama', 'red'))
        InputOrdo = varOrdoMatrix()
    getMatrix = getMatrixData(InputOrdo.SizeRowA, InputOrdo.SizeRowB, InputOrdo.SizeColumnA,  InputOrdo.SizeColumnB)
    print(colored("Data Matrix A :", 'yellow'))
    print(getMatrix.matrix_A)
    print(colored("Data Matrix B :", 'yellow'))
    print(getMatrix.matrix_B)
    print("\n")
    print(colored("Matrix A+B adalah :", 'green'))
    matrixJumlah = numpy.zeros(shape=(InputOrdo.SizeRowA, InputOrdo.SizeColumnA), dtype=float)
    for baris in range(0, len(getMatrix.matrix_A)):
        for kolom in range(0, len(getMatrix.matrix_B[0])):
            dataJumlah = (getMatrix.matrix_A[baris][kolom] + getMatrix.matrix_B[baris][kolom])
            matrixJumlah[baris, kolom] = dataJumlah
    print(matrixJumlah)
    print("\n")

def PenguranganMatrix():
    InputOrdo = varOrdoMatrix()
    while InputOrdo.SizeRowA != InputOrdo.SizeRowB or InputOrdo.SizeColumnA != InputOrdo.SizeColumnB:
        print(colored('ERROR!!! Ordo Matrix A dan B tidak sama', 'red'))
        InputOrdo = varOrdoMatrix()
    getMatrix = getMatrixData(InputOrdo.SizeRowA, InputOrdo.SizeRowB, InputOrdo.SizeColumnA,  InputOrdo.SizeColumnB)
    print(colored("Data Matrix A :", 'yellow'))
    print(getMatrix.matrix_A)
    print(colored("Data Matrix B :", 'yellow'))
    print(getMatrix.matrix_B)
    print("\n")

    CondInOpsi=False

    while CondInOpsi == False:
        try:
            SelectPengurangan = int(input(colored("Silahkan Pilih Opsi Pengurangan (1)/(2) : ", "green")+"\n(1) A-B \n(2) B-A\nOpsi Anda : "))
            CondInOpsi = True

            if SelectPengurangan == 1:
                matrixJumlah = numpy.zeros(shape=(InputOrdo.SizeRowA, InputOrdo.SizeColumnA), dtype=float)
                for baris in range(0, len(getMatrix.matrix_A)):
                    for kolom in range(0, len(getMatrix.matrix_B[0])):
                        dataJumlah = (getMatrix.matrix_A[baris][kolom] - getMatrix.matrix_B[baris][kolom])
                        matrixJumlah[baris, kolom] = dataJumlah

                print(colored("\nMatrix A-B adalah :", 'green'))
                print(matrixJumlah)

            elif SelectPengurangan == 2:
                matrixJumlah = numpy.zeros(shape=(InputOrdo.SizeRowA, InputOrdo.SizeColumnA), dtype=float)
                for baris in range(0, len(getMatrix.matrix_A)):
                    for kolom in range(0, len(getMatrix.matrix_B[0])):
                        dataJumlah = (getMatrix.matrix_B[baris][kolom] - getMatrix.matrix_A[baris][kolom])
                        matrixJumlah[baris, kolom] = dataJumlah

                print(colored("\nMatrix B-A adalah :", 'green'))
                print(matrixJumlah)
            print("\n")

        except ValueError:
            print(colored("ERROR!!! Harap Hanya Memasukkan Nilai Berupa Angka 1 atau 2", 'red'))
            CondInOpsi = False


def DeterminanMatrix():
    InputOrdo = varOrdoMatrix()
    while InputOrdo.SizeRowA != InputOrdo.SizeColumnA or InputOrdo.SizeRowB != InputOrdo.SizeColumnB:
        print(colored("ERROR!!! Matrix Tidak Memiliki Nilai Determinan, dikarenakan baris dan kolom yang tidak sama",'red'))
        InputOrdo = varOrdoMatrix()
    while InputOrdo.SizeRowA > 4 or InputOrdo.SizeRowB > 4 or InputOrdo.SizeColumnA > 4 or InputOrdo.SizeColumnB > 4:
        print(colored("ERROR!!! Mohon Maaf, Ordo Matrix terlalu besar atau lebih dari 3",'red'))
        InputOrdo = varOrdoMatrix()
    getMatrix = getMatrixData(InputOrdo.SizeRowA, InputOrdo.SizeRowB, InputOrdo.SizeColumnA,  InputOrdo.SizeColumnB)
    print(colored("Data Matrix A :",'yellow'))
    print(getMatrix.matrix_A)
    print(colored("Data Matrix B :", 'yellow'))
    print(getMatrix.matrix_B)
    print("\n")
    det_A = int(numpy.linalg.det(getMatrix.matrix_A))
    det_B = int(numpy.linalg.det(getMatrix.matrix_B))

    print(colored("Determinan dari Matrix A adalah " + str(det_A)+ "\n",'green'))
    print(colored("Determinan dari Matrix B adalah " + str(det_B),'green'))

def OperasiPerkalianAntarMatrix():
    InputOrdo = varOrdoMatrix()
    getMatrix = getMatrixData(InputOrdo.SizeRowA, InputOrdo.SizeRowB, InputOrdo.SizeColumnA, InputOrdo.SizeColumnB)

    CondInPerkalian = False

    while CondInPerkalian == False:
        try:
            print(colored("\nSilahkan Pilih, Opsi Perkalian Antar Matrix ", 'green', attrs=['bold']))
            print("(1) AxB")
            print("(2) BxA")
            SelectPerkalian = int(input(colored("Opsi Anda :", 'blue')))
            CondInPerkalian = True

            if SelectPerkalian == 1:
                print(colored("\nPerkalian Matrix AxB \n", 'green'))
                while InputOrdo.SizeColumnA != InputOrdo.SizeRowB:
                    print(colored("ERROR!!! Perkalian Tidak Bisa Dilakukan", 'red'))
                    print(colored("Kolom Matrix Pertama dgn Baris Matrix Kedua harus sama", 'red'))
                    InputOrdo = varOrdoMatrix()
                print(colored("Data matriks A:", 'yellow'))
                print(getMatrix.matrix_A)
                print(colored("Data matriks B:", 'yellow'))
                print(getMatrix.matrix_B)
                print("\n")
                matrix_A = numpy.zeros(shape=(InputOrdo.SizeRowA, InputOrdo.SizeColumnB), dtype=float)
                for a in range(0, InputOrdo.SizeRowA):
                    for b in range(0, InputOrdo.SizeColumnB):
                        for c in range(0, InputOrdo.SizeColumnA):
                            matrix_A[a][b] = matrix_A[a][b] + getMatrix.matrix_A[a][c] * getMatrix.matrix_B[c][b]
                print(colored("Data Matrix AxB :", 'green'))
                print(matrix_A)
                print("\n")

            if SelectPerkalian == 2:
                print(colored("\nPerkalian Matrix BxA \n", 'green'))
                while InputOrdo.SizeColumnA != InputOrdo.SizeRowB:
                    print(colored("ERROR!!! Perkalian Tidak Bisa Dilakukan", 'red'))
                    print(colored("ERROR!!! Kolom Matrix Pertama dgn Baris Matrix Kedua harus sama"))
                    InputOrdo = varOrdoMatrix()
                print(colored("Data matriks A:", 'yellow'))
                print(getMatrix.matrix_A)
                print(colored("Data matriks B:", 'yellow'))
                print(getMatrix.matrix_B)
                print("\n")
                matrix_B = numpy.zeros(shape=(InputOrdo.SizeRowB, InputOrdo.SizeColumnA), dtype=float)
                for a in range(0, InputOrdo.SizeRowB):
                    for b in range(0, InputOrdo.SizeColumnA):
                        for c in range(0, InputOrdo.SizeColumnB):
                            matrix_B[a][b] = matrix_B[a][b] + getMatrix.matrix_B[a][c] * getMatrix.matrix_A[c][b]
                print(colored("Data Matrix BxA :", 'green'))
                print(matrix_B)
                print("\n")

        except ValueError:
            print(colored("ERROR!!! Harap Hanya Memasukkan Nilai Berupa Angka 1 atau 2", 'red'))
            CondInPerkalian = False


if __name__ == '__main__':

    x = True

    while(x):
        print("#-------------------------------------------------- PANDUAN ----------------------------------------------------#" + colored("\n1. Pilih Operasi Matrix {Perkalian Skalar(A)/Penjumlahan(B)/Pengurangan(C)/Determinan(D)/Perkalian Antar Matrix(E)",'green'))
        print(colored("2. Untuk Mengakhiri Sesi, ketik ",'green')+colored("exit",'red')+"\n"+"#---------------------------------------------------------------------------------------------------------------#")
        try:
            PilihOperasiMatrix = str(input(colored("\nMasukkan Operasi Matrix Yang Dipilih ( A/B/C/D/E atau exit )",'blue')))
            print("#---------------------------------------------------------------------------------------------------------------#")
            if PilihOperasiMatrix == "A":
                print(colored("Anda Memilih Operasi Perkalian Skalar Matrix \n", 'green'))
                PerkalianSkalar()
            elif PilihOperasiMatrix == "B":
                print(colored("Anda Memilih Operasi Penjumlahan Matrix \n", 'green'))
                PenjumlahanMatrix()
            elif PilihOperasiMatrix == "C":
                print(colored("Anda Memilih Operasi Pengurangan Matrix \n", 'green'))
                PenguranganMatrix()
            elif PilihOperasiMatrix == "D":
                print(colored("Anda Memilih Operasi Determinan Matrix \n", 'green'))
                DeterminanMatrix()
            elif PilihOperasiMatrix == "E":
                print(colored("Anda Memilih Operasi Perkalian Matrix", 'green'))
                OperasiPerkalianAntarMatrix()
            elif PilihOperasiMatrix == "exit":
                print(colored("Sesi Anda Telah Berakhir","white"))
                break

        except ValueError:
            print(colored("ERROR!!!, Mohon Memasukkan Input Sesuai Yang Diperintahkan (A/B/C/D/E atau exit)",'red'))