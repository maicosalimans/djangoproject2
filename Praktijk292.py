# code bestaat ui 2 klasse
# De klasse "Persona" is een parent class en bevat een methode voor het vertonen van gegevens "naam" en "id"
# De klasse "Docent" is een chold class. Naast de gevens "naam", "id", "salaris", en "vakinformatie" bevat deze ook een methode die de methode van parent class uitbreidt
# zodat uiteindelijk 
# - de gegevens "naam" en "id" van de parent class worden overgenoemen
# - bij het aanroepen van child class, alle gegevens uit beide classen worden getoond. 

class Persona(object):
    
    # __init__ staat voor constructor   
    def __init__(self, naam, idnummer):        
        self.naam = naam        
        self.idnummer = idnummer   
        
    def display(self):       
        print(self.naam)       
        print(self.idnummer)   
        
    def details(self):        
        print("Mijn naam is {}".format(self.naam))        
        print("Mijn id nummer is: {}".format(self.idnummer))
        
class Docent(Persona):   
    def __init__(self, naam, idnummer, salaris, vak):        
        self.salaris = salaris        
        self.vak = vak        
        
        # het oproepen van de __init__ van parent class        
        Persona.__init__(self, naam, idnummer)   
        
    def details(self):        
        print("Mijn naam is: {}".format(self.naam))        
        print("Mijn id nummer is: {}".format(self.idnummer))   
        print("Ik geef het vak: {}".format(self.vak))
        
x = Docent("Jan", "3456", "56000", "Engels")

x.details()