from PySide2.QtWidgets import *
from PySide2.QtGui import *
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setFixedSize(400,300)
        self.setWindowTitle("IHM") #titre fenetre

        self.setWindowIcon(QIcon("FR.png"))

        self.layout=QVBoxLayout()

        self.label = QLabel("Hello World")
        self.label.setAlignment(Qt.AlignCenter)
        self.barre=QProgressBar()
        self.barre.setValue(50)
        self.ligne=QLineEdit()
        self.bouton=QPushButton("Click me!")
        self.bouton.setToolTip("Salut salut")


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.barre)
        self.layout.addWidget(self.ligne)
        self.layout.addWidget(self.bouton)


        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Fenetre()
   win.show()
   app.exec_()
