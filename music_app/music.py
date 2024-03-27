import os
import sys
import pygame
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui, QtWidgets

class Form(QWidget):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 687, 411)
        self.setWindowTitle("Music player")
        

        self.label = QLabel(self)
        self.label.setGeometry(-20, -50, 771, 511)


        self.label.setPixmap(QPixmap('Wallpaper Gif Full HD - Rhenan Lourenço ®.jpg'))
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
        self.music_list = ['ShapurKerkere-320.mp3' , 'Ehtemalan Ghahremani Dar Kar Nist.mp3' , 'Tom-Odell-another-love1.mp3' ,
                            'i love you.mp3' , 'Toomaj - Tifus.mp3' , 'Pastlives - sapientdream.mp3',
                                'Cant Get You out Of My Head.mp3' , 'i dont like it, youre not the same.mp3' , 
                                    'Mockingbird.mp3' , 'dance with me.mp3' , 'Space Song.mp3' , 'Six Feet Under.mp3',
                                        'Roozhaaye Khoobe Koodaki.mp3' , 'Losing Interest.mp3' , 'Freaks but Slowed Muffled Echo.mp3' , 'Its Not So Bad.mp3' , 'Reza Pishro - Ghabrestoune Hip Hop.mp3' , 'Palangi.mp3', 'Baby Bebin Baroone.mp3' , 'Cigare Soorati.mp3' , 'WASTE - Slowed Version.mp3' , 'Ending.mp3','Age Ye Rooz - Remix.mp3' , 'Erfan, Gdaal, Imanemun - Be Yade - Remix.mp3' , 'Cheri Cheri Lady.mp3' , 'Billie Eilish - TV.mp3' , 'Hope.mp3' , 'Fairytale.mp3' , 'Shootout.mp3' , 'Powfu, beabadoobee - death bed (coffee for your head).mp3', 'ASADI, Erfan, Xye - Hide & Seek.mp3' , 'AirplaneMode.mp3' , 'tommymuzzic_another_love_x_summertime_sadness.mp3' , 'Billie Eilish - lovely (with Khalid).mp3']
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

        elif self.lineEdit.text()=="cant get you out of my head":
            pygame.init()
            pygame.mixer.music.load(self.music_list[6])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="i dont like it":
            pygame.init()
            pygame.mixer.music.load(self.music_list[7])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="mockingbird":
            pygame.init()
            pygame.mixer.music.load(self.music_list[8])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="dance with me":
            pygame.init()
            pygame.mixer.music.load(self.music_list[9])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="space song":
            pygame.init()
            pygame.mixer.music.load(self.music_list[10])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="six feet under":
            pygame.init()
            pygame.mixer.music.load(self.music_list[11])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="rooz haaye khob":
            pygame.init()
            pygame.mixer.music.load(self.music_list[12])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="losing intrest":
            pygame.init()
            pygame.mixer.music.load(self.music_list[13])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="its not so bad":
            pygame.init()
            pygame.mixer.music.load(self.music_list[14])
            pygame.mixer.music.play()


        elif self.lineEdit.text()=="freaks but":
            pygame.init()
            pygame.mixer.music.load(self.music_list[15])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="ghabrestoune hip hop":
            pygame.init()
            pygame.mixer.music.load(self.music_list[16])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="palangi":
            pygame.init()
            pygame.mixer.music.load(self.music_list[17])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="baby bebin baroone":
            pygame.init()
            pygame.mixer.music.load(self.music_list[18])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="cigar soorati":
            pygame.init()
            pygame.mixer.music.load(self.music_list[19])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="waste":
            pygame.init()
            pygame.mixer.music.load(self.music_list[20])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="ending":
            pygame.init()
            pygame.mixer.music.load(self.music_list[21])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="age ye rooz erfan":
            pygame.init()
            pygame.mixer.music.load(self.music_list[22])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="be yade":
            pygame.init()
            pygame.mixer.music.load(self.music_list[23])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="cheri cheri lady":
            pygame.init()
            pygame.mixer.music.load(self.music_list[24])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="tv":
            pygame.init()
            pygame.mixer.music.load(self.music_list[25])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="hop":
            pygame.init()
            pygame.mixer.music.load(self.music_list[26])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="fairytale":
            pygame.init()
            pygame.mixer.music.load(self.music_list[27])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="shootout":
            pygame.init()
            pygame.mixer.music.load(self.music_list[28])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="coffe for your head":
            pygame.init()
            pygame.mixer.music.load(self.music_list[29])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="hide and seek":
            pygame.init()
            pygame.mixer.music.load(self.music_list[30])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="airplanemode":
            pygame.init()
            pygame.mixer.music.load(self.music_list[31])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="remix another love and summer sadness":
            pygame.init()
            pygame.mixer.music.load(self.music_list[32])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="lovely":
            pygame.init()
            pygame.mixer.music.load(self.music_list[33])
            pygame.mixer.music.play()

        # show message if the user doesn't type any music
        elif self.lineEdit.text()=="":
            message=QMessageBox()
            message.setText("Select the music")
            message.exec()

           # show messgae if tne music not found
        else:
            message2=QMessageBox()
            message2.setText("i dont have this music")
            message2.exec()
            
    # for pause music
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