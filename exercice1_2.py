from PySide2.QtWidgets import *
class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.layout = QVBoxLayout()

        self.button = QPushButton("salut")
        self.ligne=QLineEdit("testettest")

        self.layout.addWidget(self.button)
        self.layout.addWidget(self.ligne)

        self.setLayout(self.layout)




if __name__ == "__main__":
   app = QApplication([])
   win = Window()
   win.show()
   app.exec_()
