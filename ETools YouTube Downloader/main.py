import os
import ffmpeg
import tkinter as tk
from tkinter import messagebox


def download_video():
    link = input("Enter YouTube Video URL:\n")
    download_location = input("Enter download location:\n")
    if link and download_location:
        try:
            os.system(
                f'yt-dlp -f best -o "{download_location}/%(title)s.%(ext)s" "{link}" -S res:1080'
            )
            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    else:
        messagebox.showerror(
            "Error", "Please provide a valid YouTube URL and download location."
        )


def convert_file():
    try:
        finput = input("Enter the input file path:\n")
        foutput = input("Enter the output file path:\n")
        (ffmpeg.input(finput).output(foutput).run())
        messagebox.showinfo(message="Conversion Complete")
        print("Conversion Complete")
    except Exception as e:
        messagebox.showerror(message=f"{e}")
