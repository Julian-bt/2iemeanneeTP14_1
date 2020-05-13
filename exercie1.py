from PySide2.QtWidgets import *
app = QApplication([])
mainWidget = QWidget()

layout = QVBoxLayout()


label = QLabel("Ceci est un QLabel")
button = QPushButton("Ceci est un QPushButton")
box=QComboBox()


layout.addWidget(label)
layout.addWidget(button)
layout.addWidget(box)


mainWidget.setLayout(layout)


mainWidget.show()
app.exec_()
