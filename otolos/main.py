# Imports - Импорты
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5QtGui import *

import os
import sys

# Создаем класс с всеми функциями браузера Otolos и его GUI
class MainWindow(MainWindows)
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
      
        # В переменной Otolos хранится окно браузера
        self.otolos = QWebEngineView()
        self.otolos.setUrl(QUrl("здесь URL сайта разработчика")) # Здесь окно по-умолчанию
        
        self.otolos.urlChanged.connect(self.update_urlbar)
        self.otolos.loadFinished.connect(self.update_title)
        self.sentCentralWidget(self.otolos)
        
        self.status = QStatusBar()
