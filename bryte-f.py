from pyfiglet import Figlet #banner için bir kütüphane eklenir
from termcolor import colored #yazılan verileri renklendirmek için kütüphane eklenir
import os #dosya ve dizinler için kütüphane ekliyoruz 
from colorama import Fore, Back, Style, init #yazılan verileri renklendirmek için kütüphane eklenir
init(autoreset=True) #kütüphaneyi aktif edilir
while True: #sonsuz bir döngü başlatılır
    os.system("clear") #terminali temizlilenir
    def create_colored_banner(text, font="standard", color="cyan"):
        fig = Figlet(font=font)
        banner = fig.renderText(text)
        colored_banner = colored(banner, color)
        return colored_banner

    if __name__ == "__main__":
        banner_text = "Bryte_f"
        
        # Yazı tipi ve renk seçeneklerini önceden belirleyebilirsiniz.
        font_choice = "standard"  # veya istediğiniz bir yazı tipi
        color_choice = "blue"     # veya istediğiniz bir renk

        colored_banner = create_colored_banner(banner_text, font=font_choice, color=color_choice)
        print(colored_banner)    
    print(Fore.BLUE + "1) 3 digit \n2) 4 digit \n3) 6 digit \n4) 8 digit") #işlemleri ekrana yazdırır.
    x = int(input("işlem seç: ")) #kullanıcı işlem seçer
    dizin = "/root/bryte-f/WordList" #dosyaların kaydedilceği yerin değişkeni
    if x == 1: #işlem 1'se
        i = input("Dosya adı giriniz: ") #kullanıcıdan dosya adı alınıyor
        if os.path.exists(f'{dizin}/{i}'): #dosya adının olup olmadığına bakılıyor
            print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)") #dosya var devam etmek istiyo musun?
            user_choice = input().strip().lower()
            if user_choice != 'e': #cevap e değilse işlemi iptal edip başa dönüyoruz
                print("İşlem iptal edildi.")
                continue
            else: #cevap e'se
                with open(f'{dizin}/{i}', "w") as dosya: #i değişkene girilen ad ile dizin değişkenine txt dosyayı açılır
                    for x in range(1000): #999 a kadar saydırılır
                        dosya.write("{:03d}\n".format(x)) #txt dosyasına 3 haneli olarak yazdırılır
                    tekrar = str(input("başka bir işlem varmı Y/N: ")) #başka bir işlem var mı diye soruyorulur
                    if tekrar == "Y": #varsa başa dönülür
                     continue
                    else: #yoksa program bitiyo
                        break
        else: #dosya yoksa
            with open(f'{dizin}/{i}', "w") as dosya: #i değişkene girilen ad ile dizin değişkenine txt dosyayı kontrol edilir
                    for x in range(1000): #999 a kadar saydırılır
                        dosya.write("{:03d}\n".format(x)) #txt dosyasına 3 haneli olarak yazdırılır
                    tekrar = str(input("başka bir işlem varmı Y/N: ")) #başka bir işlem var mı diye sorulur
                    if tekrar == "Y": #varsa başa dönülür
                     continue
                    else: #yoksa program bitiyo
                        break
    elif x == 2: #işlem 2'se
        i = input("Dosya adı giriniz: ") #kullanıcıdan dosya adı alınıyor
        if os.path.exists(f'{dizin}/{i}'): #dosyanın olup olmadığına bakılır
            print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)") #dosya var devam etmek istiyo musun?
            user_choice = input().strip().lower()
            if user_choice != 'e': #cevap e değilse işlemi iptal edip başa dönülür
                print("İşlem iptal edildi.")
                continue
            else: #cevap e'se
                with open(f'{dizin}/{i}', "w") as dosya:
                    for x in range(10000):
                        dosya.write("{:04d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                    continue
                else:#yoksa program bitiyo
                    break
        else:
            with open(f'{dizin}/{i}', "w") as dosya:
                for x in range(10000):
                    dosya.write("{:04d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                    continue
                else:#yoksa program bitiyo
                    break
    elif x == 3:
        i = input("Dosya adı giriniz: ")
        if os.path.exists(f'{dizin}/{i}'):#dosyanın olup olmadığına bakıyoruz
            print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
            user_choice = input().strip().lower()
            if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                print("İşlem iptal edildi.")
                continue
            else:
                with open(f'{dizin}/{i}', "w") as dosya:
                    for x in range(1000000):
                        dosya.write("{:06d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                   continue
                else:#yoksa program bitiyo
                    break
        else:
            with open(f'{dizin}/{i}', "w") as dosya:
                for x in range(1000000):
                    dosya.write("{:06d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                   continue
                else:#yoksa program bitiyo
                    break
    elif x == 4:
        i = input("Dosya adı giriniz: ")
        if os.path.exists(f'{dizin}/{i}'):#dosyanın olup olmadığına bakıyoruz
            print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
            user_choice = input().strip().lower()
            if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                print("İşlem iptal edildi.")
                continue
            else:
                with open(f'{dizin}/{i}', "w") as dosya:
                    for x in range(100000000):
                        dosya.write("{:08d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                    continue
                else:#yoksa program bitiyo
                    break
        else:
            with open(f'{dizin}/{i}', "w") as dosya:
                for x in range(100000000):
                    dosya.write("{:08d}\n".format(x))
                tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                if tekrar == "Y":#varsabaşa dönüyoruz
                    continue
                else:#yoksa program bitiyo
                    break                        
    else:
        print(Fore.RED + "doğru işlem seç")
        c = input("çıkmak için ENTER basınız.")
        if c == " ":
            break
        else:
            continue

