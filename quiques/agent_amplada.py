from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
        self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        
        
        
     def cerca():   
        estat_inicial=Estat(percep.to_dict)
        self.__oberts=[]
        self.__oberts.append(estat_inicial)
        while(self.__oberts):
            self.__oberts.remove(estat_inicial)
            if(estat_inicial.es_meta()):
                return self.tancat
            else:

                
                llista=estat_inicial.genera_fill()
                {
                    
                }