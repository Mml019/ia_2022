import sys 
sys.path.append('C:\\Users\\missm\\miniconda3\\envs\\ia2022\\ia_2022')

from aspirador import agent, joc


def main():
    #aspirador=agent.AspiradorTaula()
    #aspirador = agent.AspiradorReflex()
    #aspirador=agent.AspiradorMemoria()
    aspirador=agent.AspiradorMemoriaProf()
    hab = joc.Casa([aspirador])
    hab.comencar()


if __name__ == "__main__":
    main()
