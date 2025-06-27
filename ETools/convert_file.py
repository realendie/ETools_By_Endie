import os
import ffmpeg

# RED TEXT = \033[31m
# YELLOW TEXT = \033[33m
# RESET TEXT COLOR = \033[0m


def convert_file():
        print(
            "\033[31mREMINDER:\033[33m File paths with spaces should be enclosed in double quotes.\033[0m"
        )
        finput = input("Enter the input file path: ")
        foutput = input("Enter the output file path: ")
        if finput and foutput:
            try:
                os.system(f"ffmpeg -i {finput} {foutput}")
                print("Conversion Complete")
            except Exception as e:
                print("Error", f"An error occurred: {e}")
        else:
            print("\033[31mError: \033[33mPlease provide a valid YouTube URL and download location.\033[0m")


convert_file()
