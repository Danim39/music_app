import os
import sys
import pygame
import termcolor
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 687, 411)
        self.setWindowTitle("music")
        

        self.label = QLabel(self)
        self.label.setGeometry(-20, -50, 771, 511)
        self.label.setPixmap(QPixmap("Wallpaper Gif Full HD - Rhenan Lourenço ®.jpg"))
        #button
        self.pushButton = QPushButton("Play", self)
        self.pushButton.setGeometry(280, 100, 141, 31)
        self.pushButton.setFont(QFont("MV Boli", 12))
        self.pushButton.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton.clicked.connect(self.play_music)
        #line Edir(Enter Text)
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(140, 40, 411, 41)
        self.lineEdit.setStyleSheet("background-color: rgb(0, 0, 0); color: mediumpurple;")  # Set text color to red

        self.lineEdit.setFont(QFont("MV Boli", 12))
        #button
        self.pushButton_2 = QPushButton("Pause", self)
        self.pushButton_2.setGeometry(280, 190, 141, 31)
        self.pushButton_2.setFont(QFont("MV Boli", 12))
        self.pushButton_2.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton_2.clicked.connect(self.pause_music)
        self.pushButton_2.clicked.connect(self.text)

        self.pushButton3 = QPushButton("Close", self)
        self.pushButton3.setGeometry(280, 350, 141, 31)
        self.pushButton3.setFont(QFont("MV Boli", 12))
        self.pushButton3.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton3.clicked.connect(self.close_form)



        self.pushButton4 = QPushButton("resume", self)
        self.pushButton4.setGeometry(280, 270, 141, 31)
        self.pushButton4.setFont(QFont("MV Boli", 12))
        self.pushButton4.setStyleSheet("background-color: rgb(170, 0, 255);")
        self.pushButton4.clicked.connect(self.unpause_music)

    #for close app
    def close_form(self):
        self.close()
    #for play music
    def play_music(self):
        #
        self.music_list = ['ShapurKerkere-320.mp3' , 'Ehtemalan Ghahremani Dar Kar Nist.mp3' , 'Tom-Odell-another-love1.mp3' ,\
                            'i love you.mp3' , 'Toomaj - Tifus.mp3' , 'Pastlives - sapientdream.mp3',\
                                'Cant Get You out Of My Head.mp3' , 'i dont like it, youre not the same.mp3']
            #Line Edit (Enter text for play music)        
        if self.lineEdit.text() == "kerkere":
            pygame.init()
            
            pygame.mixer.music.load(self.music_list[0])
            pygame.mixer.music.play()
            
        elif self.lineEdit.text()=="gharemani dar kar nist":
            pygame.init()
            pygame.mixer.music.load(self.music_list[1])
            pygame.mixer.music.play()
        elif self.lineEdit.text()=="another love":
            pygame.init()
            pygame.mixer.music.load(self.music_list[2])
            pygame.mixer.music.play()
        elif self.lineEdit.text()=="i love you":
            pygame.init()
            pygame.mixer.music.load(self.music_list[3])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="tifus":
            pygame.init()
            pygame.mixer.music.load(self.music_list[4])
            pygame.mixer.music.play()


        elif self.lineEdit.text()=="past lives":
            pygame.init()
            pygame.mixer.music.load(self.music_list[5])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="cant get you":
            pygame.init()
            pygame.mixer.music.load(self.music_list[6])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="i dont like it":
            pygame.init()
            pygame.mixer.music.load(self.music_list[7])
            pygame.mixer.music.play()

        # show message if the user doesn't type any music
        else:
            message=QMessageBox()
            message.setText("i dont have this music sorry:)")
            message.exec()
    # for puse music
    def pause_music(self):
        pygame.init()
        pygame.mixer.music.pause()

    #for resume music
    
    def unpause_music(self):
        pygame.init()
        pygame.mixer.music.unpause()

    # show message if the user select no music to pause
    def text(self):
        if self.lineEdit.text()=="":
            message=QMessageBox()
            message.setText("You have no music to pause")
            message.exec()
            

app = QApplication(sys.argv)
form = Form()
# Show app

form.show()
sys.exit(app.exec())
