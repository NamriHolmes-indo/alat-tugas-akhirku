import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QGridLayout, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, pyqtSignal

class MainMenu(QWidget):
    buttonClicked = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Home')
        self.setStyleSheet("background-color: #010020;")

        main_layout = QVBoxLayout(self)
        main_layout.setContentsMargins(50, 50, 50, 50)
        main_layout.setSpacing(20)

        center_layout = QVBoxLayout()
        center_layout.setSpacing(75)
        center_layout.setAlignment(Qt.AlignCenter)

        header_layout = QVBoxLayout()
        header_layout.setSpacing(5)
        
        welcome_label = QLabel("Selamat Datang", self)
        welcome_label.setAlignment(Qt.AlignCenter)
        welcome_label.setStyleSheet("color: white;")
        welcome_label.setFont(QFont("Comic Sans MS", 42, QFont.Bold))
        
        menu_label = QLabel("Menu Utama", self)
        menu_label.setAlignment(Qt.AlignCenter)
        menu_label.setStyleSheet("color: white;")
        menu_label.setFont(QFont("Comic Sans MS", 18))

        header_layout.addWidget(welcome_label)
        header_layout.addWidget(menu_label)

        button_container = QWidget(self)
        button_container.setStyleSheet("background-color: transparent;")
        button_container_layout = QGridLayout(button_container)
        button_container_layout.setContentsMargins(0, 0, 0, 0)
        button_container_layout.setSpacing(20)
        button_container_layout.setAlignment(Qt.AlignCenter)

        button_names = ["ECG", "EEG", "Suhu Tubuh", "Cek Kondisi", "Riwayat", "Matikan Alat"]
        for index, name in enumerate(button_names):
            icon_file = "./asset/" + name.replace(" ", "_") + ".png"
            button = QPushButton(self)
            button.setStyleSheet("background-color: #CDEDFF; max-width: 75%; max-height: 150px; border-radius: 10px;")
            button.setFixedSize(150, 150)
            
            button.setIcon(QIcon(icon_file))
            button.setIconSize(QSize(150, 150))

            row = index // 3
            col = index % 3
            button_container_layout.addWidget(button, row, col)
            button.clicked.connect(self.buttonClickedHandler)
            button.setProperty('id', name)

            if name == "Matikan Alat":
                button.setProperty('id', 'matikan_alat_button')
                button.setStyleSheet("background-color: red; max-width: 75%; max-height: 150px; border-radius: 10px;")

        center_layout.addLayout(header_layout)
        center_layout.addWidget(button_container)

        main_layout.addLayout(center_layout)
        self.setLayout(main_layout)

    def buttonClickedHandler(self):
        sender = self.sender()
        self.buttonClicked.emit(sender.property('id'))

        if sender.property('id') == "ECG":
            print("Tombol ECG diklik.")
        elif sender.property('id') == "EEG":
            print("Tombol EEG diklik.")
        elif sender.property('id') == "Suhu Tubuh":
            print("Tombol Suhu Tubuh diklik.")
        elif sender.property('id') == "Cek Kondisi":
            print("Tombol Cek Kondisi diklik.")
        elif sender.property('id') == "Riwayat":
            print("Tombol Riwayat diklik.")
        elif sender.property('id') == 'matikan_alat_button':
            print('Tombol "Matikan Alat" diklik.')
            sender.setStyleSheet("background-color: red; max-width: 75%; max-height: 150px; border-radius: 10px;")
