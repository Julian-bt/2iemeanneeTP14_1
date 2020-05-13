from PySide2.QtWidgets import *
class Fenetre(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setWindowTitle("Avis DBD") #titre fenetre

        self.layout=QGridLayout() #ajouter sous forme de grille
        self.setLayout(self.layout)


        self.label = QLabel("Laisser un commentaire")
        self.texte=QTextEdit("")
        self.layout.addWidget(self.label)
        self.layout.addWidget(self.texte,1,0,2,2)

        liste=['Success','Cancel']
        compteur=0
        for a in liste:
            self.bouton=QPushButton(a)
            self.layout.addWidget(self.bouton,3,compteur)
            compteur+=1


        self.setLayout(self.layout)


if __name__ == "__main__":
   app = QApplication([])
   win = Fenetre()
   win.show()
   app.exec_()
