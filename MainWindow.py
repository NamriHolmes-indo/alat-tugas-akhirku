import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QStackedWidget
from MainMenu import MainMenu
from MenuController import MenuController
from BodyTemp import BodyTemp
from MenuRiwayat import MenuRiwayat

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Main Window')
        self.setGeometry(100, 100, 1024, 600)
        self.setStyleSheet("background-color: #010020;")
        
        self.stacked_widget = QStackedWidget(self)
        self.setCentralWidget(self.stacked_widget)

        self.main_menu = MainMenu()
        self.menu_controller = MenuController()
        self.suhu_tubuh = BodyTemp()
        self.riwayat = MenuRiwayat()

        self.stacked_widget.addWidget(self.main_menu)
        self.stacked_widget.addWidget(self.menu_controller)
        self.stacked_widget.addWidget(self.suhu_tubuh)        
        self.stacked_widget.addWidget(self.riwayat)
        
        self.main_menu.buttonClicked.connect(self.handleMenuSelection)
        self.menu_controller.buttonClicked.connect(self.handleMenuSelection)
        self.suhu_tubuh.buttonClicked.connect(self.handleMenuSelection)
        self.riwayat.buttonClicked.connect(self.handleMenuSelection)

    def handleMenuSelection(self, menu_type):
        if menu_type == "ECG" or menu_type == "EEG":
            self.stacked_widget.setCurrentWidget(self.menu_controller)
            self.menu_controller.setMenuType(menu_type)        
        elif menu_type == "Suhu Tubuh":            
            self.stacked_widget.setCurrentWidget(self.suhu_tubuh)
        elif menu_type == "Riwayat":            
            self.stacked_widget.setCurrentWidget(self.riwayat)
        elif menu_type == "Kembali Home":
            self.stacked_widget.setCurrentWidget(self.main_menu)
        else:
            print(f"Pesan dari MainWindow Tombol {menu_type} diklik.")

def main():
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
