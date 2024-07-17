# -*- coding: utf-8 -*-
import time
from pynput.mouse import Button, Controller, Listener

from PyQt5.QtWidgets import QApplication, QMessageBox, QDialog
import os
import sys

ABSOLUT_PATH = os.path.dirname(os.path.realpath(__file__))

from gui_docnix import Ui_Dialog

class FrontEnd(QDialog):
    def __init__(self):
        super(FrontEnd, self).__init__()
        #GUI - interface
        self.gui = Ui_Dialog()
        self.gui.setupUi(self)

        self.initUI()

    def initUI(self):
        self.x_docnix1 = 104
        self.y_docnix1 = 377
        self.x_docnix2 = 671
        self.y_docnix2 = 437
        self.var = ''

        self.gui.btn_iniciar.clicked.connect(self.run)

        self.mouse = Controller()
               
    def on_click(self, x, y, button, pressed):
        if button == Button.right and pressed:
            print("Botão direito do mouse clicado. Encerrando o programa.")
            self.var = 'fechar'
            return False
        
    def click(self, x, y):
        self.mouse.position = (x, y)
        self.mouse.click(Button.left, 1)

    def run(self):
        qtd = self.gui.ln_tentativas.text()
        if qtd:
            qtd = int(qtd)
            listener = Listener(on_click=self.on_click)
            listener.start()

            c = 0
            while c <= qtd and self.var != 'fechar':
                self.click(self.x_docnix1, self.y_docnix1)
                time.sleep(0.1)
                self.click(self.x_docnix2, self.y_docnix2)
                time.sleep(0.1)
                c += 1

            listener.stop()  # Parando o listener após o loop terminar
        else:
            QMessageBox.warning(self, 'Erro', 'Por favor, preencha a quantidade.')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    gui = FrontEnd()
    gui.show() 
    sys.exit(app.exec_())

        


