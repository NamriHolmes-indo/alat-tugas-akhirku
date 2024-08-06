import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem, QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QTimer, QDateTime

class MenuRiwayat(QWidget):
    buttonClicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        main_layout = QVBoxLayout()
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)
        main_layout.setAlignment(Qt.AlignCenter)
        
        icon_label_layout = QHBoxLayout()
        icon_label_layout.setSpacing(25)
        icon_label_layout.setAlignment(Qt.AlignCenter)

        icon_label = QLabel(self)
        icon_label.setPixmap(QIcon("./asset/icon.png").pixmap(75, 75))
        icon_label_layout.addWidget(icon_label)

        self.text_label = QLabel(f"Riwayat Pemeriksaaan", self)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.text_label.setStyleSheet("color: white;")
        self.text_label.setFont(QFont("Comic Sans MS", 36, QFont.Bold))
        icon_label_layout.addWidget(self.text_label)

        main_layout.addLayout(icon_label_layout)
        self.setLayout(main_layout)