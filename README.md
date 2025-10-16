# 🎥 YouTube Downloader GUI

A simple and user-friendly Python application that lets you download YouTube videos with a graphical interface. Just paste the video URL, select your preferred resolution, and download\!



## ✨ Features

  - **Easy to Use:** A straightforward GUI makes it simple to download videos.
  - **Resolution Selection:** Choose from a list of available resolutions (720p, 480p, 360p, 240p).
  - **Progress Bar:** A progress bar indicates when the download is in progress.
  - **Download Status:** Get a notification when your download is complete or if an error occurs.



## 💻 Requirements

To run this application, you need to have Python installed on your system. You'll also need the following libraries, which you can install using pip:

  - `pytube`: For downloading YouTube videos.
  - `tkinter`: Python's standard GUI library (usually included with Python).
  - `ttk`: Themed Tkinter, for better styling.

You can install `pytube` by running this command in your terminal:

```bash
pip install pytube
```



## 🚀 How to Run

1.  **Clone the repository** or download the project files.

2.  **Navigate** to the project directory in your terminal.

3.  **Run the Python script:**

    ```bash
    python Youtube_VDownloader.py
    ```





## 🔧 How It Works

This application is built with the **Tkinter** library for its graphical user interface. The backend uses the **Pytube** library to handle the video downloading process. When you click the "Download" button, the program gets the URL and desired resolution, and a new **thread** is started to prevent the GUI from freezing. This thread then uses **Pytube** to find the video stream with the specified resolution and downloads it to your user's home directory.

-----

## ✍️ Contribution

If you have any suggestions or find a bug, feel free to open an issue or submit a pull request. Your contributions are welcome\!
