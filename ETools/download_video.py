import os
import ffmpeg

#def download_video():
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