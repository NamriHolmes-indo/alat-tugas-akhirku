from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLabel, QSizePolicy, QSpacerItem
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt, QSize, pyqtSignal

class MenuController(QWidget):
    buttonClicked = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)

    def initUI(self, menu_type):
        self.current_menu_type = menu_type  # Simpan menu_type saat ini
        self.setWindowTitle(f'Menu {menu_type}')
        self.setStyleSheet("background-color: #010020;")

        self.clearLayout()

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

        self.text_label = QLabel(f"Pemeriksaan {self.current_menu_type}", self)
        self.text_label.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.text_label.setStyleSheet("color: white;")
        self.text_label.setFont(QFont("Comic Sans MS", 36, QFont.Bold))
        icon_label_layout.addWidget(self.text_label)

        main_layout.addLayout(icon_label_layout)

        spacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)
        main_layout.addSpacerItem(spacer)

        button_layout = QHBoxLayout()
        button_layout.setSpacing(50)
        button_layout.setAlignment(Qt.AlignCenter)

        button_names = ["Mulai Rekam", "Lihat Hasil", "History", "Kembali Home"]

        for name in button_names:
            icon_file = "./asset/" + name.replace(" ", "_") + ".png"
            button = QPushButton(self)
            button.setStyleSheet("background-color: #CDEDFF; max-width: 75%; max-height: 150px; border-radius: 10px;")
            button.setFixedSize(150, 150)

            button.setIcon(QIcon(icon_file))
            button.setIconSize(QSize(150, 150))
            button.setProperty('id', name)
            button.clicked.connect(lambda checked, name=name: self.buttonClickedHandler(name))  # Menghubungkan ke buttonClickedHandler

            button_layout.addWidget(button)

        main_layout.addLayout(button_layout)

        self.setLayout(main_layout)

    def clearLayout(self):
        if self.layout() is not None:
            for i in reversed(range(self.layout().count())):
                item = self.layout().itemAt(i)
                if isinstance(item, QWidget):
                    item.widget().deleteLater()
                elif isinstance(item, QSpacerItem):
                    pass  # Biarkan QSpacerItem tanpa dihapus
                else:
                    pass  # Penanganan kasus lain jika ada

    def setMenuType(self, menu_type):
        self.initUI(menu_type)

    def buttonClickedHandler(self, button_name):
        self.buttonClicked.emit(button_name)

        if button_name == "Mulai Rekam":
            print(f"Tombol {self.current_menu_type} Rekam diklik.")
        elif button_name == "Lihat Hasil":
            print(f"Tombol {self.current_menu_type} Hasil diklik.")
        elif button_name == "History":
            print(f"Tombol {self.current_menu_type} History diklik.")
        elif button_name == "Kembali Home":
            print(f"Tombol {self.current_menu_type} Home diklik.")
