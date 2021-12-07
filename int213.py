import tkinter
from tkinter import *
from tkinter import filedialog
from tkinter import ttk
import pygame
root=tkinter.Tk()
root.title("MP3 Player")
root.geometry("400x250")

#Initialize pygame
pygame.mixer.init()

def add_song():
    song = filedialog.askopenfilename(title="Choose a song", filetypes=(("mp3 files","*.mp3"),))
    song = song.replace("C:/Users/hp/Desktop/mp3/audio/","")
    song = song.replace(".mp3","")
    song_list.insert(END, song)

def add_many_songs():
       songs = filedialog.askopenfilenames(title="Choose a song", filetypes=(("mp3 files", "*.mp3"),))
       for song in songs:
           song = song.replace("C:/Users/hp/Desktop/mp3/audio/", "")
           song = song.replace(".mp3", "")
           song_list.insert(END, song)

def play_song():
    song = song_list.get(ACTIVE)
    song = f'C:/Users/hp/Desktop/mp3/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop_song():
    pygame.mixer.music.stop()
    song_list.selection_clear(ACTIVE)

def next_song():
    current_one = song_list.curselection()
    next_one = current_one[0]+1
    song = song_list.get(next_one)
    song = f'C:/Users/hp/Desktop/mp3/audio/{song}.mp3'
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_list.selection_clear(0, END)
    song_list.activate(next_one)
    song_list.selection_set(next_one, last=None)

def previous_song():
     current_one = song_list.curselection()
     previous_one = current_one[0] - 1
     song = song_list.get(previous_one)
     song = f'C:/Users/hp/Desktop/mp3/audio/{song}.mp3'
     pygame.mixer.music.load(song)
     pygame.mixer.music.play(loops=0)
     song_list.selection_clear(0, END)
     song_list.activate(previous_one)
     song_list.selection_set(previous_one, last=None)

global paused
paused = False
def pause_song(is_paused):
   global paused
   paused = is_paused
   if paused:
       pygame.mixer.music.unpause()
       paused=False
   else:
       pygame.mixer.music.pause()
       paused=True  

def delete_song():
    song_list.delete(ANCHOR)
    pygame.mixer.music.stop()  

def delete_all_songs():
    song_list.delete(0, END)
    pygame.mixer.music.stop()  

#List box
song_list= Listbox(root,bg="black",fg="white",width=60)
song_list.pack(pady=20)

#Images to Buttons
Play_btn_image= PhotoImage(file='C:\\Users\\hp\\Desktop\\mp3\\images\\playbutton50.png') 

Pause_btn_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\mp3\\images\\pausebutton50.png')

Stop_btn_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\mp3\\images\\stopbutton50.png')

Back_btn_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\mp3\\images\\backbutton50.png')

Forward_btn_image = PhotoImage(file='C:\\Users\\hp\\Desktop\\mp3\\images\\forwardbutton50.png')

#Frame for button to be in same line
contols_frame = Frame(root)
contols_frame.pack()

#Butttons Controls
Play_btn = Button(contols_frame, image=Play_btn_image,borderwidth=0,command=play_song)

Pause_btn = Button(contols_frame, image=Pause_btn_image,borderwidth=0,command=lambda : pause_song(paused))

Stop_btn = Button(contols_frame, image=Stop_btn_image,borderwidth=0,command=stop_song)

Back_btn = Button(contols_frame, image=Back_btn_image,borderwidth=0,command=previous_song)

Forward_btn = Button(contols_frame, image=Forward_btn_image,borderwidth=0,command=next_song)

#Using Grid
Back_btn.grid(row=0,column=0)
Pause_btn.grid(row=0,column=1)
Play_btn.grid(row=0,column=2)
Stop_btn.grid(row=0,column=3)
Forward_btn.grid(row=0,column=4)

my_menu = Menu(root)
root.config(menu=my_menu)
add_songs = Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_songs)
add_songs.add_command(label="Add One Song ",command=add_song)
add_songs.add_command(label="Add Many Songs",command=add_many_songs)
remove_songs = Menu(my_menu)
my_menu.add_cascade(label="Delete Songs",menu=remove_songs)
remove_songs.add_command(label="Delete One Song",command=delete_song)
remove_songs.add_command(label="Delete ALL Songs",command=delete_all_songs)
