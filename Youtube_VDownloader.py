import os
from tkinter import Tk, Label, Entry, Button, StringVar, messagebox, OptionMenu, ttk
from pytube import YouTube
from threading import Thread

class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Downloader")
        self.root.geometry("700x400")  # Set the screen size

        # Styling with ttk
        style = ttk.Style()

        # Set the color scheme to red and blue
        style.theme_create("custom", settings={
            "TLabel": {"configure": {"background": "red", "foreground": "white", "padding": 6, "font": ("Helvetica", 12)}},
            "TButton": {"configure": {"background": "blue", "foreground": "white", "padding": 6, "font": ("Helvetica", 12)}},
            "TEntry": {"configure": {"background": "white", "padding": 6, "font": ("Helvetica", 12)}},
            "TCombobox": {"configure": {"background": "white", "padding": 6, "font": ("Helvetica", 12)}}
        })

        style.theme_use("custom")

        self.url_label = ttk.Label(root, text="Enter YouTube URL:")
        self.url_label.pack(pady=10)

        self.url_var = StringVar()
        self.url_entry = ttk.Entry(root, textvariable=self.url_var, width=40)
        self.url_entry.pack(pady=10)

        self.resolution_label = ttk.Label(root, text="Select Resolution:")
        self.resolution_label.pack(pady=5)

        self.resolutions = StringVar(root)
        self.resolutions.set("Select Resolution")

        self.resolution_options = ["720p", "480p", "360p", "240p"]
        self.resolution_dropdown = ttk.Combobox(root, textvariable=self.resolutions, values=self.resolution_options)
        self.resolution_dropdown.pack(pady=5)

        self.download_button = ttk.Button(root, text="Download", command=self.start_download)
        self.download_button.pack(pady=10)

        self.exit_button = ttk.Button(root, text="Exit", command=root.destroy)
        self.exit_button.pack(pady=10)

        self.progress_bar = ttk.Progressbar(root, mode="determinate", length=200)
        self.progress_bar.pack(pady=10)

    def start_download(self):
        self.progress_bar.start()
        download_thread = Thread(target=self.download_video)
        download_thread.start()

    def download_video(self):
        url = self.url_var.get()
        resolution = self.resolutions.get()

        try:
            yt = YouTube(url)
            video = yt.streams.filter(progressive=True, file_extension="mp4", resolution=resolution).first()

            download_folder = os.path.expanduser("~")  # Change this to your desired download folder
            video.download()

            messagebox.showinfo("Success", "Download complete!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
        finally:
            self.progress_bar.stop()

if __name__ == "__main__":
    root = Tk()
    app = YouTubeDownloader(root)
    root.mainloop()
