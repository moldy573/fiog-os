#requierments
try:
    import tkinter as tk
    from tkinter import Menu
    from tkinter import Toplevel
    from tkinter import messagebox
    import subprocess
    from PIL import Image, ImageTk
    import sounddevice as sd
    import soundfile as sf
    import pygetwindow as gw
    import os
except ImportError:
    print("plz install tkinter to procced")
    result = subprocess.run('plz install missing modules', shell=True, capture_output=True, text=True)

    print(result.stdout)
#config
about_window=None
killapp=0
opened, fs=sf.read(r'C:\Users\Bradf\OneDrive\Documents\python projects\images-sounds\fiog-os-program.wav')
data, fs=sf.read(r'C:\Users\Bradf\OneDrive\Documents\python projects\images-sounds\fiogos.wav')
sd.play(data, fs)
root = tk.Tk()
root.configure(bg='dark blue')
root.title("fiog os")
root.geometry("500x400+500+200")
icon=ImageTk.PhotoImage(Image.open(r"C:\Users\Bradf\OneDrive\Documents\python projects\images-sounds\fiog os logo.png"))
root.iconphoto(True, icon)
global password2
password2 = tk.StringVar()
#bar
entryb = tk.Entry(root, width=150)
entryb.pack(pady=120)
kill_lock=tk.Button(root, text="quit", command=root.quit)
options = Menu(root)
options_menu = Menu(options, tearoff=0)
options_menu.add_command(label="shutdown", command=lambda:shutdown(), activebackground="blue", activeforeground='black')
options_menu.add_command(label="restart", command=lambda:restart(), activebackground="blue", activeforeground='black')
options_menu.add_command(label="settings", command=lambda:settings(), activebackground="blue", activeforeground='black')
options_menu.add_command(label="about", command=lambda:about(), activebackground="blue", activeforeground='black')
entryb.pack_forget()
options_menu.pack_forget()

    
#shows the lock screen
def passbutton():
    password5.pack()
    entryb.pack(pady=20)
    kill_lock.pack(pady=30)
#def caller
def password1():
    ac2()
    pinput = entryb.get()
#checks the entry
def ac2():
    main=tk.Label(root, text="hi")
    main.pack(pady=120)
    root.after(200)
    pinput = entryb.get()
    if entryb.get() == password2.get():
        root.configure(bg="dark cyan")
        entryb.pack_forget()
        password5.pack_forget()
        main.pack_forget()
        root.config(menu=options_menu)
        kill_lock.pack_forget()
        
    else:
        main.config(text="failed to log in")
        root.after(1000, main.destroy)
#restart
def restart():
    global settings
    root.configure(bg="black")
    root.configure(menu="")
    password5 = tk.Button(root, text="submit", bg="white", command=password1)
    password5.pack(pady=20)
    password5.pack_forget()
    boot = tk.Label(root, text="fiog os", bg="black", width=20, height=5, anchor="center", fg="white")
    boot.pack(expand=True, fill="both")
    data, fs=sf.read(r'C:\Users\Bradf\OneDrive\Documents\python projects\images-sounds\fiogos.wav')
    sd.play(data, fs)
    root.config(bg="dark blue")
    root.after(3200, boot.destroy)
    root.after(3000, passbutton)
#get entry password
def boot_entry():
    pinput = entryb.get()
#boot up
password5 = tk.Button(root, text="submit", bg="white", command=password1)
password5.pack(pady=20)
password5.pack_forget()
boot = tk.Label(root, text="fiog os", bg="black", width=20, height=5, anchor="center", fg="white")
boot.pack(expand=True, fill="both")
root.after(3200, boot.destroy)
root.after(3000, passbutton)

#settings window
def settings():
    settings = tk.Toplevel(root)
    settings.title("fiog os (settings)")
    settings.geometry("300x200+600+300")
    settings.configure(bg="black")
    sd.play(opened, fs)
    #the welcome label
    settings_label = tk.Label(settings, text="welcome", bg="black", fg="white")
    settings_label.pack()
    #quit
    quit_set=tk.Button(settings, text="quit", command=settings.destroy)
    quit_set.pack()
    #password
    def password():
        submit_pass = tk.Button(settings, text="submit", command=lambda:(entrys.pack_forget(), submit_pass.pack_forget(), password2.set(entrys.get())))
        submit_pass.pack()
        entrys = tk.Entry(settings, width=120)
        entrys.pack(pady=10)
    #the button
    password_butt = tk.Button(settings, text="password", command=password)
    password_butt.pack()
#about window
def about():
        about_window=tk.Toplevel(root)
        about_window.title("fiog-os")
        aboutttt=tk.Label(about_window, text="Fiog OS:stone")
        sd.play(opened, fs)
        aboutttt.pack()
        aboutt=tk.Label(about_window, text="last updated 2/16/2025 11:59 AM")
        abouttt=tk.Label(about_window, text="by bradford mapes")
        abouttttt=tk.Label(about_window, text="Build ver:stone")
        aboutttt.pack()
        abouttt.pack()
        aboutt.pack()
        abouttttt.pack()
        about_window.geometry("300x200+600+100")
        quit_abo=tk.Button(about_window, text="quit", command=about_window.destroy)
        quit_abo.pack()
       
#shutdown
def shutdown():
    root.configure(bg="black")
    root.configure(menu="")
    shutdown1, fs=sf.read(r'C:\Users\Bradf\OneDrive\Documents\python projects\images-sounds\shutdown-fiog-os.wav')
    sd.play(shutdown1, fs)
    sd.wait()
    root.quit()


#the main loop
root.mainloop()
