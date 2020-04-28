from drone import Drone
from random import uniform
from chaotic import Chaotic
from aleatory import Aleatory
from circle import Circle
from colisao import Colisao

import numpy as np
from random import randint

class Create(Drone):
    def __init__(self, num_steps):
        super().__init__(num_steps)

        
    def SetDrones(self,dro,qtde_chao,qtde_circ,qtde_alea,num_steps,qtde_dron):
        #par = randint(1, 4)
        #theta = np.linspace((-1*par) * np.pi, par * np.pi, num_steps)
        thetas = []
        zs = []
        vetorColisao = []
        incrementoColisao, qtde_colisao = 0,0
        qtdedrones = qtde_dron
        
        qtdeFinal = 0
        
        for ponto in range(num_steps):
            
            for i in range(qtde_chao): 
                if(ponto == 0):
                    dro[i].x[ponto], dro[i].y[ponto], dro[i].z[ponto] = uniform(0.0,25.0),uniform(0.0,25.0),uniform(0.0,25.0)
                    dro[i].tipo = 1
                else:
                    if(dro[i].ativo == True):
                        dro[i].x[ponto], dro[i].y[ponto],dro[i].z[ponto] =  Chaotic.lorenz2(num_steps,dro[i].x[ponto-1],dro[i].y[ponto-1],dro[i].z[ponto-1])

                #Tipo Caotico = 1
                

            for i in range(qtde_circ): 
                u = i + qtde_chao
                if(ponto == 0):
                    par = randint(1, 4)
                    thetas.append(np.linspace((-1*par) * np.pi, par * np.pi, num_steps))
                    zs.append(np.linspace(randint(0,4), randint(0,4), num_steps))
                    #zs.append(np.linspace(0,2, num_steps))
                    dro[u].x[ponto], dro[u].y[ponto], dro[u].z[ponto] = Circle.movCircle2(num_steps,thetas[i],zs[i],ponto)
                    dro[u].tipo = 2
                else:
                    if(dro[u].ativo == True):
                        dro[u].x[ponto], dro[u].y[ponto], dro[u].z[ponto] = Circle.movCircle2(num_steps,thetas[i],zs[i],ponto)
                
                #Tipo Circulo = 2
                
            for i in range(qtde_alea):     
                u = i + qtde_chao + qtde_circ
                if(ponto == 0):
                        par = randint(1, 4)
                        thetas.append(np.linspace((-1*par) * np.pi, par * np.pi, num_steps))
                        zs.append(np.linspace(randint(0,4), randint(0,4), num_steps))
                        #zs.append(np.linspace(0,2, num_steps))
                        dro[u].x[ponto], dro[u].y[ponto], dro[u].z[ponto] = Circle.movCircle2(num_steps,thetas[i],zs[i],ponto)
                        dro[u].tipo = 3
                #Tipo Aleatorio = 3
                else:
                    if(dro[u].ativo == True):
                        dro[u].x[ponto], dro[u].y[ponto], dro[u].z[ponto] = Circle.movCircle2(num_steps,thetas[i],zs[i],ponto)
        
            incrementoColisao,vetorColisao = Colisao.colisoesDro(self,dro,qtdedrones,ponto)
            qtde_colisao += incrementoColisao
            
            
                        

            for j in range(vetorColisao.__len__()):
                
                dro[vetorColisao[j]].ativo = False
        
        for j in range(qtde_dron):
            if(dro[j].ativo == True):
                qtdeFinal += 1
                        
        return dro,qtde_colisao,qtdeFinal

