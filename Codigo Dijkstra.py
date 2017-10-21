from heapq import heappop, heappush

def flatten(L):
    while len(L) > 0:
        yield L[0]
        L = L[1]

class Grafo:
 
    def __init__(self):
        self.V = set() 
        self.E = dict() 
        self.vecinos = dict() 
 
    def agrega(self, v):
        self.V.add(v)
        if not v in self.vecinos: 
            self.vecinos[v] = set() 
 
    def conecta(self, v, u, peso=1):
        self.agrega(v)
        self.agrega(u)
        self.E[(v, u)] = self.E[(u, v)] = peso 
        self.vecinos[v].add(u)
        self.vecinos[u].add(v)
 
    def complemento(self):
        comp= Grafo()
        for v in self.V:
            for w in self.V:
                if v != w and (v, w) not in self.E:
                    comp.conecta(v, w, 1)
        return comp

    def shortest(self, v): 
        q = [(0, v, ())] 
        dist = dict()  
        visited = set() 
        while len(q) > 0: 
            (l, u, p) = heappop(q) 
            if u not in visited: 
                visited.add(u) 
                dist[u] = (l,u,list(flatten(p))[::-1] + [u])  	
            p = (u, p) 
            for n in self.vecinos[u]: 
                if n not in visited: 
                    el = self.E[(u,n)] 
                    heappush(q, (l + el, n, p))  
        return dist 

#Programa Principal
#5 nodos,10 aristas
print("Primer prueba 5 nodos, 10 aristas")

g=Grafo()
g.conecta('a','b',2)
g.conecta('a','c',4)
g.conecta('a','d',6)
g.conecta('a','e',8)
g.conecta('a','b',10)
g.conecta('b','c',12)
g.conecta('b','d',14)
g.conecta('b','e',16)
g.conecta('c','e',18)
g.conecta('c','d',20)

print(g.shortest('a'))


#10 nodos,20 aristas
print("Segunda prueba 10 nodos,20 aristas")

f=Grafo()
f.conecta('a','b',3)
f.conecta('a','c',9)
f.conecta('a','d',12)
f.conecta('a','e',7)
f.conecta('a','f',4)
f.conecta('a','g',3)
f.conecta('a','h',2)
f.conecta('a','i',1)
f.conecta('a','j',5)
f.conecta('b','c',11)
f.conecta('b','d',8)
f.conecta('c','d',9)
f.conecta('d','e',4)
f.conecta('e','f',7)
f.conecta('f','g',6)
f.conecta('g','h',1)
f.conecta('h','e',10)
f.conecta('i','j',14)
f.conecta('j','h',4)
f.conecta('j','g',5)
f.conecta('c','e',5)

print(f.shortest('a'))


#15 nodos,30 aristas
print("Tercera prueba 15 nodos, 30 aristas")
h=Grafo()
h.conecta('a','b',4)
h.conecta('a','c',8)
h.conecta('a','d',7)
h.conecta('a','e',5)
h.conecta('a','f',3)
h.conecta('a','g',2)
h.conecta('a','h',1)
h.conecta('b','i',9)
h.conecta('c','j',10)
h.conecta('d','k',11)
h.conecta('e','l',8)
h.conecta('f','m',4)
h.conecta('j','n',7)
h.conecta('a','ñ',9)
h.conecta('i','k',11)
h.conecta('b','b',3)
h.conecta('c','e',5)
h.conecta('d','i',6)
h.conecta('e','h',7)
h.conecta('f','c',10)
h.conecta('g','e',12)
h.conecta('h','f',15)
h.conecta('i','b',9)
h.conecta('j','c',3)
h.conecta('k','j',2)
h.conecta('l','f',1)
h.conecta('m','i',5)
h.conecta('n','k',8)
h.conecta('ñ','d',9)
h.conecta('a','m',13)

print(h.shortest('a'))


#20 nodos, 40 aristas)
print("Cuarta prueba 20 nodos, 40 aristas")

m=Grafo()
m.conecta('a','b',5)
m.conecta('a','c',2)
m.conecta('a','d',3)
m.conecta('c','e',4)
m.conecta('a','f',2)
m.conecta('a','g',5)
m.conecta('g','h',9)
m.conecta('a','i',10)
m.conecta('k','j',21)
m.conecta('a','k',34)
m.conecta('a','l',7)
m.conecta('c','m',8)
m.conecta('r','n',9)
m.conecta('a','ñ',12)
m.conecta('b','o',11)
m.conecta('c','p',2)
m.conecta('d','q',1)
m.conecta('e','r',5)
m.conecta('f','s',6)
m.conecta('g','m',7)
m.conecta('h','n',9)
m.conecta('i','l',11)
m.conecta('j','o',10)
m.conecta('m','p',12)
m.conecta('o','q',2)
m.conecta('s','r',3)
m.conecta('l','s',4)
m.conecta('k','e',5)
m.conecta('j','f',4)
m.conecta('b','g',7)
m.conecta('e','h',8)
m.conecta('d','i',12)
m.conecta('r','j',2)
m.conecta('s','k',5)
m.conecta('p','l',6)
m.conecta('n','m',7)
m.conecta('g','n',8)
m.conecta('f','ñ',9)
m.conecta('e','o',10)
m.conecta('s','p',1)

print(m.shortest('a'))



#25 nodos, 50 aristas
print("Quinta prueba 50 nodos, 50 aristas")

r=Grafo()
r.conecta('a','b',5)
r.conecta('a','c',1)
r.conecta('a','d',2)
r.conecta('a','e',53)
r.conecta('a','f',4)
r.conecta('a','g',7)
r.conecta('a','h',9)
r.conecta('a','i',12)
r.conecta('a','j',8)
r.conecta('a','k',9)
r.conecta('a','l',2)
r.conecta('a','m',3)
r.conecta('b','n',5)
r.conecta('a','ñ',8)
r.conecta('s','o',6)
r.conecta('d','p',51)
r.conecta('d','q',4)
r.conecta('p','r',7)
r.conecta('o','s',9)
r.conecta('x','t',3)
r.conecta('x','u',4)
r.conecta('r','v',57)
r.conecta('k','w',7)
r.conecta('s','x',56)
r.conecta('j','b',6)
r.conecta('e','c',3)
r.conecta('b','d',2)
r.conecta('a','e',51)
r.conecta('a','f',1)
r.conecta('x','g',2)
r.conecta('w','h',4)
r.conecta('v','i',5)
r.conecta('u','j',8)
r.conecta('s','k',10)
r.conecta('r','l',11)
r.conecta('q','m',9)
r.conecta('p','n',12)
r.conecta('o','ñ',13)
r.conecta('n','o',14)
r.conecta('m','p',5)
r.conecta('l','q',8)
r.conecta('k','r',9)
r.conecta('j','s',2)
r.conecta('i','t',1)
r.conecta('h','u',4)
r.conecta('g','v',7)
r.conecta('f','w',3)
r.conecta('e','x',2)
r.conecta('d','e',20)
r.conecta('c','b',11)

print(r.shortest('a'))


#RESULTADOS DEL PROGRAMA

#Primer prueba 5 nodos, 10 aristas
#{'a': (0, 'a', ['a']), 'c': (4, 'c', ['a', 'c']), 'd': (6, 'd', ['a', 'd']), 'e': (8, 'e', ['a', 'e']), 'b': (10, 'b', ['a', 'b'])}

#Segunda prueba 10 nodos,20 aristas
#{'a': (0, 'a', ['a']), 'i': (1, 'i', ['a', 'i']), 'h': (2, 'h', ['a', 'h']), 'b': (3, 'b', ['a', 'b']), 'g': (3, 'g', ['a', 'g']),
#'f': (4, 'f', ['a', 'f']), 'j': (5, 'j', ['a', 'j']), 'e': (7, 'e', ['a', 'e']), 'c': (9, 'c', ['a', 'c']), 'd': (11, 'd', ['a', 'b', 'd'])}

#Tercera prueba 15 nodos, 30 aristas
#{'a': (0, 'a', ['a']), 'h': (1, 'h', ['a', 'h']), 'g': (2, 'g', ['a', 'g']), 'f': (3, 'f', ['a', 'f']), 'b': (4, 'b', ['a', 'b']),
#'l': (4, 'l', ['a', 'f', 'l']), 'e': (5, 'e', ['a', 'e']), 'd': (7, 'd', ['a', 'd']), 'm': (7, 'm', ['a', 'f', 'm']), 'c': (8, 'c', ['a', 'c']),
#'ñ': (9, 'ñ', ['a', 'ñ']), 'j': (11, 'j', ['a', 'c', 'j']), 'i': (12, 'i', ['a', 'f', 'm', 'i']), 'k': (13, 'k', ['a', 'c', 'j', 'k']),
#'n': (18, 'n', ['a', 'c', 'j', 'n'])}

#Cuarta prueba 20 nodos, 40 aristas
#{'a': (0, 'a', ['a']), 'c': (2, 'c', ['a', 'c']), 'f': (2, 'f', ['a', 'f']), 'd': (3, 'd', ['a', 'd']), 'p': (4, 'p', ['a', 'c', 'p']),
#'q': (4, 'q', ['a', 'd', 'q']), 'b': (5, 'b', ['a', 'b']), 'g': (5, 'g', ['a', 'g']), 's': (5, 's', ['a', 'c', 'p', 's']),
#'e': (6, 'e', ['a', 'c', 'e']), 'j': (6, 'j', ['a', 'f', 'j']), 'o': (6, 'o', ['a', 'd', 'q', 'o']), 'l': (7, 'l', ['a', 'l']),
#'r': (8, 'r', ['a', 'f', 'j', 'r']), 'i': (10, 'i', ['a', 'i']), 'k': (10, 'k', ['a', 'c', 'p', 's', 'k']), 'm': (10, 'm', ['a', 'c', 'm']),
#'ñ': (11, 'ñ', ['a', 'f', 'ñ']), 'n': (13, 'n', ['a', 'g', 'n']), 'h': (14, 'h', ['a', 'c', 'e', 'h'])}

#Quinta prueba 50 nodos, 50 aristas
#{'a': (0, 'a', ['a']), 'c': (1, 'c', ['a', 'c']), 'f': (1, 'f', ['a', 'f']), 'd': (2, 'd', ['a', 'd']), 'l': (2, 'l', ['a', 'l']),
#'m': (3, 'm', ['a', 'm']), 'b': (4, 'b', ['a', 'd', 'b']), 'e': (4, 'e', ['a', 'c', 'e']), 'w': (4, 'w', ['a', 'f', 'w']),
#'q': (6, 'q', ['a', 'd', 'q']), 'x': (6, 'x', ['a', 'c', 'e', 'x']), 'g': (7, 'g', ['a', 'g']), 'h': (8, 'h', ['a', 'f', 'w', 'h']),
#'j': (8, 'j', ['a', 'j']), 'p': (8, 'p', ['a', 'm', 'p']), 'ñ': (8, 'ñ', ['a', 'ñ']), 'k': (9, 'k', ['a', 'k']), 'n': (9, 'n', ['a', 'd', 'b', 'n']),
#'t': (9, 't', ['a', 'c', 'e', 'x', 't']), 'i': (10, 'i', ['a', 'c', 'e', 'x', 't', 'i']), 's': (10, 's', ['a', 'j', 's']),
#'u': (10, 'u', ['a', 'c', 'e', 'x', 'u']), 'r': (13, 'r', ['a', 'l', 'r']), 'v': (14, 'v', ['a', 'g', 'v']), 'o': (19, 'o', ['a', 'j', 's', 'o'])}
