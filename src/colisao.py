from drone import Drone

class Colisao():
    def __init__(self,dro,qtde_drones,num_step):
        self.dro = dro
        self.qtde_drones = qtde_drones
        self.num_step = num_step
    """     
    def colisoes(dro,qtde_drones,num_step): 
        qde_colisoes = 0
        for k in range(qtde_drones-1):
            for i in range((k+1),qtde_drones):
                for j in range(num_step):
                    if(dro[k].x[j] == dro[i].x[j]):
                        if(dro[k].y[j] == dro[i].y[j]):
                            if(dro[k].z[j] == dro[i].z[j]):
                                qde_colisoes += 1
                                      
        return qde_colisoes
    """
    """ def colisoesPeloTempo(dro,qtde_drones,num_step):
        drones_envolvidos = 0
        qtde_colisoes = 0
        for step in range(num_step):
            for dr_atual in range(qtde_drones - 1):
                for dr_prox in range((dr_atual+1),qtde_drones):
                    if(dro[dr_atual].x[step] == dro[dr_prox].x[step] ):
                        if(dro[dr_atual].y[step] == dro[dr_prox].y[step]):
                            if(dro[dr_atual].z[step] == dro[dr_prox].z[step]):
                                drones_envolvidos += 1
            if(drones_envolvidos != 0):
                qtde_colisoes += 1
                drones_envolvidos = 0

        return qtde_colisoes """    

    def colisoesDro(self,dro,qtde_drones,ponto):
        vetorColisao = []
        drones_envolvidos = 0
        qtde_colisoes = 0

        for dro_atual in range(qtde_drones -1):
            for dro_prox in range((dro_atual+1),qtde_drones):
                if((dro[dro_atual].x[ponto] == dro[dro_prox].x[ponto]) and (dro[dro_atual].ativo == True) and (dro[dro_prox].ativo == True)):
                    if(dro[dro_atual].y[ponto] == dro[dro_prox].y[ponto]):
                        if(dro[dro_atual].z[ponto] == dro[dro_prox].z[ponto]):
                            drones_envolvidos += 1
                            #add na lista os drones envolvidos para futura retirada
                            if(vetorColisao.__contains__(dro_atual) == False):
                                vetorColisao.append(dro_atual)
                            if(vetorColisao.__contains__(dro_prox) == False):
                                vetorColisao.append(dro_prox)
        #vetorColisao.__len__
        #Depois de contado a qtde de drones envolvidos intrementa se a qtde de colosao
        if(drones_envolvidos != 0):
            qtde_colisoes += 1
            

        return qtde_colisoes,vetorColisao