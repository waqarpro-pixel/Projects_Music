"""Music Player"""
import os
from tkinter import *
import pygame
from tkinter import filedialog
root = Tk()
root.title("Musicyer By Waqar")
root.iconbitmap("indexs.ico")
root.geometry("600x500")

# Intialize the Player
pygame.mixer.init()


# Addinng Song Function
def addingsong():
    songs = filedialog.askopenfilename(defaultextension="songs/",title="Choose the Song",filetype=(("mp3 files","*.mp3"),))
    #songs = songs.replace("C:\Waqar\Desktop\songs","")
    #songs = songs.replace(".mp3","")

    # Add Songs to ListBox
    song_box.insert(END,songs)

# Play Selcted Songs
def play():
    songs = song_box.get(ACTIVE)
    #songs = f"C:\Waqar\Desktop\songs{songs}.mp3"
    pygame.mixer.music.load(songs)
    pygame.mixer.music.play(loops=0)






# Creating Song Box
song_box = Listbox(root,bg="black",fg="white",width=60,selectbackground="green")
song_box.pack(pady=30)

# Create Buttons for Player / Images
back_btn = PhotoImage(file="Fast-backward-icon.png")
forward_btn = PhotoImage(file="Button-Forward-icon.png")
play_btn = PhotoImage(file="Button-Play-icon.png")
pause_btn = PhotoImage(file="Button-Pause-icon.png")
stop_btn = PhotoImage(file="Button-Stop-icon.png")

# Frame Players Button
control_frame =  Frame(root)
control_frame.pack()

# Control Button Players
back_but  =  Button(control_frame,image=back_btn,borderwidth=0)
forward_but = Button(control_frame,image=forward_btn,borderwidth=0)
play_but =  Button(control_frame,image=play_btn,borderwidth=0,command=play)
pause_but =  Button(control_frame,image=pause_btn,borderwidth=0)
stop_but =  Button(control_frame,image=stop_btn,borderwidth=0)

back_but.grid(row=0,column=0,padx=10)
forward_but.grid(row=0,column=1,padx=10)
play_but.grid(row=0,column=2,padx=10)
pause_but.grid(row=0,column=3,padx=10)
stop_but.grid(row=0,column=4,padx=10)

# Create Menus
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Song Menus
add_song = Menu(my_menu)
my_menu.add_cascade(label="Adding Songs",menu=add_song)
add_song.add_command(label="Adding in the Playlist",command=addingsong)


root.mainloop()