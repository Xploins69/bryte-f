from pyfiglet import Figlet
from termcolor import colored
import os
from colorama import Fore, Back, Style, init
init(autoreset=True)
while True:
    os.system("clear")
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
    print(Fore.BLUE + "1) 3 digit \n2) 4 digit \n3) 6 digit \n4) 8 digit")#bu satır işlemleri ekrana yazdırır.
    x = input("işlem seç: ")
    if x == 1:
        i = input("Dosya adı giriniz: ")#dosya adı alma
        with open(i, "w") as dosya:#i değişkene girilen ad ile txt dosyayı kontrol ediyoruz
            for x in range(1000):#999 a kadar saydırıyoruz
                    dosya.write("{:03d}\n".format(x))#txt dosyasına 3 haneli olarak yazdırıyoruz
            if os.path.exists(i):#dosyanın olup olmadığına bakıyoruz
                print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
                user_choice = input().strip().lower()
                if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                    print("İşlem iptal edildi.")
                    continue
                else:
                    tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                    if tekrar == "Y":#varsabaşa dönüyoruz
                        continue
                    else:#yoksa program bitiyo
                        break
    elif x == 2:
        i = input("Dosya adı giriniz: ")
        with open(i, "w") as dosya:
            for x in range(10000):
                dosya.write("{:04d}\n".format(x))
            if os.path.exists(i):#dosyanın olup olmadığına bakıyoruz
                print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
                user_choice = input().strip().lower()
                if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                    print("İşlem iptal edildi.")
                    continue
                else:
                    tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                    if tekrar == "Y":#varsabaşa dönüyoruz
                        continue
                    else:#yoksa program bitiyo
                        break
    elif x == 3:
        i = input("Dosya adı giriniz: ")
        with open(i, "w") as dosya:
           for x in range(1000000):
                dosya.write("{:06d}\n".format(x))
        if os.path.exists(i):#dosyanın olup olmadığına bakıyoruz
                print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
                user_choice = input().strip().lower()
                if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                    print("İşlem iptal edildi.")
                    continue
                else:
                    tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                    if tekrar == "Y":#varsabaşa dönüyoruz
                        continue
                    else:#yoksa program bitiyo
                        break
    elif x == 4:
        i = input("Dosya adı giriniz: ")
        with open(i, "w") as dosya:
            for x in range(100000000):
               dosya.write("{:08d}\n".format(x))
        if os.path.exists(i):#dosyanın olup olmadığına bakıyoruz
                print(f"'{i}' adlı dosya zaten var. Üzerine yazmak istiyor musunuz? (E/H)")#dosya var devam etmek istiyo musun?
                user_choice = input().strip().lower()
                if user_choice != 'e':#cevap e değilse işlemi iptal edip başa dönüyoruz
                    print("İşlem iptal edildi.")
                    continue
                else:
                    tekrar = str(input("başka bir işlem varmı Y/N: "))#başka bir işlem var mı diye soruyoruz
                    if tekrar == "Y":#varsabaşa dönüyoruz
                        continue
                    else:#yoksa program bitiyo
                        break
    #yanlış işlem                          
    else:
        print(Fore.RED + "doğru işlem seç")
        c = input("çıkmak için ENTER basınız.")
        if c == " ":
            break
        else:
            continue

