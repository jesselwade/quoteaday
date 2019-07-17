import tkinter as tk
import requests as req


master = tk.Tk()
master.title("Quote a Day")

quote = req.get("http://quotes.rest/qod.json").json()
qod = quote['contents']['quotes'][0]['quote'] + '\n - ' + quote['contents']['quotes'][0]['author']

msg = tk.Message(master, text = qod, anchor='nw', aspect=200)
msg.config(bg='lightgreen', font=('verdana', 18))
msg.pack()

tk.mainloop()
