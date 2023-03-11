import sys
from ThemeController import ThemeController
from ThemeEnum import Theme
from PyQt5.QtCore import QSize, Qt
from PyQt5.QtWidgets import QCheckBox, QMenu, QAction, QVBoxLayout, QLineEdit, QLabel, QApplication, QMainWindow, QPushButton, QWidget
from pathlib import Path

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(QSize(400, 300))
        
        self.button = QPushButton("Light")
        self.button.clicked.connect(self.clickHandler)

        self.setCentralWidget(self.button)

    def clickHandler(self):
        if themeController.theme == Theme.Light:
            themeController.theme = Theme.Dark
            self.button.setText("Dark")
        else:
            themeController.theme = Theme.Light
            self.button.setText("Light")
        app.setStyleSheet(themeController.ApplyThemeToQSS(styleSheet))
        

def readTextFromFile(path: str):
    file = open(path, "rt")
    text = file.read()
    file.close()
    return text

app = QApplication(sys.argv)

styleSheet = readTextFromFile("./styles/mainStyle.qss")

themeController = ThemeController()
app.setStyleSheet(themeController.ApplyThemeToQSS(styleSheet))

window = MainWindow()
window.show()
app.exec()

