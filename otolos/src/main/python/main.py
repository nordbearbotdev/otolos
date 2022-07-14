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
        
        # Кнопки
        navtb = QToolBar("Навигация")
        navtb.setIconSize(QSize(18,18))
        navtb.setAllowedAreas(Qt.TopToolBarArea)
        navtb.setFloatable(False)
        navtb.setMovable(False)
        self.addToolBar(navtb)
        
         back_btn = QAction(QIcon(os.path.join('data/images', 'arrow-180.png')), "Back", self)
        back_btn.setStatusTip("Вернутся на предыдущую страницу")
        back_btn.triggered.connect(lambda: self.tabs.currentWidget().back())
        navtb.addAction(back_btn)

        next_btn = QAction(QIcon(os.path.join('data/images', 'arrow-000.png')), "Forward", self)
        next_btn.setStatusTip("Перейти на следующую страницу")
        next_btn.triggered.connect(lambda: self.tabs.currentWidget().forward())
        navtb.addAction(next_btn)

        reload_btn = QAction(QIcon(os.path.join('data/images', 'arrow-circle-315.png')), "reload", self)
        reload_btn.setStatusTip("Перезагрузить страницу")
        reload_btn.triggered.connect(lambda: self.tabs.currentWidget().reload())
        navtb.addAction(reload_btn)

         stop_btn = QAction(QIcon(os.path.join('data/images', 'cross-circle.png')), "Stop", self)
        stop_btn.setStatusTip("Остановить загрузку страницы")
        stop_btn.triggered.connect(lambda: self.tabs.currentWidget().stop())
        navtb.addAction(stop_btn)

        navtb.addSeparator()
        
        self.httpsicon = QLabel()
        self.httpsicon.setPixmap(QPixmap(os.path.join('data/images', 'lock-nossl.png')))
        navtb.addWidget(self.httpsicon)
        
        self.urlbar = QLineEdit()
        self.urlbar.returnPressed.connect(self.navigate_to_url)
        navtb.addWidget(self.urlbar)
