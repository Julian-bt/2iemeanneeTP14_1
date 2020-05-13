from PySide2.QtWidgets import *
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Avis DBD") #titre fenetre

        self.layout=QGridLayout() #ajouter sous forme de grille

        self.label = QLabel("Laisser un commentaire")

        self.texte=QTextEdit("")

        self.bouton1=QPushButton("Success")
        self.bouton2=QPushButton("Cancel")


        self.layout.addWidget(self.label)
        self.layout.addWidget(self.texte)
        self.layout.addWidget(self.bouton1)
        self.layout.addWidget(self.bouton2)

        self.setLayout(self.layout)

if __name__ == "__main__":
   app = QApplication([])
   win = Fenetre()
   win.show()
   app.exec_()
