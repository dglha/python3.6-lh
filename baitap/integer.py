def test(num):
    num = num % 2
    if num == 1:
        return "So le"
    elif num == 0:
        return "So chan"

def main():
    num=int(input("Nhap so int: "))
    print (test(num))

main()