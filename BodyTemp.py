import sys
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem, QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, pyqtSignal, QTimer, QDateTime

class BodyTemp(QWidget):
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

        self.text_label = QLabel(f"Pemeriksaan Suhu Tubuh", self)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.text_label.setStyleSheet("color: white;")
        self.text_label.setFont(QFont("Comic Sans MS", 36, QFont.Bold))
        icon_label_layout.addWidget(self.text_label)

        main_layout.addLayout(icon_label_layout)
        
        main_content_layout = QHBoxLayout()
        main_content_layout.setSpacing(25)
        main_content_layout.setAlignment(Qt.AlignCenter)

        time_date_back_layout = QVBoxLayout()
        time_date_back_layout.setSpacing(25)
        time_date_back_layout.setAlignment(Qt.AlignTop)
        
        self.time_label = QLabel(self)
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setStyleSheet("color: black; padding: 5px; background-color: #CDEDFF; border-radius: 10px;")
        self.time_label.setFont(QFont("Comic Sans MS", 24))
        time_date_back_layout.addWidget(self.time_label)

        self.date_label = QLabel(self)
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setStyleSheet("color: black; padding: 5px; background-color: #CDEDFF; border-radius: 10px;")
        self.date_label.setFont(QFont("Comic Sans MS", 24))
        time_date_back_layout.addWidget(self.date_label)

        back_button = QPushButton("Kembali", self)
        back_button.setStyleSheet("background-color: #CDEDFF; border-radius: 10px;")
        back_button.setFont(QFont("Comic Sans MS", 18))
        back_button.setIcon(QIcon("./asset/Back.png"))
        back_button.setIconSize(QSize(50, 50))
        
        back_button.clicked.connect(self.backButtonClicked)
        time_date_back_layout.addWidget(back_button)
        
        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)
        main_content_layout.addSpacerItem(spacer)
        
        main_content_layout.addLayout(time_date_back_layout)

        layout_right = QHBoxLayout()
        layout_right.setSpacing(25)
        layout_right.setAlignment(Qt.AlignCenter)
        
        layout_informasi = QVBoxLayout()
        layout_informasi.setSpacing(25)
        layout_informasi.setAlignment(Qt.AlignCenter)
        
        self.suhu = QLabel(self)
        self.suhu.setAlignment(Qt.AlignCenter)
        self.suhu.setStyleSheet("color: black; padding: 5px; background-color: #CDEDFF; border-radius: 10px;")
        self.suhu.setFont(QFont("Comic Sans MS", 24))
        self.suhu.setText("25")
        self.suhu.setFixedSize(150, 150)
        layout_informasi.addWidget(self.suhu)
        
        self.status = QLabel(self)
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setStyleSheet("color: black; padding: 5px; background-color: #CDEDFF; border-radius: 10px;")
        self.status.setFont(QFont("Comic Sans MS", 24))
        self.status.setText("Normal")
        self.status.setFixedSize(150, 150)
        layout_informasi.addWidget(self.status)
        
        layout_controller = QVBoxLayout()
        layout_controller.setSpacing(25)
        layout_controller.setAlignment(Qt.AlignCenter)
        
        button_names = ["start suhu", "stop suhu"]

        for name in button_names:
            icon_file = "./asset/" + name.replace(" ", "_") + ".png"
            button = QPushButton(self)
            button.setStyleSheet("background-color: #CDEDFF; max-width: 75%; max-height: 150px; border-radius: 10px;")
            button.setFixedSize(150, 150)

            button.setIcon(QIcon(icon_file))
            button.setIconSize(QSize(150, 150))
            button.setProperty('id', name)
            button.clicked.connect(self.buttonClickedHandler)

            layout_controller.addWidget(button)
        
        layout_right.addLayout(layout_informasi)
        layout_right.addLayout(layout_controller)
        
        main_content_layout.addLayout(layout_right)
        main_layout.addLayout(main_content_layout)
        
        self.setLayout(main_layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.updateDateTime)
        self.timer.start(1000)

        self.updateDateTime()

    def updateDateTime(self):
        current_time = QDateTime.currentDateTime()
        self.time_label.setText(current_time.toString("hh:mm:ss"))
        self.date_label.setText(current_time.toString("dddd, dd MMMM yyyy"))

    def backButtonClicked(self):
        self.buttonClicked.emit("Kembali Home")
        
    def buttonClickedHandler(self):
        sender = self.sender()
        self.buttonClicked.emit(sender.property('id'))

        if sender.property('id') == "start suhu":
            print(f"Tombol Rekam diklik.")
        elif sender.property('id') == "stop suhu":
            print(f"Tombol Berhenti diklik.")