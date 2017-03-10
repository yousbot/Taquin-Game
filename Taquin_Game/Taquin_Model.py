'''
Created on 10 mars 2017

@author: Youssef Sbai Idrissi
@Place : Morocco, Casablanca

'''

class Taquin(object):

    def __init__(self, inp_list, out_list):
        
        self.In = inp_list
        self.Out = out_list
        
        self.Siblings = []
        self.Path_List = []
        self.Zero_Index = -1
        self.Path_List.append(inp_list)

    def print_Elements(self):
        
        print(" In  : " , self.In)
        print("\n Out : ", self.Out)
        
    
    def Check_Validity(self):
        return self.In == self.Out

    def Generate_Siblings(self):
        self.Zero_Index = self.In.index('.')
        
        Temp_List = self.In[:]
        if self.Zero_Index != 0 or self.Zero_Index != 3 or self.Zero_Index != 6 :

            Temp_List[self.Zero_Index] = Temp_List[self.Zero_Index + 1]
            Temp_List[self.Zero_Index + 1] = '.'
            
            self.Siblings.append(Temp_List)
            Temp_List = []
            Temp_List = self.In[:]

            
        if self.Zero_Index != 2 or self.Zero_Index != 5 or self.Zero_Index != 8 :

            Temp_List[self.Zero_Index] = Temp_List[self.Zero_Index - 1]
            Temp_List[self.Zero_Index - 1] = '.'
            
            self.Siblings.append(Temp_List)
            Temp_List = []
            Temp_List = self.In[:]
            
        if self.Zero_Index - 3 > -1 :

            Temp_List[self.Zero_Index] = Temp_List[self.Zero_Index - 3]
            Temp_List[self.Zero_Index - 3] = '.'
            
            self.Siblings.append(Temp_List)
            Temp_List = []
            Temp_List = self.In[:]
        
        if self.Zero_Index + 3 < 9 :

            Temp_List[self.Zero_Index] = Temp_List[self.Zero_Index + 3]
            Temp_List[self.Zero_Index + 3] = '.'
            
            self.Siblings.append(Temp_List)
            Temp_List = []
            Temp_List = self.In[:]
        
            
    def Print_Tree(self):
        
        for item in self.Siblings :
            print(" \n \t -  ", item)
        
    
    def Get_The_Fittest(self):
        Coefs = []
        for iter in self.Siblings:
            coof = 0
            for j in iter :
                if iter.index(j) != self.Out.index(j) :
                # Equation : 
                # Dist = | Level(x)-Level(Y) | + | Pos(x) - Pos(y) |
                # with : Level(x) = int(index / 3 )
                #Pos(x) = index - Level(x)*3
                    if j != '.' :
                        
                        Level_iter = iter.index(j)//3
                        Level_Out = self.Out.index(j)//3
                        Pos_iter = iter.index(j) - Level_iter*3
                        Pos_Out = self.Out.index(j) - Level_Out*3
                        coof += abs(Level_iter - Level_Out ) + abs( Pos_iter - Pos_Out )
            Coefs.append(coof)
        
        #print(" Min_Coef : ", min(Coefs))
        
        
       
        #print(" Coef index : " , Coefs.index(min(Coefs)))
            
        self.Path_List.append(self.Siblings[Coefs.index(min(Coefs))])
        self.In = self.Siblings[Coefs.index(min(Coefs))]
        #print(" New Path : " , self.Path_List)
        
    def Print_Resolution_Steps(self):
        
        for item in self.Path_List :
            
            print(" Step ", self.Path_List.index(item) + 1)
            print("\n ", item[0], " ", item[1], " ", item[2])
            print("\n ", item[3], " ", item[4], " ", item[5])
            print("\n ", item[6], " ", item[7], " ", item[8])
            
            print("\n")

    
    
    def Resolve(self, T):
        
        while not T.Check_Validity() :
            #T.print_Elements()
            T.Generate_Siblings()
            T.Get_The_Fittest()
        
        self.Print_Resolution_Steps()
        
L_in = "2,8,3,1,6,4,7,.,5".split(',')
L_Out = "1,2,3,8,.,4,7,6,5".split(',')
T = Taquin(L_in, L_Out)
T.Resolve(T)
