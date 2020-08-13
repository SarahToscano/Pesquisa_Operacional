from __future__ import print_function
from ortools.linear_solver import pywraplp

solver = pywraplp.Solver('simple_lp_program',
                         pywraplp.Solver.GLOP_LINEAR_PROGRAMMING)

def main():
    texto = []
    with open('instance5.txt') as arq:
        texto = arq.read()

    texto = texto.split()  # quebra os dados de acordo com os espaços
    # Converte os numeros de string para inteiro
    texto_num = list(map(int, texto))
   
    n=texto_num[0] #vertice
    m=texto_num[1] #arco
    s=texto_num[2] #origem
    t=texto_num[3] #escoadoro
 
    custo=[0]*(m+1)
    custo[m]=-1

    count =1
    flag =0 
    matriz = []
    aux=[t, s, -1 ,1000]
    for i in range(0, m+1):
        linha = []
        for j in range(0, 3):
            #if( j == 1):
            #if(texto_num[count] == 0):  
            #flag = 0
            #linhas -= 1
            linha.append(texto_num[count])
            count = count+1
                
        if(flag == 1):
            matriz.append(linha)
        flag = 1
    linha = []
    linha.append(t)
    linha.append(s)
    linha.append(1000)
    matriz.append(linha)

    #print(matriz)
    restricao = [0]*n
    somatorio = [0]*n
    #Definição de Variáveis
    x = [0]*(m+1) #arcos
    for i in range (0, m+1):
        x[i] = solver.NumVar(0, matriz[i][2], str(i))

    for ref in range (0, n):
        restricao[ref] = solver.Constraint(0,0)
        #print("REFERENCIA:", ref)
        #print(matriz)
        for vert in range (0,m+1):
            #print("analisando parte:", vert)
            if(matriz[vert][1]==ref):
                restricao[ref].SetCoefficient(x[vert], 1)
                #print(ref, vert, 1)
            if(matriz[vert][0]==ref):
                restricao[ref].SetCoefficient(x[vert], -1)
                #print(ref, vert, -1)

    objective = solver.Objective()
    for i in range (0,m+1):
        objective.SetCoefficient(x[i], custo[i])
    objective.SetMinimization()
    print("")
    solver.Solve()
    opt_solution=0
    for i in range (0,m+1):
        opt_solution += custo[i] * x[i].solution_value()
        #print('i = ', x[i].solution_value())
        opt_solution*=-1
    #print('Optimal objective value =', opt_solution)
    #print(matriz)
    print("\n   Arcos   |  Fluxos")
    print("-----------|---------")
    for i in range (0,m+1):
        if(x[i].solution_value()!=0):
            print(" ",matriz[i][0], "->", matriz[i][1], "  |  ", x[i].solution_value())
    print("\n Solucao otima: ", opt_solution)


main()
