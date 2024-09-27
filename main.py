import sys
from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QPushButton, QLabel, QMessageBox, QComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class Conjuntos(QWidget):
    def __init__(self):
        super().__init__()
        self.aplication()
        
    def aplication(self):
        self.setGeometry(300, 300, 400, 500)
        self.setWindowTitle("Conjuntos")
        self.content()
        self.show()
        
    def content(self):
        label_conjunto1 = QLabel(self)
        label_conjunto1.setText("Conjunto 1")
        label_conjunto1.setFont(QFont("Comic Sans MS", 11))
        label_conjunto1.move(55, 40)
        
        self.input_conjunto1 = QLineEdit(self)
        self.input_conjunto1.setPlaceholderText("Ej: 1,2,3,4,5,6,7,8,9")
        self.input_conjunto1.resize(300, 35)
        self.input_conjunto1.move(50, 65)
        self.input_conjunto1.setFont(QFont("Comic Sans MS", 11))
        
        label_conjunto2 = QLabel(self)
        label_conjunto2.setText("Conjunto 2")
        label_conjunto2.setFont(QFont("Comic Sans MS", 11))
        label_conjunto2.move(55, 120)
        
        self.input_conjunto2 = QLineEdit(self)
        self.input_conjunto2.setPlaceholderText("Ej: a,b,c,d,e,f,g,h,i")
        self.input_conjunto2.resize(300, 35)
        self.input_conjunto2.move(55, 145)
        self.input_conjunto2.setFont(QFont("Comic Sans MS", 11))
    
        label_operacion = QLabel(self)
        label_operacion.setText("Operación")
        label_operacion.setFont(QFont("Comic Sans MS", 11))
        label_operacion.move(55, 195)
        
        self.combo_operacion = QComboBox(self)
        self.combo_operacion.addItems([
            "1. Unión",
            "2. Intersección",
            "3. Diferencia",
            "4. Diferencia simétrica",
            "5. Pertenencia"
        ])
        self.combo_operacion.resize(300, 35)
        self.combo_operacion.move(50, 220)
        self.combo_operacion.setFont(QFont("Comic Sans MS", 11))
        
        calculo_button = QPushButton(self)
        calculo_button.setText("Calcular")
        calculo_button.resize(140, 40)
        calculo_button.move(130, 300)
        calculo_button.setFont(QFont("Segoe UI", 11))
        calculo_button.clicked.connect(self.Calcular)
        calculo_button.setStyleSheet("""
            QPushButton {
                background-color: #3c3c3c;    
                border-radius: 15px;          
                color: white;                 
                font-size: 16px;              
                padding: 5px;     
                border-bottom: 0.5px solid #727272;  
            }
            QPushButton:hover {
                background-color: #424242;   
            }
            QPushButton:pressed {
                background-color: #4E4E4E; 
                color: #979696;   
            }
        """)
        
        self.result = QLabel(self)
        self.result.setFixedSize(400, 50)
        self.result.setFont(QFont("Comic Sans MS", 11))
        self.result.move(0, 350)
        self.result.setStyleSheet("color:#17ff00")
        self.result.setAlignment(Qt.AlignmentFlag.AlignCenter)
        
        
    def Calcular(self):
        conjunto_1 = self.input_conjunto1.text()
        conjunto_2 = self.input_conjunto2.text()
        operador = self.combo_operacion.currentText() 
        
        elementos = conjunto_1.split(",")
        conjunto1 = set()
        for i in elementos:
            conjunto1.add(i.strip())  
        
        elementos_2 = conjunto_2.split(",")
        conjunto2 = set()
        for i in elementos_2:
            conjunto2.add(i.strip())
        
        if not conjunto_1 or not conjunto_2:
            QMessageBox.information(self, "Error", "Los campos no pueden estar vacíos", QMessageBox.StandardButton.Ok)
            return
        
        if "Unión" in operador:
            op = conjunto1 | conjunto2
            resultado_sin_comillas = "{ " + ", ".join(op) + " }"
            self.result.setText(f"El resultado de la unión es: {resultado_sin_comillas}")
        
        elif "Intersección" in operador:
            op = conjunto1 & conjunto2
            resultado_sin_comillas = "{ " + ", ".join(op) + " }"
            self.result.setText(f"El resultado de la intersección es: {resultado_sin_comillas}")
        
        elif "Diferencia" in operador:
            op = conjunto1 - conjunto2
            resultado_sin_comillas = "{ " + ", ".join(op) + " }"
            self.result.setText(f"El resultado de la diferencia es: {resultado_sin_comillas}")
        
        elif "Diferencia simétrica" in operador:
            op = conjunto1 ^ conjunto2
            resultado_sin_comillas = "{ " + ", ".join(op) + " }"
            self.result.setText(f"El resultado de la diferencia simétrica es: {resultado_sin_comillas}")
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Conjuntos()
    sys.exit(app.exec())