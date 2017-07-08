#Nhap n, in ra 'n' so nguyen to ton tai!

#Kiem tra dau vao
def check():
    while True:
        num=int(input('Nhap so: '))
        if num < 0:
            print('- So nhap phai la so nguyen duong va lon hon 0')
            print('--- vui lng nhap lai so!')
            continue
        else:
            break
        return num

#Funcion kiem tra so nguyen to
def nto(num):
    dem_soluong=0
    soluong_nguyento=num
    print('Cac so nguyen to: ')

    if soluong_nguyento ==1:
        print('2')
    else:
        so_kiemtra=2
        so_dem=2
        dem_soluong=0
        while True:
            if dem_soluong==soluong_nguyento:
                break
            so_dem=2
            while True:
                so_chiahet = so_kiemtra % so_dem
                if so_dem == so_kiemtra:
                    print (so_kiemtra)
                    so_kiemtra +=1
                    dem_soluong +=1
                    break
                if so_chiahet == 0:
                    so_kiemtra +=1
                    continue
                else:
                    so_dem +=1
                    continue

#Funcion main
if __name__ == '__main__':
    nto(check())

