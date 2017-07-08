import time
year=time.localtime()

def tuoi(year1, name):
    age = year[0] - year1
    if age == 0:
        age == age +1
        print('Chao ban',name,'ban',age,'tuoi phai khong?')
    elif age > 0:
        print('Chao ban', name, 'ban', age, 'tuoi phai khong?')
    else:
        print('Chao ban', name, 'ban co do tuoi khong phu hop!')

def main():
    year1=int(input('Vui long nhap nam sinh: '))
    name=input('Vui long nhap ten cua ban: ')
    tuoi(year1,name)

main()