from copy import deepcopy
import random

def permutaciones(arr):
    if len(arr)==0: return [[]]
    perm=[]
    for i in range(len(arr)):
        wot=permutaciones(arr[:i]+arr[i+1:])
        for w in wot:
            perm.append([arr[i]]+w)
    return perm

class grafo:
    def __init__(self):
        self.V =set() #un conjunto
        self.E = dict() #un mapeo de pesos a aritstas
        self.vecinos = dict() #un mapeo
        
    def agrega(self, v ):
        self.V.add(v)
        if not  v in self.vecinos: # vecindad de v
            self.vecinos[v]= set() #inicialmente no tiene nada
    def conecta(self, v , u , peso = 1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v,u)] = self.E[(u,v)] = peso
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
        
    def complemento(self):
        comp= grafo()
        for v in self.V:
            for w in self.V:
                if v != w  and (v,w) not in self.E:
                    comp.conecta(v,w,1)
        return comp
    
    def aristas(self):
        return self.E
    
    def vertices(self):
        return self.V
    
    def __str__(self):
        return "Aristas= " + str(self.E)+"\nVertices = " +str(self.V)
    
    def BFS_n(self, bi):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=fila()      ##fila con los nodos por visitar          
        Xvisitar.meter( bi )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados

    def DFS_n(self, bi):
        visitados=[]          ##arreglo con nodos visitados inicialmente vacio
        Xvisitar=pila()      ##fila con los nodos por visitar          
        Xvisitar.meter( bi )
        while Xvisitar.longitud > 0: ##mientras haya alguien en fila
            nodo = Xvisitar.obtener()
            if nodo not in visitados:  ##si el nodo aun no en visitado
                visitados.append(nodo)
                for vecino in self.vecinos[nodo]:
                    Xvisitar.meter(vecino)
        return visitados

    def kruskal(self):
        e = deepcopy(self.E)
        arbol = grafo()
        peso = 0
        comp = dict()
        t = sorted(e.keys(), key = lambda k: e[k], reverse=True)
        nuevo = set()
        while len(t) > 0 and len(nuevo) < len(self.V):
            #print(len(t)) 
            arista = t.pop()
            w = e[arista]    
            del e[arista]
            (u,v) = arista
            c = comp.get(v, {v})
            if u not in c:
                #print('u ',u, 'v ',v ,'c ', c)
                arbol.conecta(u,v,w)
                peso += w
                nuevo = c.union(comp.get(u,{u}))
                for i in nuevo:
                    comp[i]= nuevo
        print('MST con peso', peso, ':', nuevo, '\n', arbol.E)
        return arbol


    def DFS(self,bi):
        visitados =[]
        f=pila()
        f.meter(bi)
        while(f.longitud>0):
            na = f.obtener()
            visitados.append(na)
            ln = self.vecinos[na]
            for nodo in ln:
                if nodo not in visitados:
                    f.meter(nodo)
        return visitados
    
    def vecinoMasCercano(self):
        lv = list(self.V)   ##lista de vertices
        random.shuffle(lv)
        ni = lv.pop()
        inicial = ni
        lv2=list()
        lv2.append(ni)
        peso=0
        while len(lv2)<len(self.V):
            le = list()
            ln=list()
            ln = self.vecinos[ni]
            for nv in ln:
                if nv not in lv2:
                    le.append((nv,self.E[(ni,nv)]))
            sorted(le, key = lambda le: le[1] )
            t=le[0]
            lv2.append(t[0])
            peso=peso+t[1]
            ni=t[0]
        peso=peso+self.E[lv2[-1], inicial]
        lv2.append(inicial)
        return (lv2,peso)
    

    def Problem(self):
        perm=permutaciones(list(self.V))
        mejor=-1
        camino=[]
        for w in perm:
            peso=0
            for i in range(len(w)-1):
                peso+=self.E[(w[i],w[i+1])]
            peso+=self.E[(w[-1],w[0])]
            if peso<mejor or mejor==-1:
                mejor=peso
                camino=w
        return camino

    
def BFS_N(g, ni):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=fila()
    Xvisitar.meter(  (ni,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados

def DFS_N(g, bi):
    visitados= dict()    ##dicionario con llaves igual a nodos y valores igual a distancia de nodo inicial
    Xvisitar=pila()
    Xvisitar.meter(  (bi,0)   )   
    while Xvisitar.longitud > 0: ##mientras haya alguien en fila
        nodo = Xvisitar.obtener()
        if nodo[0] not in visitados:
            visitados[nodo[0]]=nodo[1]
            for vecino in g.vecinos[nodo[0]]:
                #vecinos_d.append( (e,nodo[1]+1) )
                Xvisitar.meter((vecino,nodo[1]+1))
            #for v in vecinos_d:
                #f.meter(v)
    return visitados


class pila(object):##quitas el mas nuevo STACK
    def __init__(self):
        self.a=[]
    
    def obtener(self):
        return self.a.pop()
    
    def meter(self, e):
        self.a.append(e)
        
    @property
    def longitud(self):
        return len(self.a)
    
    def __str__(self):
        return "<" + str(self.a)+ ">"
    
    



class fila(pila):##quitas el que ha estado mas tiempo 
    def obtener(self):
        return self.a.pop(0)
    


#Introducir los datos en el grafo
g=grafo()
g.conecta("Santa Lucia","Macroplaza",0.55)
g.conecta("Santa Lucia","Barrio Antiguo",0.48)
g.conecta("Santa Lucia","Estadio BBVA",6.4)
g.conecta("Santa Lucia","La Purisima",2.24)
g.conecta("Santa Lucia","Ciudad Universitaria",6.26)
g.conecta("Santa Lucia","Arena Monterrey",1.96)
g.conecta("Santa Lucia","Obelisco",6.4)
g.conecta("Santa Lucia","Fundidora",2.24)
g.conecta("Santa Lucia","Obispado",6.26)

g.conecta("Macroplaza","Santa Lucia",0.55)
g.conecta("Macroplaza","Barrio Antiguo",0.38)
g.conecta("Macroplaza","Estadio BBVA",6.56)
g.conecta("Macroplaza","La Purisima",1.64)
g.conecta("Macroplaza","Ciudad Universitaria",6.36)
g.conecta("Macroplaza","Arena Monterrey",2.49)
g.conecta("Macroplaza","Obelisco",0.78)
g.conecta("Macroplaza","Fundidora",2.79)
g.conecta("Macroplaza","Obispado",3.76)

g.conecta("Barrio Antiguo","Santa Lucia",0.48)
g.conecta("Barrio Antiguo","Macroplaza",0.38)
g.conecta("Barrio Antiguo","Estadio BBVA",6.27)
g.conecta("Barrio Antiguo","La Purisima",2.02)
g.conecta("Barrio Antiguo","Ciudad Universitaria",6.62)
g.conecta("Barrio Antiguo","Arena Monterrey",2.42)
g.conecta("Barrio Antiguo","Obelisco",1.22)
g.conecta("Barrio Antiguo","Fundidora",2.57)
g.conecta("Barrio Antiguo","Obispado",4.14)

g.conecta("Estadio BBVA", "Santa Lucia",6.4)
g.conecta("Estadio BBVA", "Macroplaza",6.56)
g.conecta("Estadio BBVA", "Barrio Antiguo",6.27)
g.conecta("Estadio BBVA", "La Purisima",8.3)
g.conecta("Estadio BBVA", "Ciudad Universitaria",9.38)
g.conecta("Estadio BBVA", "Arena Monterrey",4.61)
g.conecta("Estadio BBVA", "Obelisco",7.46)
g.conecta("Estadio BBVA", "Fundidora",4.15)
g.conecta("Estadio BBVA", "Obispado",10.4)

g.conecta("La Purisima","Santa Lucia",2.24)
g.conecta("La Purisima","Macroplaza",1.64)
g.conecta("La Purisima","Barrio Antiguo",2.02)
g.conecta("La Purisima","Estadio BBVA",8.30)
g.conecta("La Purisima","Ciudad Universitaria",6.45)
g.conecta("La Purisima","Arena Monterrey",4.03)
g.conecta("La Purisima","Obelisco",0.87)
g.conecta("La Purisima","Fundidora",4.38)
g.conecta("La Purisima","Obispado",2.12)

g.conecta("Ciudad Universitaria","Santa Lucia",6.26)
g.conecta("Ciudad Universitaria","Macroplaza",6.36)
g.conecta("Ciudad Universitaria","Barrio Antiguo",6.62)
g.conecta("Ciudad Universitaria","Estadio BBVA",9.38)
g.conecta("Ciudad Universitaria","La Purisima",6.45)
g.conecta("Ciudad Universitaria","Arena Monterrey",5.61)
g.conecta("Ciudad Universitaria","Obelisco",6.11)
g.conecta("Ciudad Universitaria","Fundidora",5.98)
g.conecta("Ciudad Universitaria","Obispado",6.9)

g.conecta("Arena Monterrey","Santa Lucia",1.96)
g.conecta("Arena Monterrey","Macroplaza",2.49)
g.conecta("Arena Monterrey","Barrio Antiguo",2.42)
g.conecta("Arena Monterrey","Estadio BBVA",4.61)
g.conecta("Arena Monterrey","La Purisima",4.03)
g.conecta("Arena Monterrey","Ciudad Universitaria",5.61)
g.conecta("Arena Monterrey","Obelisco",3.17)
g.conecta("Arena Monterrey","Fundidora",0.47)
g.conecta("Arena Monterrey","Obispado",5.95)

g.conecta("Obelisco","Santa Lucia",1.41)
g.conecta("Obelisco","Macroplaza",0.78)
g.conecta("Obelisco","Barrio Antiguo",122)
g.conecta("Obelisco","Estadio BBVA",7.46)
g.conecta("Obelisco","La Purisima",0.87)
g.conecta("Obelisco","Ciudad Universitaria",6.11)
g.conecta("Obelisco","Arena Monterrey",3.17)
g.conecta("Obelisco","Fundidora",3.53)
g.conecta("Obelisco","Obispado",2.9)

g.conecta("Fundidora","Santa Lucia",2.22)
g.conecta("Fundidora","Macroplaza",2.79)
g.conecta("Fundidora","Barrio Antiguo",2.57)
g.conecta("Fundidora","Estadio BBVA",4.15)
g.conecta("Fundidora","La Purisima",4.38)
g.conecta("Fundidora","Ciudad Universitaria",5.98)
g.conecta("Fundidora","Arena Monterrey",0.43)
g.conecta("Fundidora","Obelisco",3.53)
g.conecta("Fundidora","Obispado",6.35)

g.conecta("Obispado","Santa Lucia",4.33)
g.conecta("Obispado","Macroplaza",3.76)
g.conecta("Obispado","Barrio Antiguo",4.14)
g.conecta("Obispado","Estadio BBVA",10.4)
g.conecta("Obispado","La Purisima",2.12)
g.conecta("Obispado","Ciudad Universitaria",6.9)
g.conecta("Obispado","Arena Monterrey",5.95)
g.conecta("Obispado","Obelisco",2.9)
g.conecta("Obispado","Fundidora",6.35)

#EMPLEANDO KRUSKAL EN EL ALGORITMO DE APROXIMACION 
C=g.kruskal()
for i in range(50):
    bi=random.choice(list(C.V))
    dfs=C.DFS(bi)
    c=0
    for f in range(len(dfs)-1):
        c+=g.E[(dfs[f],dfs[f+1])]
        print(dfs[f],dfs[f+1],g.E[(dfs[f],dfs[f+1])])
    c+=g.E[(dfs[-1],dfs[0])]
    print(dfs[-1],dfs[0],g.E[(dfs[-1],dfs[0])])
    print("costo:",c,"\n")


#ALGORITMO EXACTO
import time
print("SOLUCION EXACTA\n")
tim=time.clock()
camino=[]
camino=g.Problem()
dfs=camino
best=0
for i in range(len(dfs)-1):
    best+=g.E[(dfs[i],dfs[i+1])]
best+=g.E[(dfs[-1],dfs[0])]
print("El camino mejor fue: ")
for k in camino:
    print(k,'->')
print(camino[0])
print("\n Con costo de: ",best)
print("Con tiempo de: ",time.clock()-tim)

