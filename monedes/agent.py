""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from mimetypes import init
from ia_2022 import agent, entorn
from monedes.entorn import AccionsMoneda, ClauPercepcio

SOLUCIO = " XXXC"


class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def actua(
        self, percep: entorn.Percepcio
    ) -> entorn.Accio | tuple[entorn.Accio, object]:
        estat=Estat(percep.to_dict())

        if self.__accions is None:
            self._cerca(estat)
        
        if len(self.__accions)>0:
            pass
        else:
           return AccionsMoneda.RES

class Estat:


    def __init__(self,info:dict=None, pare=None) -> None:
        if info is None:
            info={}
        self.__info=info
        self.__pare=pare
    
    def __hash__(self):
        return hash(tuple(self.__info.items()))

    def __getitem__(self, key):
        return self.__info[key]

    def __setitem__(self, key, value):
        self.__info[key] = value

    def legal(self)-> bool:
        '''Si no tiene estados negativos'''
        for key in [ClauPercepcio.MONEDES]:
            if self.__info[key]<0:
                return False
        return True

    def esMeta(self)->bool:
        '''El estado ganador es '''
        return self[ClauPercepcio.MONEDES]==" XXXC"

    def generarHijos(self)->list:
        '''Devuelve todos los estados anteriores hasta el actual'''
    estados_generados=[]



