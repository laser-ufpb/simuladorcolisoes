import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from drone import Drone
from create_drones import Create
from plot import Plot
from colisao import Colisao

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Simulador Drones'
        self.left = 470
        self.top = 50
        self.width = 400
        self.height = 300
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.table_widget = MyTableWidget(self)
        self.setCentralWidget(self.table_widget)
        
        self.show()
      
class MyTableWidget(QWidget):
    
    def __init__(self, parent):
        super(QWidget, self).__init__(parent)
        self.layout = QVBoxLayout(self)
        
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tabs.resize(300,200)
        
        # Add tabs
        self.tabs.addTab(self.tab1,"Dados da Simulação")
        self.tabs.addTab(self.tab2,"Resultados")

        # Create first tab
        self.tab1UI()

        # Create second tab
        self.tab2UI()

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)
    
    def tab1UI(self):
        self.sp1,self.sp2,self.sp3,self.sp4 = QSpinBox(),QSpinBox(),QSpinBox(),QSpinBox()    
        self.sp1.setMaximum(100000),self.sp2.setMaximum(1000),self.sp3.setMaximum(1000),self.sp4.setMaximum(1000) 
        layout = QFormLayout()
        layout.addRow(QLabel("Quantidade de Passos:"), self.sp1)
        layout.addRow(QLabel("Quantidade Caótico:"), self.sp2)
        layout.addRow(QLabel("Quantidade Aleatório:"), self.sp3)
        layout.addRow(QLabel("Quantidade Circulos:"), self.sp4)
        self.tab1.layout = layout
        button = QPushButton('Simular', self)
        self.tab1.layout.addWidget(button)
        self.tab1.setLayout(self.tab1.layout)
        button.clicked.connect(self.click_button)

    def tab2UI(self):
        layout = QVBoxLayout()
        self.l1 = QLabel("Quantidade de Colisões:")
        self.l1.setAlignment(Qt.AlignAbsolute)
        layout.addWidget(self.l1)
        self.tab2.layout = layout
        self.tab2.setLayout(self.tab2.layout)
    
    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
  
    def click_button(self):
        
        num_steps,qtde_chao,qtde_alea,qtde_circ = self.sp1.value(),self.sp2.value(),self.sp3.value(),self.sp4.value()
        qtde_dron = qtde_chao + qtde_alea + qtde_circ
        #Criando array de objetos drones
        dro = []
        for i in range(qtde_dron):
            dro.append(Drone(num_steps))
        #Setando os drones p/ cada tipo de movimento
        dro,colisoes,droneFinais = Create.SetDrones(self,dro,qtde_chao,qtde_circ,qtde_alea,num_steps,qtde_dron)
        # Plotando os resultados das trajetorias
        #colisoes = Colisao.colisoes(dro,qtde_dron,num_steps)
        #colisoes = Colisao.colisoesPeloTempo(dro,qtde_dron,num_steps)
        self.l1.setText("Quantidade de Colisões:  "+str(colisoes)+ 
                        "\nQuantidade de drones restantes:  "+str(droneFinais)
                        )

        Plot(dro,droneFinais)
