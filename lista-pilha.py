
# coding: utf-8

# In[ ]:


'''
Univesidade Federal de Pernambuco -- UFPE (http://www.ufpe.br)
Centro de Informatica -- CIn (http://www.cin.ufpe.br)
Bacharelado em Sistemas de Informacao
IF969 -- Algoritmos e Estruturas de Dados


FORKED FROM: Antônio Paulino de Lima Neto (apln2@cin.ufpe.br) (2018-03-01)

Autor:  Anderson Sobrinho Lima Laurentino
Email:         asll@cin.ufpe.br
Data:            2019-09-16
'''


# In[1]:


class Item:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


# In[2]:


class Lista:
    def __init__(self, init):
        self._item = None
        self._size = 0
        
        for item in init:
            self.append(item)
    
    @property
    def length(self):
        return self._size
    
    def append(self, valor):
        self._size += 1
        
        if self._item == None:
            self._item = Item(valor)
            return
        
        aux = self._item
        while not aux.next == None:
            aux = aux.next
        
        aux.next = Item(valor)
        aux.next.previous = aux
    
    def _get_item(self, index):
        if index < 0 or index > self._size-1:
            raise ValueError("Index out exception!")
            return
        
        count = 0
        aux = self._item
        
        while count < index:
            aux = aux.next
            count += 1
        
        
        return aux
    
    def __setitem__(self, index, value):
        self._get_item(index).value = value
    
    def __getitem__(self, index):
        return self._get_item(index).value
    
    def pop(self, index):
        if index < 0 or index > self._size-1:
            raise ValueError("Index out exception!")
            return
        
        if index == 0:
            self._size -= 1
            self._item = self._item.next
            return
        
        before = self._get_item(index-1)
        after = self._get_item(index+1) if index+1 != self._size+1 else None
        
        self._size -= 1
        before.next = after
    
    def __repr__(self):
        return f"Lista({self.__str__()})"
    
    def __str__(self):
        result = "["
        for i in range(self._size):
            result += str(self.__getitem__(i)) + ("," if i < self._size-1 else "")
        
        result += "]"
        
        return result


# In[3]:


class Pilha(Lista):
    def append(self, valor):
        self._size += 1
        
        if self._item == None:
            self._item = Item(valor)
            return
        
        else:
            aux = self._item
    
            self._item = Item(valor)
            self._item.next = aux
            aux.previous = self._item
    
    def __repr__(self):
        return f"Pilha({self.__str__()})"


# In[9]:


lista = Lista([1000, 20, 30])

lista.append(10)
lista.append(20)
lista.append(30)
lista.append(100)
lista.append(300)

print(f"Size of: {lista.length}\n")

for i in range(lista.length):
    print(f"[{i}] = {lista[i]}")
    

lista.pop(2)
lista.pop(2)

print(f"\n\nSize: {lista.length}\n")

for i in range(lista.length):
    print(f"[{i}] = {lista[i]}")
    
    
lista[1] = 50

print(f"\n\nSize of: {lista.length}\n")

for i in range(lista.length):
    print(f"[{i}] = {lista[i]}")
    
print("\n", repr(lista))


# In[11]:


pilha = Pilha("Algoritimos")

pilha.append('a')
pilha.append('Z')
pilha.append(' ')
pilha.append(100)
pilha.append(300)
    
pilha[1] = 'z'

print(f"Size: {pilha.length}\n")

for i in range(pilha.length):
    print(f"[{i}] = {pilha[i]}")

print("\n", repr(pilha))

