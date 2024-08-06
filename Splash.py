import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QSizePolicy
from PyQt5.QtGui import QColor, QPalette, QPixmap
from PyQt5.QtCore import Qt

class Splash(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(1024, 600)
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('Home')
        self.setStyleSheet("background-color: #010020;")

        # Create the main layout with a vertical alignment
        self.main_layout = QVBoxLayout(self)
        self.main_layout.setContentsMargins(50, 50, 50, 50)
        self.main_layout.setSpacing(20)
        
        self.icon_label = QLabel(self)
        self.pixmap = QPixmap("./asset/IconLong.png")
        self.icon_label.setPixmap(self.pixmap)
        self.icon_label.setAlignment(Qt.AlignCenter)
        
        self.main_layout.addWidget(self.icon_label, alignment=Qt.AlignCenter)
        self.setLayout(self.main_layout)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        new_width = int(self.width() * 0.60)
        scaled_pixmap = self.pixmap.scaledToWidth(new_width, Qt.SmoothTransformation)
        self.icon_label.setPixmap(scaled_pixmap)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(1, 0, 32))
    app.setPalette(palette)
    ex = Splash()
    ex.show()
    sys.exit(app.exec_())
