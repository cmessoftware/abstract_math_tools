from itertools import permutations
from .utils.nt_basics import has_unique_numbers, has_bijections, gcd

class zn_group:
    
   def __init__ (self, n):
       self.n = n
       self.G = [i for i in range(n)]
       
   def is_isomorphic(self,H):
       if self.order(H) != self.order(self.G):
           return False
       if not has_unique_numbers(H):
           return False
       if not has_bijections(H,self.G):
           return False
        
       return True                 
           
   
   def is_normal(self, H):
       return H
   
   def order(self,a):
       for i in range(100):
           if (a*(i+1))%self.n == 0:
               return i+1
    
       return float('inf')
   
           
   def is_abelian(self):
       for a in self.G:
        for b in self.G:
            if self.binary_operation(a, b) != self.binary_operation(a ,b):
                return False
        return True
   
   def conjugate_class_subgroups(self, n):
    def conjugate(perm, g):
        return tuple(g[i - 1] for i in perm)

    def find_conjugacy_classes(elements):
        conjugacy_classes = []
        while elements:
            current = [elements.pop()]
            to_remove = []
            for perm in elements:
                is_conjugate = False
                for g in current:
                    conjugated = conjugate(perm, g)
                    if conjugated in elements:
                        is_conjugate = True
                        current.append(perm)
                        to_remove.append(conjugated)
                        break
                if is_conjugate:
                    break
            for r in to_remove:
                elements.remove(r)
            conjugacy_classes.append(current)
        return conjugacy_classes

    symmetric_group = list(permutations(range(1, n + 1)))
    return find_conjugacy_classes(symmetric_group)

   def cardinality(self,n):
       return n    
  
   def binary_operation(self,a,b):
       return (a+b)%self.n
      
   def gens(self):
       return [i for i in range(self.n) if gcd(i,self.n) == 1 ]
        
   def cayley_table(self):
        return []
        