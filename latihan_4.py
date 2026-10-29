import math
while True:
    print("""
1 = Segi 4
2 = Segi 3
3 = Lingkaran 
4 = Keluar    
""")
    choice=int(input("Tentukan Angka"))
    if choice == 1:
        l=int(input("Lebar?"))
        p=int(input("Panjang?"))
        print("Luas=", p*l)
    elif choice == 2:
        a=int(input("alas?"))
        t=int(input("Tinggi?"))
        print("Luas=", a*t*1/2)
    elif choice == 3:
        r=int(input("Radius?"))
        print(r*r*math.pi)
    elif choice == 4:
        break
    else:
        print("tidak sesuai")
