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
                                        'Roozhaaye Khoobe Koodaki.mp3' , 'Losing Interest.mp3' , 'Freaks but Slowed Muffled Echo.mp3' , 'Its Not So Bad.mp3' , 'Reza Pishro - Ghabrestoune Hip Hop.mp3' , 'Palangi.mp3', 'Baby Bebin Baroone.mp3' , 'Cigare Soorati.mp3' , 'WASTE - Slowed Version.mp3' , 'Ending.mp3','Age Ye Rooz - Remix.mp3' , 'Erfan, Gdaal, Imanemun - Be Yade - Remix.mp3' , 'Cheri Cheri Lady.mp3' , 'Billie Eilish - TV.mp3' , 'Hope.mp3' , 'Fairytale.mp3' , 'Shootout.mp3' , 'Powfu, beabadoobee - death bed (coffee for your head).mp3', 'ASADI, Erfan, Xye - Hide & Seek.mp3' , 'AirplaneMode.mp3' , 'tommymuzzic_another_love_x_summertime_sadness.mp3' , 'Billie Eilish - lovely (with Khalid).mp3' , 'Arta & Koorosh - Zendegi Hamine.mp3' , 'Go Little Rockstar.mp3' , 'Yas - BEEM  بیم.mp3' , 'Yas - Sarkoob.mp3' ,'Yas - LaL.mp3' , 'NF - The Search.mp3' , 'Rio Romeo - Nothings New.mp3' , 'Khodafez.mp3' , 'AURORA - Runaway.mp3' , 'Summertime Sadn ,ess.mp3' , 'Bawaasir.mp3' , 'Miley Cyrus - Flowers.mp3' , 'LUCKY LOVE - MASCULINITY.mp3' , 'Lil Peep - Star Shopping.mp3' , 'Vengeance.mp3' , 'Yadete (feat. Sogand).mp3' , 'KALEO - Way down We Go.mp3' , '021kid - Naghabel.mp3' , 'Yas - Bad Shodam.mp3' , 'Homage.mp3' , 'w.mp3' , 'Nabz-Pe7aeFp_RTo-192k-1712514228.mp3' , 'Kaftar Bazi-8Eoc-GG6h9E-192k-1712514610.mp3' , 'OD-mxsMr7RdciY-192k-1712613994.mp3' , 'GHORS II-Lw7LWxJnMVg-192k-1712614772.mp3' , 'SLAP feat. Chvrsi -7Iq5G8DsYnY-192k-1712679249.mp3' , 'AZHIR-ZTSyw81WpaQ-192k-1712680355.mp3' , 'you_broke_my_heart_again-oV5af6XGZtg-192k-1712754820.mp3' , 'Silk-IYWg-jGNLvo-192k-1712755203.mp3' , 'Illegal Remix -eIbyHCB00o4-192k-1712822166.mp3' , 'when the partys over.mp3' , 'Oon Dare Mire-Ajvrcd1YzJM-192k-1712980420.mp3' , 'Romantic Homicide-gPDCwmaUSSM-192k-1712980601.mp3' , 'Batman.mp3' , 'Inja Irane.mp3' , 'Pesar.mp3' , 'Yeki Dar Mizane.mp3' , '5AM--Lge44z_veA-192k-1713298508.mp3' , 'Sogand.mp3' , 'i like the way you kiss me.mp3' , 'GHORS II-Lw7LWxJnMVg-192k-1712614772.mp3']
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
            pygame.mixer.music.load(self.music_list[15])
            pygame.mixer.music.play()


        elif self.lineEdit.text()=="freaks but":
            pygame.init()
            pygame.mixer.music.load(self.music_list[14])
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

        elif self.lineEdit.text()=="zendegi hamine":
            pygame.init()
            pygame.mixer.music.load(self.music_list[34])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="go little rockstar":
            pygame.init()
            pygame.mixer.music.load(self.music_list[35])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="bem":
            pygame.init()
            pygame.mixer.music.load(self.music_list[36])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="sarkoob":
            pygame.init()
            pygame.mixer.music.load(self.music_list[37])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="lal":
            pygame.init()
            pygame.mixer.music.load(self.music_list[38])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="the search":
            pygame.init()
            pygame.mixer.music.load(self.music_list[39])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="nothing new":
            pygame.init()
            pygame.mixer.music.load(self.music_list[40])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="khodafez":
            pygame.init()
            pygame.mixer.music.load(self.music_list[41])
            pygame.mixer.music.play()


        elif self.lineEdit.text()=="runaway":
            pygame.init()
            pygame.mixer.music.load(self.music_list[42])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="summer sadness":
            pygame.init()
            pygame.mixer.music.load(self.music_list[43])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="bewaasir":
            pygame.init()
            pygame.mixer.music.load(self.music_list[44])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="flower":
            pygame.init()
            pygame.mixer.music.load(self.music_list[45])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="MASCULINITY".lower():
            pygame.init()
            pygame.mixer.music.load(self.music_list[46])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="star shopping":
            pygame.init()
            pygame.mixer.music.load(self.music_list[47])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="vengeance":
            pygame.init()
            pygame.mixer.music.load(self.music_list[48])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="yadete":
            pygame.init()
            pygame.mixer.music.load(self.music_list[49])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="way down we go":
            pygame.init()
            pygame.mixer.music.load(self.music_list[50])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="naghabel":
            pygame.init()
            pygame.mixer.music.load(self.music_list[51])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="bad shodam":
            pygame.init()
            pygame.mixer.music.load(self.music_list[52])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="homage":
            pygame.init()
            pygame.mixer.music.load(self.music_list[53])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="koofeh":
            pygame.init()
            pygame.mixer.music.load(self.music_list[54])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="nabz":
            pygame.init()
            pygame.mixer.music.load(self.music_list[55])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="kaftar bazi":
            pygame.init()
            pygame.mixer.music.load(self.music_list[56])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="od":
            pygame.init()
            pygame.mixer.music.load(self.music_list[57])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="ghors2":
            pygame.init()
            pygame.mixer.music.load(self.music_list[58])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="slap":
            pygame.init()
            pygame.mixer.music.load(self.music_list[59])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="azhir":
            pygame.init()
            pygame.mixer.music.load(self.music_list[60])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="you broke my heart again":
            pygame.init()
            pygame.mixer.music.load(self.music_list[61])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="silk":
            pygame.init()
            pygame.mixer.music.load(self.music_list[62])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="llegal":
            pygame.init()
            pygame.mixer.music.load(self.music_list[63])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="when the party over":
            pygame.init()
            pygame.mixer.music.load(self.music_list[64])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="oon dare mire":
            pygame.init()
            pygame.mixer.music.load(self.music_list[65])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="romantic homicide":
            pygame.init()
            pygame.mixer.music.load(self.music_list[66])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="batman":
            pygame.init()
            pygame.mixer.music.load(self.music_list[67])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="inja irane":
            pygame.init()
            pygame.mixer.music.load(self.music_list[68])
            pygame.mixer.music.play()
        
        elif self.lineEdit.text()=="pesar":
            pygame.init()
            pygame.mixer.music.load(self.music_list[69])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="yeki dar mizane":
            pygame.init()
            pygame.mixer.music.load(self.music_list[70])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="5am":
            pygame.init()
            pygame.mixer.music.load(self.music_list[71])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="sogand":
            pygame.init()
            pygame.mixer.music.load(self.music_list[72])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="i like the way you kiss me":
            pygame.init()
            pygame.mixer.music.load(self.music_list[73])
            pygame.mixer.music.play()

        elif self.lineEdit.text()=="ghors2":
            pygame.init()
            pygame.mixer.music.load(self.music_list[73])
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