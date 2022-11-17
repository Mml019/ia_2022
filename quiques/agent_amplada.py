from importlib.machinery import FrozenImporter
from queue import Empty
from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca


class BarcaAmplada(Barca):
    def __init__(self):
        super(BarcaAmplada, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None
    
    def _cercaProf(self, estat: Estat):
        self.__oberts = []
        self.__tancats = set()

        self.__oberts.append(estat)
        actual = None
        while len(self.__oberts) > 0:
            actual = self.__oberts[0]
            self.__oberts = self.__oberts[1:]

            if actual in self.__tancats:
                continue

            if not actual.es_segur():
                self.__tancats.add(actual)
                continue

            estats_fills = actual.genera_fill()

            if actual.es_meta():
                break

            for estat_f in estats_fills:
                self.__oberts.append(estat_f)

            self.__tancats.add(actual)
        if actual is None:
            raise ValueError("Error impossible")

        if actual.es_meta():
            accions = []
            iterador = actual

            while iterador.pare is not None:
                pare, accio = iterador.pare

                accions.append(accio)
                iterador = pare
            self.__accions = accions
            return True

    def _cerca(self, estat: Estat):
        self.__oberts=[]
        self.__tancats=set()

        self.__oberts.append(estat)

        while(self.__oberts is not  Empty):
            #eliminarlo de FIFO
            estat_actual = self.__oberts.pop(0)

            #comprobar si se puede seguir con ese estado
            if not estat_actual.es_segur() or estat_actual in self.__tancats:
                self.__tancats.add(estat_actual)
                continue #volver inicio bucle a por siguiente elemento

            if estat_actual.es_meta():
                break
            
            hijos=estat_actual.genera_fill()

            for i in hijos:
                self.__oberts.append(i)
            self.__tancats.add(estat_actual)

        if estat_actual is None:
            raise ValueError("Error impossible")
        
        if estat_actual.es_meta():
            accions=[]
            iterador=estat_actual

            while iterador.pare :
                pare, accion=estat_actual.pare
                accions.append(accion)
                iterador=pare
            self.__accions=accions
            return True 

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat = Estat(percep.to_dict())
        
        if self.__accions is None:
            self._cercaProf(estat=estat)

        if len(self.__accions) > 0:
            return AccionsBarca.MOURE, self.__accions.pop()
        else:
            return AccionsBarca.ATURAR
                