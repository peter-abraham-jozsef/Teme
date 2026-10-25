import random

def calculeaza_cost(graf:dict,drum:list,stop:int)->int:
    if drum[-1] != stop:
        return 1000000
    for i in range(len(drum)-1):
        nod_curent=drum[i]
        nod_urmator=drum[i+1]
        if nod_urmator in graf[nod_curent]:
            cost_total+=graf[nod_curent][nod_urmator]
        else:
            return 1000000
    return cost_total
def genereaza_individ(graf:dict,start:int,stop:int)->list:
    path:list=[start]
    curent:int=start
    vizitat={start}
    while curent!= stop:
        vecini_nevizitati = []
        for vecin in graf[curent]:
            if vecin not in vizitat:
                vecini_nevizitati.append(vecin)
        if not vecini_nevizitati:
            break
        urmatorul=random.choice(vecini_nevizitati)
        
        path.append(urmatorul)
        vizitat.add(urmatorul)
        curent=urmatorul
        
    return path
def genereaza_populatie(start:int,graf:dict,stop:int,N:int)->list:
    genereaza_individ:list=[]
    for i in range(N):
        genereaza_individ.append(genereaza_individ(start,graf,stop))
    return  genereaza_individ    
        
        

if __name__=='main':
    pass