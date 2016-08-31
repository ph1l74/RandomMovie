# -*- coding: utf-8 -*-

import sys
import os
import csv
import random
import re
import mainwin
from PyQt4.QtGui import *
from PyQt4.QtCore import *

filmList = {"Number":[], "Title":[], "Year":[], "Director":[], "Rating":[], "Tags":[]}

App = QApplication(sys.argv)
MainWindow = QWidget()

UI = mainwin.Ui_RandomMovie()
UI.setupUi(MainWindow)
MainWindow.show()

QCoreApplication.processEvents()

def _translate(context, text, disambig):
        return QApplication.translate(context, text, disambig, QApplication.UnicodeUTF8)

def changeLabel (label, text):
    label.setText(_translate("RandomMovie", text, None))

def fileOpen():
    global filmList
    filename = QFileDialog.getOpenFileName()
    file = open(filename, 'rb')
    filmListDR = csv.DictReader(file, delimiter=',')
    filmNumber = 0
    for row in filmListDR:
        filmList["Number"].append(filmNumber)
        filmList["Title"].append(str(row['Title']))
        filmList["Year"].append(str(row['Year']))
        filmList["Rating"].append(str(row['IMDb Rating']))
        filmList["Tags"].append(str(row['Genres']))
        filmList["Director"].append(str(row['Directors']))
        #filmList["URL"].append(str(row['URL']))
        filmNumber += 1
    filmNumber -= 1
    changeLabel(UI.listStatus, 'Список успешно загружен')
    if filmNumber % 10 == 1:
        string = "фильм"
    elif filmNumber % 10 == 2 or filmNumber % 10 == 3 or filmNumber % 10 == 4:
        string = "фильма"
    else:
        string = "фильмов"
    changeLabel(UI.listCount, 'В вашем списке %d %s' % (filmNumber, string))

def getRandom():
    global filmList
    randomFilm = random.choice(filmList["Number"])
    print randomFilm
    #print(random.choice(filmList["Title"]))
    changeLabel(UI.filmInfoTitle, '%s' % str(filmList["Title"][randomFilm]))
    changeLabel(UI.filmInfoYear, '%s' % str(filmList["Year"][randomFilm]))
    changeLabel(UI.filmInfoRating, '%s' % str(filmList["Rating"][randomFilm]))
    changeLabel(UI.filmInfoTags, '%s' % str(filmList["Tags"][randomFilm]))
    changeLabel(UI.filmInfoDirector, '%s' % str(filmList["Director"][randomFilm]))

UI.btnLoad.clicked.connect(lambda : fileOpen())
UI.btnRandom.clicked.connect(lambda : getRandom())

sys.exit(App.exec_())