import os
import subprocess
import tkinter as tk
from tkinter import messagebox

def download_video():
    link = input("Enter YouTube Video URL: ")
    download_location = input("Enter download location: ")
    if link and download_location:
        try:
            os.system(f'yt-dlp -f best -o "{download_location}/%(title)s.%(ext)s" "{link}" -S res:1080')
            messagebox.showinfo("Success", "Download completed!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")           
    else:
        messagebox.showerror("Error", "Please provide a valid YouTube URL and download location.")