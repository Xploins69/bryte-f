import os

from colorOS.colorOS import color, reset
from libs.BannerManager import Create

def Save(path, process, digit, number):
    green = color.green()
    red = color.red()

    try:
        if process:
            with open(path, "w") as f:
                for i in range(number):
                    f.write(f"{i:0{digit}d}\n")
                print(f"{green}[success]{reset()}: File is Created and Written.")
        else:
            with open(path, "a") as f:
                for i in range(number):
                    f.write(f"{i:0{digit}d}\n")
                print(f"{green}[success]{reset()}: Added is File.")

    except Exception as e:
        print(f"{red}[ERROR]: {e}{reset()}")

def main():
    blue = color.blue()
    red = color.red()

    while True:
        try:
            os.system("cls||clear")
            Create("bryte-f", font="slant", width=60, justify="center", Color="blue")
            file_name = input(f"{blue}File Name: {reset()}")
            number = int(input(f"{blue}Count: {reset()}"))
            digit = int(input(f"{blue}Digit: {reset()}"))
            path = os.path.join("wordlist", file_name)
            if os.path.exists(path):
                os.system("cls||clear")
                while True:
                    print(f"{color.yellow()}[Warning !!]{reset()}: if the selection is no it will be added to the file.")
                    answer = input(f"{blue}file exists, should i overwrite it? (Y/n): {reset()}")
                    if answer.lower() == "y":
                        Save(path, process=True, digit=digit, number=number)
                        input()
                        break
                    elif answer.lower() == "n":
                        Save(path, process=False, digit=digit, number=number)
                        input()
                        break
                    else:
                        pass
            else:
                Save(path, process=True, digit=digit, number=number)
                input()
        except Exception as e:
            print(f"{red}[ERROR]{reset()}: {e}")
            input()

if __name__ == "__main__":
    main()