import os

# RED TEXT = \033[31m
# YELLOW TEXT = \033[33m
# RESET TEXT COLOR = \033[0m


def download_video():
    link = input("Enter YouTube Video URL: ")
    print(
        "\033[31mREMINDER:\033[33m File paths with spaces should be enclosed in double quotes.\033[0m"
    )
    download_location = input("Enter download location: ")
    if link and download_location:
        try:
            os.system(f'yt-dlp -o "{download_location}/%(title)s.%(ext)s" "{link}"')
            print("Success", "Download completed!")
        except Exception as e:
            print("Error", f"An error occurred: {e}")
    elif not link:
        print("\033[31mError", "\033[33mPlease provide a valid YouTube URL.\033[0m")
        download_video()
    elif not download_location:
        print(
            "\033[31mError",
            "\033[33mPlease provide a valid download location.\033[0m",
        )
        download_video()
    else:
        print("Error: Please provide a valid YouTube URL and download location.")


download_video()
