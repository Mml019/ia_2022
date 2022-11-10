import sys 
sys.path.append('C:\\Users\\missm\\miniconda3\\envs\\ia2022\\ia_2022')

from practica1 import agent, joc


def main():
    rana = agent.Rana("Miquel")
    lab = joc.Laberint([rana], parets=True)
    lab.comencar()


if __name__ == "__main__":
    main()
