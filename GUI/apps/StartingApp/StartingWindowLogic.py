from PyQt5 import QtWidgets
from PyQt5.QtWidgets import (QWidget, QToolTip, QPushButton, QApplication)

from .StartingWindow import *
from ..StatisticsApp.StatisticsApp import StatisticsApp

# UI_main rename
class StartingWindowLogic(Ui_MainWindow, QtWidgets.QMainWindow):
    def __init__(self):
        self.settings = {}

        super().__init__()
        self.setupUi(self)
        self.__build_buttons()

    def __build_buttons(self):
        # self.push_stats_button...

        # create button and add signal
        self.pushButton.clicked.connect(self.button_stats)
        self.pushButton_2.clicked.connect(self.button_prediction)
        self.pushButton_3.clicked.connect(self.button_bioeq)
        self.pushButton_4.clicked.connect(self.done)
        
        self.commandLinkButton.clicked.connect(self.path_to_file)

    def done(self):
        self.close()

    def button_stats(self):
        self.settings['MODULE'] = 'STATISTICS'
        self.hide()
        app = StatisticsApp()
        app.start()

        # update settings
        return app.settings

    def button_prediction(self):
        self.settings['MODULE'] = 'PREDICTION'
        
    def button_bioeq(self):
        self.settings['MODULE'] = 'BIOEQ'

    def path_to_file(self):
        self.settings['data'] = {'preprocessing': {
                                               'AUTO': False,
                                               'fillna': 'mean',
                                               'encoding': 'label_encoding',
                                               'scaling': False
                                              },
                                'path': ''
                                }
        self.settings['data']['path'] = QtWidgets.QFileDialog.getOpenFileName()[0]