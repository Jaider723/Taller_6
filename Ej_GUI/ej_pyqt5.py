import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

# Ejemplo de una interfaz gráfica con PyQt5

class MiVentana(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Crear una etiqueta
        self.etiqueta = QLabel('Bienvenido a mi aplicación', self)

        # Crear un botón
        self.boton = QPushButton('Haz clic aquí', self)
        self.boton.clicked.connect(self.actualizar_etiqueta)

        # Crear un diseño vertical
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.etiqueta)
        self.layout.addWidget(self.boton)

        # Establecer el diseño de la ventana
        self.setLayout(self.layout)

        # Configurar la ventana
        self.setWindowTitle('Ejemplo de Interfaz Gráfica con PyQt')
        self.setGeometry(100, 100, 300, 150)

    def actualizar_etiqueta(self):
        self.etiqueta.setText('¡Hola, mundo!')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ventana = MiVentana()
    ventana.show()
    sys.exit(app.exec_())
