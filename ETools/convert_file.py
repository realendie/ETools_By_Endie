import os
import ffmpeg

# RED TEXT = \033[31m
# YELLOW TEXT = \033[33m
# RESET TEXT COLOR = \033[0m

try:
    print(
        "\033[31mREMINDER:\033[33m File paths with spaces should be enclosed in double quotes.\033[0m"
    )
    finput = input("Enter the input file path: ")
    foutput = input("Enter the output file path: ")
    os.system(f"ffmpeg -i {finput} {foutput}")
    print("Conversion Complete")
except Exception as e:
    print(f"{e}")
