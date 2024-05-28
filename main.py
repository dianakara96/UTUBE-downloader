


import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
from pytube import YouTube
import psycopg2

DB_USER = "postgres"
DB_PASSWORD = "diana2006"
DB_HOST = "localhost"
DB_PORT = "5432"
DB_DATABASE = "youtube"
class YouTubeDownloader:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x400")
        self.root.title("YouTube Downloader")
        self.setup_ui()
        self.create_table_if_not_exists()
        self.show_stored_data()
    def setup_ui(self):
        tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        self.link = tk.StringVar()
        tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
        link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
        link_entry.pack()
        self.download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
        self.download_button.pack()
        self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', length=400, mode='determinate')
        self.progress_bar.pack(pady=10)
    def download_video(self):
        self.download_button.config(state='disabled')
        url = self.link.get()
        try:
            yt = YouTube(url, on_progress_callback=self.show_progress)
            self.start_download(yt)
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.download_button.config(state='normal')
    def start_download(self, yt):
        try:
            stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
            self.progress_bar.start(10)
            stream.download(output_path='./downloads')
            self.progress_bar.stop()
            self.save_to_database(yt.title, yt.watch_url)
            messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
        except Exception as e:
            messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")
        finally:
            self.download_button.config(state='normal')
    def save_to_database(self, title, url):
        connection = None
        try:
            connection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_DATABASE)
            cursor = connection.cursor()
            postgres_insert_query = """ INSERT INTO youtube_videos (title, url) VALUES (%s, %s)"""
            cursor.execute(postgres_insert_query, (title, url))
            connection.commit()
            count = cursor.rowcount
            print(f"{count} Record inserted successfully into youtube_videos table")
        except (Exception, psycopg2.Error) as error:
            print("Failed to insert record into youtube_videos table", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    def create_table_if_not_exists(self):
        connection = None
        try:
            connection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_DATABASE)
            cursor = connection.cursor()
            create_table_query = """
            CREATE TABLE IF NOT EXISTS youtube_videos (
                id SERIAL PRIMARY KEY,
                title VARCHAR(255) NOT NULL,
                url TEXT NOT NULL,
                download_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            );
            """
            cursor.execute(create_table_query)
            connection.commit()
        except (Exception, psycopg2.Error) as error:
            print("Failed to create table youtube_videos", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
    def show_progress(self, stream, chunk, bytes_remaining):
        total_bytes = stream.filesize
        bytes_downloaded = total_bytes - bytes_remaining
        percentage = (bytes_downloaded / total_bytes) * 100
        self.progress_bar['value'] = percentage
        self.root.update_idletasks()
    def show_stored_data(self):
        connection = None
        try:
            connection = psycopg2.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_DATABASE)
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM youtube_videos;")
            rows = cursor.fetchall()
            if rows:
                print("Stored Data:")
                for row in rows:
                    print("ID =", row[0], "Title =", row[1], "URL =", row[2], "download_date=", row[3])
            else:
                print("No data stored in the database.")
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            if connection:
                cursor.close()
                connection.close()
if __name__ == "__main__":
    root = tk.Tk()
    app = YouTubeDownloader(root)
    root.mainloop()