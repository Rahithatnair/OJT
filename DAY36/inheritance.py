class father: 
    def father_name(self):
        print("my father name is abc")
class son(father):
    pass
obj_father= father()
obj_son=son()
obj_son.father_name() 

#multilevel inheritance

class g_father:
    def g_father_name(self):
        print("my father name is abc")
class father(g_father): 
    def father_name(self):
        print("my father name is def")
class son(father): 
    def son_name(self):
        print("my name is ghi")

obj_g_father= father() 
obj_father= father() 
obj_son=son() 
obj_son.g_father_name() 
obj_son.father_name() 
obj_son.son_name() 


#multiple inheritance
class Father:
    def father_name(self):
        print("My father's name is ABC")
        
class Mother:
    def mother_name(self):
        print("My mother's name is PQR")
        
class Son(Mother, Father):
    pass

obj_father = Father()
obj_mother = Mother()
obj_son = Son()
obj_son.father_name()  
obj_son.mother_name() 
obj_father.father_name()
