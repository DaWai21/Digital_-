import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt, QTime, QTimer
from PyQt5.QtGui import QFont, QFontDatabase
class Digital_Clock(QWidget):

    def __init__(self):
        super().__init__()

        self.time_label = QLabel(self)
        self.timer = QTimer(self)
        self.iniGui()
        self.update_time()

    def iniGui(self):
        self.setWindowTitle("Digital clcok")
        self.setGeometry(600, 300, 600,100)
        vbox = QVBoxLayout()
        vbox.addWidget(self.time_label)
        self.setLayout(vbox)
        self.time_label.setStyleSheet("font-size: 150px;"
                                      "color: red;")
        self.setStyleSheet('background: purple;')
        font_id = QFontDatabase.addApplicationFont("DS-DIGIT.TTF")
        fond_family = QFontDatabase.applicationFontFamilies(font_id)[0]
        my_font = QFont(fond_family, 150)
        self.time_label.setFont(my_font)

    def update_time(self):
        current_time = QTime.currentTime().toString("hh:mm:ss AP")
        self.time_label.setText(current_time)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

if __name__ == '__main__':

    app = QApplication(sys.argv)
    clock = Digital_Clock()
    clock.show()
    sys.exit(app.exec_())