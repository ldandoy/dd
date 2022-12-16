from tkinter import *
import pygame
import os, glob
import tkinter as tk
from random import *
from functools import partial
from Perso.person import *
from Utils.Sound import Sound
from Window.new_character import *
from Perso import * 





class Personnage(DefaultController) :
    def __init__(self, name, image, pv):
        self.name = name
        self.image = image
        self.pdv = pv
       
    def get_name(self):
        return self.name

    def get_image(self):
        return self.image

   
    def get_pdv(self):
        return self.pv

    def get_name_from_character_selection(self):
        return self.name


    def character_show(self) :
      print("hello")  
      #frameshow = Frame(self.q, width=1024, height=600, bg='black')
      #print(frameshow)
      #card = Canvas(frameshow, width=650, height=154, bg='black')
      #card.place(x=105, y=420)
      #image_path = os.path.join(self.base_folder, '../medias/character/' + self.image)
      #bg = PhotoImage(file=image_path)
      #canvas = Canvas(frameshow, width=150, height=150)
      #canvas.place(x=105, y=150)
      #canvas.create_image(0, 0, image=bg, anchor="nw")
      #canvas.image = bg
      #lname = Label(frameshow, text=self.name, fg='white', bg='black')
      #lnamefont = ('Calibri (Body)', 24, 'bold')
      #lname.config(font=lnamefont)
      #lname.place(x=105, y=100)
      #lpv = Label(frameshow, text=self.pv, fg='white', bg='black')
      #lpvfont = ('Calibri (Body)', 24, 'bold')
      #lpv.config(font=lpvfont)
      #lpv.place(x=105, y=300)
      #lwelcome = Label(frameshow, text="Voici votre personnage", fg='white', bg='black')
      #lwelcomefont = ('Calibri (Body)', 24, 'bold')
      #lwelcome.config(font=lwelcomefont)
      #lwelcome.place(x=105, y=30)





