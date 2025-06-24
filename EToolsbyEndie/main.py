import os
import ffmpeg
from pyfiglet import Figlet
import download_video
import convert_file

# RED TEXT = \033[31m
# YELLOW TEXT = \033[33m
# RESET TEXT COLOR = \033[0m


def select_tool():
    select_function = input(
        "Select a function:\n1. Download Video\n2. Convert File\n3. Exit\n\n"
    )

    if select_function == "1":
        download_video.download_video()
    elif select_function == "2":
        convert_file.convert_file()
    elif select_function == "3":
        print("\nExiting the program. Goodbye!")
        quit()
    else:
        print(
            "\n\033[31mERROR: \033[33mYou selected an invalid function. Please try again.\n\033[0m"
        )
        select_tool()


big = Figlet(font="big")
print(big.renderText("ETools By Endie"))
select_tool()
