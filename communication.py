import tkinter as tk

def open_instagram():
    import webbrowser
    webbrowser.open("https://www.instagram.com/r94xs/")

window = tk.Tk()
window.title("روابط التواصل الاجتماعي")

entry = tk.Entry(window)
entry.pack()

instagram_button = tk.Button(window, text="Instagram", command=open_instagram)
instagram_button.pack()

window.mainloop()
           
