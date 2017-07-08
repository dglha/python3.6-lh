#Kiem tra 1 so co phai so nguyen to hay khong

#kiem tra dau vao
def test():
    while True:
        number = int(input("Nhap so: "))

#        if number == 2:
#            print('So', number, 'la so nguyen to')
#            break
        if number == 1:
            break
        elif number < 0:
            print ("So nguyen to phai la 1 so nguyen duong (>0)!")
            print("Vui long nhap lai so!")
            continue
        else:
            break
    return number

#Funcion kiem tra so nguyen to
def kiemtra(number):
    count=2
    while True:
        if number==1:
            print('So',number,'khong phai la so nguyen to!')
            break
        num_check=number % count
        if count == number:
            print('So',number,'la so nguyen to!')
            break
        if num_check==0:
            print('So',number,'khong phai la so nguyen to!')
            break
        else:
            count = count +1
            continue

#Funcion main
if __name__ == '__main__':
    kiemtra(test())
