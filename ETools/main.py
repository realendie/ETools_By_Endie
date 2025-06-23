import os
import ffmpeg
from pyfiglet import Figlet
import download_video
import convert_file

big = Figlet(font="big")
print(big.renderText("ETools By Endie"))

select_function = input(
    "Select a function:\n1. Download Video\n2. Convert File\n3. Exit\n\n"
)

if select_function == "1":
    download_video.download_video()
elif select_function == "2":
    convert_file.convert_file()
elif select_function == "3":
    print("Exiting the program. Goodbye!")
    quit()
else:
    print("You selected an invalid option. Please try again.")
