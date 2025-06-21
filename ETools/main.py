import os
import ffmpeg

def download_video():
    link = input("Enter YouTube Video URL: ")
    download_location = input("Enter download location: ")
    if link and download_location:
        try:
            os.system(
                f'yt-dlp -f best -o "{download_location}/%(title)s.%(ext)s" "{link}" -S res:1080'
            )
            print("Success", "Download completed!")
        except Exception as e:
            print("Error", f"An error occurred: {e}")
    else:
        print(
            "Error", "Please provide a valid YouTube URL and download location."
        )

def convert_file():
    try:
        finput = input("Enter the input file path: ")
        foutput = input("Enter the output file path: ")
        (ffmpeg.input(finput).output(foutput).run())
        print("Conversion Complete")
    except Exception as e:
        print(f"{e}")
