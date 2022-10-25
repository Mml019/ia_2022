import sys 
sys.path.append('C:\\Users\\missm\\miniconda3\\envs\\ia2022\\ia_2022')

from quiques import agent_amplada, agent_profunditat, joc


def main():
    barca = agent_amplada.BarcaAmplada()
    #barca= agent_profunditat.BarcaProfunditat()

    illes = joc.Illes([barca])
    illes.comencar()


if __name__ == "__main__":
    main()
