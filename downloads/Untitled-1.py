



# import tkinter as tk
# from tkinter import messagebox
# from pytube import YouTube
# import threading

# class YouTubeDownloader:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("600x400")
#         self.root.title("YouTube Downloader")
        
#         self.setup_ui()

#     def setup_ui(self):
#         tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        
#         self.link = tk.StringVar()
#         tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
#         link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
#         link_entry.pack()
        
#         download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
#         download_button.pack()

#         self.download_list = tk.Listbox(self.root, width=80, height=10)
#         self.download_list.pack(pady=10)
        
#     def download_video(self):
#         url = self.link.get()
#         try:
#             yt = YouTube(url)
#             stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             download_thread = threading.Thread(target=self.start_download, args=(yt, stream))
#             download_thread.start()
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
    
#     def start_download(self, yt, stream):
#         try:
#             self.download_list.insert(tk.END, f"Downloading: {yt.title}")
#             stream.download(output_path='./downloads')
#             self.download_list.delete(tk.END)
#             messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
#         except Exception as e:
#             messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeDownloader(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from pytube import YouTube
# import threading
# import time

# class YouTubeDownloader:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("600x400")
#         self.root.title("YouTube Downloader")
        
#         self.setup_ui()

#     def setup_ui(self):
#         tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        
#         self.link = tk.StringVar()
#         tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
#         link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
#         link_entry.pack()
        
#         self.download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
#         self.download_button.pack()

#         self.download_list = tk.Listbox(self.root, width=60, height=5)
#         self.download_list.pack(pady=10)
        
#     def download_video(self):
#         self.download_button.config(state='disabled')  
#         url = self.link.get()
#         try:
#             yt = YouTube(url)
#             self.download_list.insert(tk.END, f"Downloading: {yt.title}")
#             self.root.after(2000, self.start_download, yt)
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
#             self.download_button.config(state='normal')  
    
#     def start_download(self, yt):
#         try:
#             stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             stream.download(output_path='./downloads')
#             self.download_list.delete(tk.END)
#             messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
#         except Exception as e:
#             messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")
#         self.download_button.config(state='normal') 

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeDownloader(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from pytube import YouTube
# import psycopg2  

# class YouTubeDownloader:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("600x400")
#         self.root.title("YouTube Downloader")
        
#         self.setup_ui()

#     def setup_ui(self):
#         tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        
#         self.link = tk.StringVar()
#         tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
#         link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
#         link_entry.pack()
        
#         self.download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
#         self.download_button.pack()

#         self.download_list = tk.Listbox(self.root, width=60, height=5)
#         self.download_list.pack(pady=10)
        
#     def download_video(self):
#         self.download_button.config(state='disabled')  
#         url = self.link.get()
#         try:
#             yt = YouTube(url)
#             self.download_list.insert(tk.END, f"Downloading: {yt.title}")
#             self.root.after(2000, self.start_download, yt)
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
#             self.download_button.config(state='normal')  
    
#     def start_download(self, yt):
#         try:
#             stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             stream.download(output_path='./downloads')
#             self.download_list.delete(tk.END)
#             self.save_to_database(yt.title, yt.watch_url)
#             messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
#         except Exception as e:
#             messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")
#         self.download_button.config(state='normal') 

#     def save_to_database(self, title, url):
#         try:
#             connection = psycopg2.connect(user="postgres",
#                                           password="diana2006",
#                                           host="localhost",
#                                           port="5432",
#                                           database="youtube")
#             cursor = connection.cursor()
#             postgres_insert_query = """ INSERT INTO youtube_videos (title, url) VALUES (%s,%s)"""
#             record_to_insert = (title, url)
#             cursor.execute(postgres_insert_query, record_to_insert)
#             connection.commit()
#             count = cursor.rowcount
#             print(count, "Record inserted successfully into youtube_videos table")
#         except (Exception, psycopg2.Error) as error:
#             if(connection):
#                 print("Failed to insert record into youtube_videos table", error)
#         finally:
#             if(connection):
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeDownloader(root)
#     root.mainloop()

# import tkinter as tk
# from tkinter import messagebox
# from pytube import YouTube
# import psycopg2  

# class YouTubeDownloader:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("600x400")
#         self.root.title("YouTube Downloader")
        
#         self.setup_ui()

#     def setup_ui(self):
#         tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        
#         self.link = tk.StringVar()
#         tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
#         link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
#         link_entry.pack()
        
#         self.download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
#         self.download_button.pack()

#         self.download_list = tk.Listbox(self.root, width=60, height=5)
#         self.download_list.pack(pady=10)
        
#     def download_video(self):
#         self.download_button.config(state='disabled')  
#         url = self.link.get()
#         try:
#             yt = YouTube(url)
#             self.download_list.insert(tk.END, f"Downloading: {yt.title}")
#             self.start_download(yt) 
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
#             self.download_button.config(state='normal')  
    
#     def start_download(self, yt):
#         try:
#             stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             stream.download(output_path='./downloads')
#             self.download_list.delete(tk.END)
#             self.save_to_database(yt.title, yt.watch_url)
#             messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
#         except Exception as e:
#             messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")
#         finally:
#             self.download_button.config(state='normal')

#     def save_to_database(self, title, url):
#         try:
#             connection = psycopg2.connect(user="postgres",
#                                           password="diana2006",
#                                           host="localhost",
#                                           port="5432",
#                                           database="youtube")
#             cursor = connection.cursor()
#             postgres_insert_query = """ INSERT INTO youtube_videos (title, url) VALUES (%s,%s)"""
#             record_to_insert = (title, url)
#             cursor.execute(postgres_insert_query, record_to_insert)
#             connection.commit()
#             count = cursor.rowcount
#             print(count, "Record inserted successfully into youtube_videos table")
#         except (Exception, psycopg2.Error) as error:
#             if(connection):
#                 print("Failed to insert record into youtube_videos table", error)
#         finally:
#             if(connection):
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeDownloader(root)
#     root.mainloop()





# import tkinter as tk
# from tkinter import messagebox
# from tkinter import ttk
# from pytube import YouTube
# import psycopg2  

# class YouTubeDownloader:
#     def __init__(self, root):
#         self.root = root
#         self.root.geometry("600x400")
#         self.root.title("YouTube Downloader")
        
#         self.setup_ui()

#     def setup_ui(self):
#         tk.Label(self.root, text="YouTube Downloader", font='arial 20 bold').pack()
        
#         self.link = tk.StringVar()
#         tk.Label(self.root, text='Paste Link Here:', font='arial 15 bold').pack()
#         link_entry = tk.Entry(self.root, width=70, textvariable=self.link)
#         link_entry.pack()
        
#         self.download_button = tk.Button(self.root, text='DOWNLOAD', font='roboto 15 bold', bg='red', padx=2, command=self.download_video)
#         self.download_button.pack()

#         self.progress_bar = ttk.Progressbar(self.root, orient='horizontal', length=400, mode='determinate')
#         self.progress_bar.pack(pady=10)

#     def download_video(self):
#         self.download_button.config(state='disabled')  
#         url = self.link.get()
#         try:
#             yt = YouTube(url, on_progress_callback=self.show_progress)
#             self.start_download(yt) 
#         except Exception as e:
#             messagebox.showerror("Error", f"An error occurred: {e}")
#             self.download_button.config(state='normal')  
    
#     def start_download(self, yt):
#         try:
#             stream = yt.streams.filter(progressive=True, file_extension='mp4').first()
#             self.progress_bar.start(10) 
#             stream.download(output_path='./downloads')
#             self.progress_bar.stop()  
#             self.save_to_database(yt.title, yt.watch_url)
#             messagebox.showinfo("Download Complete", f"{yt.title} has been successfully downloaded.")
#         except Exception as e:
#             messagebox.showerror("Download Error", f"An error occurred while downloading: {e}")
#         finally:
#             self.download_button.config(state='normal')

#     def save_to_database(self, title, url):
#         try:
#             connection = psycopg2.connect(user="postgres",
#                                           password="diana2006",
#                                           host="localhost",
#                                           port="5432",
#                                           database="youtube")
#             cursor = connection.cursor()
#             postgres_insert_query = """ INSERT INTO youtube_videos (title, url) VALUES (%s,%s)"""
#             record_to_insert = (title, url)
#             cursor.execute(postgres_insert_query, record_to_insert)
#             connection.commit()
#             count = cursor.rowcount
#             print(count, "Record inserted successfully into youtube_videos table")
#         except (Exception, psycopg2.Error) as error:
#             if(connection):
#                 print("Failed to insert record into youtube_videos table", error)
#         finally:
#             if(connection):
#                 cursor.close()
#                 connection.close()
#                 print("PostgreSQL connection is closed")

#     def show_progress(self, stream, chunk, bytes_remaining):
#         total_bytes = stream.filesize
#         bytes_downloaded = total_bytes - bytes_remaining
#         percentage = (bytes_downloaded / total_bytes) * 100
#         self.progress_bar['value'] = percentage
#         self.root.update_idletasks()

# if __name__ == "__main__":
#     root = tk.Tk()
#     app = YouTubeDownloader(root)
#     root.mainloop()