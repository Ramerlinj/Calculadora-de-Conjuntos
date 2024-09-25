import sys
from PyQt6.QtWidgets import QWidget,QApplication,QLineEdit,QPushButton,QLabel
from PyQt6.QtGui import QFont

class Conjuntos(QWidget):
    def __init__(self):
        super().__init__()
        self.aplication()
        
    def aplication(self):
        self.setGeometry(200,200,400,400)
        self.setWindowTitle("Conjuntos")
        self.content()
        self.show()
        
    def content(self):
        label_conjunto1 = QLabel(self)
        label_conjunto1.setText("Conjunto 1")
        label_conjunto1.setFont(QFont("Comic Sans MS",11))
        label_conjunto1.move(55,40)
        
        self.input_conjunto1=QLineEdit(self)
        self.input_conjunto1.setPlaceholderText("Ej: 1,2,3,4,5,6,7,8,9")
        self.input_conjunto1.resize(300,35)
        self.input_conjunto1.move(50,65)
        self.input_conjunto1.setFont(QFont("Comic Sans MS", 11))
        
        label_conjunto2 = QLabel(self)
        label_conjunto2.setText("conjunto 2")
        label_conjunto2.setFont(QFont("Comic Sans MS",11))
        label_conjunto2.move(55,120)
        
        self.input_conjunto2=QLineEdit(self)
        self.input_conjunto2.setPlaceholderText("Ej: a,b,c,d,e,f,g,h,i")
        self.input_conjunto2.resize(300,35)
        self.input_conjunto2.move(55,145)
        self.input_conjunto2.setFont(QFont("Comic Sans MS", 11))
        
        calculo_button = QPushButton(self)
        calculo_button.setText("Calcular")
        calculo_button.resize(140,40)
        calculo_button.move(130,300)
        calculo_button.setFont(QFont("Segoe UI",11))
        calculo_button.clicked.connect(self.Calcular)
        calculo_button.setStyleSheet("""
                QPushButton {
                background-color: #3c3c3c;    
                border-radius: 15px;          
                color: white;                 
                font-size: 16px;              
                padding:5px;     
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
        label_conjunto1 = QLabel(self)
        label_conjunto1.setText("Operacion")
        label_conjunto1.setFont(QFont("Comic Sans MS",11))
        label_conjunto1.move(55,195)
        
        self.input_conjunto1=QLineEdit(self)
        self.input_conjunto1.setPlaceholderText("Ej: Solo ingrese el numero de la operacion")
        self.input_conjunto1.resize(300,35)
        self.input_conjunto1.move(50,220)
        self.input_conjunto1.setFont(QFont("Comic Sans MS", 11))
        
        label_conjunto2 = QLabel(self)
        label_conjunto2.setText("""
        1.Union
        2.Interseccion 
        3.Diferencia
        4.Diferencia simétrica
        5.pertenencia""")
        label_conjunto2.setFont(QFont("Comic Sans MS",9))
        label_conjunto2.move(-25,270)
        
        
    def Calcular(self):
        pass
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Conjuntos()
    sys.exit(app.exec())