print("-----------------------------------------")
print("Nama : Nabil Daffa Athalasyah            ")
print("NIM  : 2409116090                        ")
print("Kelas: Sistem Informasi C 2024           ")
print("Tugas Mini Project 1 Dasar Pemrograman   ")
print("-----------------------------------------")

while True:
    print("Welcome to Traning Center Basic Programming!, Please enter your Name, NIM, and Class !")
    Name = input("Enter your Name: ")
    NIM = input("Enter your NIM: ")
    Class = input("Enter your Class: ")
    if Name == "Nabil" and NIM == "090" and Class == "C":
        print("Welcome Back Challenger!", Name)
        break
    else:
        print("Your Name is Invalid! Please Try another Name!")
        break

while True:
    Pricelist_Packet = int(input("Enter_Pricelist(Example=200000): "))
    the_amount_of_goods = int(input("Enter_the_amount_of_goods(Example=4): "))
    total = Pricelist_Packet * the_amount_of_goods

    if total > 250000:
        Discount = total- (0.25*total)
        print("Congrats you get discount 25%!")
        print("total", total)
    else:
        print("total", total)

    Choice = input("You want return?(Yes/No): ")
    if Choice == "Yes":
        continue
    else:
        print("Thank you so much for coming!, See you later! ")
        
        exit()