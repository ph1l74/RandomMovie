# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwin.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_RandomMovie(object):
    def setupUi(self, RandomMovie):
        RandomMovie.setObjectName(_fromUtf8("RandomMovie"))
        RandomMovie.resize(390, 270)
        self.btnLoad = QtGui.QPushButton(RandomMovie)
        self.btnLoad.setGeometry(QtCore.QRect(130, 50, 131, 41))
        self.btnLoad.setObjectName(_fromUtf8("btnLoad"))
        self.listStatus = QtGui.QLabel(RandomMovie)
        self.listStatus.setGeometry(QtCore.QRect(10, 10, 371, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.listStatus.setFont(font)
        self.listStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.listStatus.setObjectName(_fromUtf8("listStatus"))
        self.listCount = QtGui.QLabel(RandomMovie)
        self.listCount.setGeometry(QtCore.QRect(10, 100, 371, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.listCount.setFont(font)
        self.listCount.setAlignment(QtCore.Qt.AlignCenter)
        self.listCount.setObjectName(_fromUtf8("listCount"))
        self.btnRandom = QtGui.QPushButton(RandomMovie)
        self.btnRandom.setGeometry(QtCore.QRect(130, 140, 131, 41))
        self.btnRandom.setObjectName(_fromUtf8("btnRandom"))
        self.frame = QtGui.QFrame(RandomMovie)
        self.frame.setGeometry(QtCore.QRect(10, 200, 371, 65))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.filmInfoTitle = QtGui.QLabel(self.frame)
        self.filmInfoTitle.setGeometry(QtCore.QRect(0, 0, 371, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.filmInfoTitle.setFont(font)
        self.filmInfoTitle.setText(_fromUtf8(""))
        self.filmInfoTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.filmInfoTitle.setObjectName(_fromUtf8("filmInfoTitle"))
        self.filmInfoYear = QtGui.QLabel(self.frame)
        self.filmInfoYear.setGeometry(QtCore.QRect(0, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.filmInfoYear.setFont(font)
        self.filmInfoYear.setText(_fromUtf8(""))
        self.filmInfoYear.setAlignment(QtCore.Qt.AlignCenter)
        self.filmInfoYear.setObjectName(_fromUtf8("filmInfoYear"))
        self.filmInfoRating = QtGui.QLabel(self.frame)
        self.filmInfoRating.setGeometry(QtCore.QRect(190, 20, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.filmInfoRating.setFont(font)
        self.filmInfoRating.setText(_fromUtf8(""))
        self.filmInfoRating.setAlignment(QtCore.Qt.AlignCenter)
        self.filmInfoRating.setObjectName(_fromUtf8("filmInfoRating"))
        self.filmInfoDirector = QtGui.QLabel(self.frame)
        self.filmInfoDirector.setGeometry(QtCore.QRect(0, 40, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.filmInfoDirector.setFont(font)
        self.filmInfoDirector.setText(_fromUtf8(""))
        self.filmInfoDirector.setAlignment(QtCore.Qt.AlignCenter)
        self.filmInfoDirector.setObjectName(_fromUtf8("filmInfoDirector"))
        self.filmInfoTags = QtGui.QLabel(self.frame)
        self.filmInfoTags.setGeometry(QtCore.QRect(190, 40, 181, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Tahoma"))
        font.setPointSize(11)
        self.filmInfoTags.setFont(font)
        self.filmInfoTags.setText(_fromUtf8(""))
        self.filmInfoTags.setAlignment(QtCore.Qt.AlignCenter)
        self.filmInfoTags.setObjectName(_fromUtf8("filmInfoTags"))

        self.retranslateUi(RandomMovie)
        QtCore.QMetaObject.connectSlotsByName(RandomMovie)

    def retranslateUi(self, RandomMovie):
        RandomMovie.setWindowTitle(_translate("RandomMovie", "RandomMovie", None))
        self.btnLoad.setText(_translate("RandomMovie", "Загрузить список", None))
        self.listStatus.setText(_translate("RandomMovie", "Список не загружен", None))
        self.listCount.setText(_translate("RandomMovie", "", None))
        self.btnRandom.setText(_translate("RandomMovie", "Выбрать случайный", None))

