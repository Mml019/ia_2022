""" Fitxer que conté els diferents agents aspiradors.
Autora: Marta Martín López

Percepcions:
    ClauPercepcio.LOC: [Localitzacio.HABITACIO_ESQ, Localitzacio.HABITACIO_DRET]
    ClauPercepcio.ESTAT: [EstatHabitacio.NET, EstatHabitacio.BRUT]

Accions:
    AccionsAspirador.DRETA
    AccionsAspirador.ESQUERRA
    AccionsAspirador.ATURA
    AccionsAspirador.ASPIRA

Autor: Miquel Miró Nicolau (UIB), 2022
"""
import abc

import pygame

from aspirador.entorn import (AccionsAspirador, ClauPercepcio, EstatHabitacio,Localitzacio)
from ia_2022 import agent
from ia_2022 import entorn


class Aspirador(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=1)

    def pinta(self, display):
        img = pygame.image.load("../assets/aspirador/sprite.png")
        img = pygame.transform.scale(img, (100, 100))
        display.blit(img, self._posicio_pintar)

    @abc.abstractmethod
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio:
        pass


class AspiradorReflex(Aspirador):
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio:
        '''
            00  esq,net Localitzacio.*,EstatHabitacio.*
            01  esq,brut
            10  dreta,net
            11  dreta,brut
        '''
        #percep[ClauPercepcio.LOC] 
        if (percep.__getitem__(ClauPercepcio.ESTAT)==EstatHabitacio.BRUT):
            return AccionsAspirador.ASPIRA
        else: #estará limpio
            if(percep.__getitem__(ClauPercepcio.LOC)==Localitzacio.HABITACIO_DRET):
                return AccionsAspirador.ESQUERRA
                #else: 
            return AccionsAspirador.DRETA


        


class AspiradorTaula(Aspirador):
    TAULA = {
        (Localitzacio.HABITACIO_ESQ, EstatHabitacio.NET): AccionsAspirador.DRETA,
        (Localitzacio.HABITACIO_ESQ, EstatHabitacio.BRUT): AccionsAspirador.ASPIRA,
        (Localitzacio.HABITACIO_DRET, EstatHabitacio.NET): AccionsAspirador.ESQUERRA,
        (Localitzacio.HABITACIO_DRET, EstatHabitacio.BRUT): AccionsAspirador.ASPIRA,
    }

    def actua(self, percep: entorn.Percepcio) -> entorn.Accio:
        return AspiradorTaula.TAULA[
            (percep[ClauPercepcio.LOC], percep[ClauPercepcio.ESTAT])
            ]


class AspiradorMemoria(Aspirador):
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio:
        mem=self.get_memoria(1)
        self.set_memoria(percep)
        if(mem is not None and ((mem[ClauPercepcio.ESTAT]==EstatHabitacio.NET)and (percep[ClauPercepcio.ESTAT]==EstatHabitacio.NET ))):
            return AccionsAspirador.ATURA
        elif(percep[ClauPercepcio.ESTAT]==EstatHabitacio.BRUT):
            return AccionsAspirador.ASPIRA
        elif(percep.__getitem__(ClauPercepcio.LOC)==Localitzacio.HABITACIO_DRET):
            return AccionsAspirador.ESQUERRA
        else:
            return AccionsAspirador.DRETA
        ''' if(self.get_memoria(1) is None):
            self.set_memoria(percep) 
        percep2=entorn.Percepcio(self.get_memoria(1))
        if(percep.__getitem__(ClauPercepcio.ESTAT)==EstatHabitacio.NET):
            if(percep2.__getitem__(ClauPercepcio.LOC)==percep.__getitem__(ClauPercepcio.LOC)):
                if(percep2.__getitem__(ClauPercepcio.LOC)==Localitzacio.HABITACIO_DRET):
                    self.set_memoria(percep)
                    return AccionsAspirador.ESQUERRA
                else:
                        self.set_memoria(percep)
                        return AccionsAspirador.DRETA
            else:
                self.set_memoria(percep)
                return AccionsAspirador.ATURA        
        else:
            self.set_memoria(percep)
            return AccionsAspirador.ASPIRA'''
   


    
class AspiradorMemoriaProf(Aspirador):
    def actua(self, percep: entorn.Percepcio) -> entorn.Accio:
        accio = None

        mem = self.get_memoria(1)

        if percep[ClauPercepcio.ESTAT] is EstatHabitacio.BRUT:
            accio = AccionsAspirador.ASPIRA
        elif mem is not None and (mem[ClauPercepcio.ESTAT] is EstatHabitacio.NET):
            accio = AccionsAspirador.ATURA
        elif percep[ClauPercepcio.LOC] is Localitzacio.HABITACIO_ESQ:
            accio = AccionsAspirador.DRETA
        elif percep[ClauPercepcio.LOC] is Localitzacio.HABITACIO_DRET:
            accio = AccionsAspirador.ESQUERRA

        self.set_memoria(percep)

        return accio

