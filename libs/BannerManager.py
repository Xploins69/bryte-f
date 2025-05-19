import os
import pyfiglet

from colorOS.colorOS import color, background, reset

def Create(text, width=40, font="standard", justify="left", Color="white", bg_color=None):
    ascii = pyfiglet.Figlet(font=font, width=width).renderText(text)
    width = os.get_terminal_size().columns
    colors = {"white": color.white(), "black": color.black(), "red": color.red(), "green": color.green(), "blue": color.blue(), "yellow": color.yellow(), "purple": color.purple(), "brown": color.brown(), "cyan": color.cyan(), "light_red": color.lightred(), "light_green": color.lightgreen(), "light_blue": color.lightblue(), "light_purple": color.lightpurple(), "light_cyan": color.lightcyan(), "light_gray": color.lightgray(), "dark_gray": color.darkgray()}
    bg_colors = {"white": background.white(), "black": background.black(), "red": background.red(), "green": background.green(), "blue": background.blue(), "yellow": background.yellow(), "purple": background.purple(), "brown": background.brown(), "cyan": background.cyan(), "light_red": background.lightred(), "light_green": background.lightgreen(), "light_blue": background.lightblue(), "light_purple": background.lightpurple(), "light_cyan": background.lightcyan(), "light_gray": background.lightgray(), "dark_gray": background.darkgray()}
    
    if Color.lower() in "rgb:":
        color_codes = Color.split(":")[1].split(",")
        Color = color.RGB(int(color_codes[0]), int(color_codes[1]), int(color_codes[2]))
    else:
        Color = colors[Color]
    
    if not bg_color is None:
        if bg_color.lower() in "rgb:":
            color_codes = bg_color.split(":")[1].split(",")
            bg_color = background.RGB(int(color_codes[0]), int(color_codes[1]), int(color_codes[2]))
        else:
            bg_color = bg_colors[bg_color]
    
    if not bg_color is None:
        if justify.lower() == "left":
            print(f"{bg_color}{ascii}{reset()}")
        elif justify.lower() == "center":
            for line in ascii.split("\n"):
                print(f"{bg_color}{line.center(width)}{reset()}")
        elif justify.lower() == "right":
            halfpast = width - len(ascii.split("\n")[0])
            for line in ascii.split("\n"):
                print(f"{bg_color}{" " * halfpast + line}{reset()}")
    else:
        if justify.lower() == "left":
            print(f"{Color}{ascii}{reset()}")
        elif justify.lower() == "center":
            for line in ascii.split("\n"):
                print(f"{Color}{line.center(width)}{reset()}")
        elif justify.lower() == "right":
            halfpast = width - len(ascii.split("\n")[0])
            for line in ascii.split("\n"):
                print(f"{Color}{" " * halfpast + line}{reset()}")

def available_fonts():
    fonts = pyfiglet.Figlet.getFonts()
    for i, font in enumerate(fonts):
        ascii = pyfiglet.figlet_format("test", font=font)
        print(f"{i}.{font}\n{ascii}")