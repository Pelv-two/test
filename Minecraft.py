import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QUrl, Qt

class WebBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Minecraft")
        self.resize(1800, 900)  # установка ширины и высоты окна
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://x.mess.eu.org/eris/"))
        self.setMouseTracking(True)  # включаем отслеживание мыши
        self.setCentralWidget(self.browser)

if __name__ == '__main__':
    __all__ = []
    app = QApplication(sys.argv)
    browser = WebBrowser()
    browser.show()
    sys.exit(app.exec_())
