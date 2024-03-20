import tkinter as tk
from tkinter import messagebox
import pyshorteners

class URLShortenerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("URL Shortener")

        self.long_url_label = tk.Label(root, text="Enter Long URL:")
        self.long_url_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

        self.long_url_entry = tk.Entry(root, width=50)
        self.long_url_entry.grid(row=0, column=1, padx=5, pady=5)

        self.shorten_button = tk.Button(root, text="Shorten URL", command=self.shorten_url)
        self.shorten_button.grid(row=0, column=2, padx=5, pady=5)

        self.short_url_label = tk.Label(root, text="Shortened URL:")
        self.short_url_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

        self.short_url_entry = tk.Entry(root, width=50, state='readonly')
        self.short_url_entry.grid(row=1, column=1, padx=5, pady=5)

        self.copy_button = tk.Button(root, text="Copy", command=self.copy_short_url)
        self.copy_button.grid(row=1, column=2, padx=5, pady=5)

        self.shortener = pyshorteners.Shortener()

    def shorten_url(self):
        long_url = self.long_url_entry.get()
        if long_url:
            try:
                short_url = self.shortener.tinyurl.short(long_url)
                self.short_url_entry.config(state='normal')
                self.short_url_entry.delete(0, tk.END)
                self.short_url_entry.insert(0, short_url)
                self.short_url_entry.config(state='readonly')
            except Exception as e:
                messagebox.showerror("Error", str(e))
        else:
            messagebox.showerror("Error", "Please enter a URL.")

    def copy_short_url(self):
        short_url = self.short_url_entry.get()
        if short_url:
            self.root.clipboard_clear()
            self.root.clipboard_append(short_url)
            messagebox.showinfo("Success", "Short URL copied to clipboard.")
        else:
            messagebox.showerror("Error", "No URL to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    app = URLShortenerApp(root)
    root.mainloop()
