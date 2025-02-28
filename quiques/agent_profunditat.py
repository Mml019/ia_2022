""" Fitxer que conté l'agent barca en profunditat.

S'ha d'implementar el mètode:
    actua()
"""
from queue import Empty
from ia_2022 import entorn
from quiques.agent import Barca, Estat
from quiques.entorn import AccionsBarca, ClauPercepcio


class BarcaProfunditat(Barca):
    def __init__(self):
        super(BarcaProfunditat, self).__init__()
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def actua(
            self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:

        estat=Estat(percep.to_dict())
        if self.__accions is None:
            self._cercaProf(estat=estat)

        if self.__accions is not Empty:
            return AccionsBarca.MOURE,self.__accions.pop()
        else:
            return AccionsBarca.ATURAR

    def actuaProf(self,percep):
        estat = Estat(percep.to_dict())

        if self.__accions is None:
            self._cerca(estat=estat)

        if len(self.__accions) > 0:
            return AccionsBarca.MOURE, self.__accions.pop()
        else:
            return AccionsBarca.ATURAR

    def _cercaProf(self, estat:Estat):
        self.__oberts = []
        self.__tancats = set()

        self.__oberts.append(estat)

        actual = None
        while len(self.__oberts) > 0:
            actual = self.__oberts.pop()
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
        else:
            return False

    def _cerca(self,estat:Estat):
        estat_inicial=estat
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
                
