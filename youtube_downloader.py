from pytube import YouTube
import tkinter as tk
from tkinter import filedialog

def download_video(url, save_path):

  try:
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True,file_extension="mp4")
    high_res_stream = streams.get_highest_resolution()
    high_res_stream.download(output_path=save_path)
    print("Video download successful")


  except Exception as err:
    print(err)

def open_file_dialog():
  folder = filedialog.askdirectory()
  if folder:
    print(f"Select folder: {folder}")

  return folder




if __name__ == "__main__":
  root = tk.Tk()
  root.withdraw()

  url = input("Enter a youtube url: ")
  dir = open_file_dialog()

  if not dir:
    print("Invalid location")
  else:
    print("Downloading")
    download_video(url, dir)

