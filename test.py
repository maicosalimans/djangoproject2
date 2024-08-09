class koek:
    
    def stelling(self):
        print("Er bestaan vele soorten koek.")   
        
    def smaak(self):
        print("De meeste koeken zijn lekker.")
        
class boterkoek(koek):   
    def smaak(self):        
        print("Boterkoek smaakt naar boter.")

class honingkoek(koek):    
    def smaak(self):        
        print("Honingkoek smaakt naar honing.")
        
obj_koek = koek()
obj_btr = boterkoek()
obj_hng = honingkoek()

obj_koek.stelling()
obj_koek.smaak()

obj_btr.stelling()
obj_btr.smaak()

obj_hng.stelling()
obj_hng.smaak()