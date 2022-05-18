from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

Form,Window= uic.loadUiType('main.ui')

app= QApplication([])

window= Window()
form= Form()
form.setupUipyuic5
(window)
window.show()
app.exec()