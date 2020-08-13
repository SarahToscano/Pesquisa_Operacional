# Modelagem de Fluxo Máximo

## Descrição

A modelagem e resolução de problemas, nos quais é necessário definir de modo quantitativo a distribuição, condução ou coordenação de quaisquer operações ou atividades em instituições pode ser realizada com a utilização da programação linear. Este tipo de programação apresenta diversos métodos para facilitar a modelagem matemática de situações problemas reais através de sistemas de equações/inequações. Os modelos objetivam maximizar ou minimizar o valor da função linear interpretada a restringindo a um determinado conjunto de restrições específicos da situação. 
Na área de programação linear, o conceito “rede” surge como modo de facilitar a representação e ilustração do problema através de um grafo que descreve e indica os componentes do sistema, seus conjunto de custos, demandas, capacidades e fluxos associados ao arcos. Os problemas de rede podem ser divididos em várias categorias, como problema do caminho mais curto, fluxo máximo, custo mínimo, entre outros. Alguns desses métodos possuem uma estrutura mais específica para as aplicações, enquanto outros são mais abrangentes fornecem uma metodologia mais unificada e genérica.
Nesse contexto, o seguinte relatório irá focar na descrição de 2 problemas desses 5, sendo eles o problema de fluxo máximo (PFM) e do problema de fluxo de custo mínimo (PFCM). Também serão realizadas modelagens teóricas e práticas utilizando estes dois métodos em aplicações de situações problemas.

## Definição do Problema

O Problema do fluxo máximo é um dos casos particulares do problema do fluxo de custo mínimo, os dois são semelhantes por considerarem o fluxo por uma rede com capacidades de arcos limitadas sendo formulado como um problema de programação linear. 
O problema do fluxo máximo trata-se de um problema particular do Problema do fluxo mínimo, ele permite avaliar a capacidade de transporte, ou seja em fluxo através de uma rede. O objetivo é encontrar o fluxo máximo da rede. Dada uma rede, com um nó de entrada e um nó de saída, com capacidades associadas a cada ramo, pretende-se saber qual  é o fluxo máximo, de um certo bem, que se pode enviar da entrada para a saída. 
Definição: De modo geral o fluxo de máximo consiste em enviar a quantidade máxima de fluxo de uma dada origem s para um destino t em uma rede com uma capacidade, ou seja,  Ci< ∞ ∀ i=1,..,m. Dada uma rede, com um nó de entrada e um nó de saıda, com capacidades associadas a cada ramo, pretende-se saber qual é o fluxo máximo, que se pode enviar da entrada para a saída.

Modelando de forma genérica:

	- xij – fluxo que passa no ramo (i, j), de i para j
	- cij – capacidade do ramo (i, j)
	- Nó 1 – Nó  de entrada
	- Nó t – Nó de saída
  
  O objetivo é a maximização do fluxo pela rede. Usando-se a convenção de que os somatórios são considerados apenas sobre arcos existentes, a formulação de programação linear desse problema  com a função objetivo para maximizar o fluxo de uma rede ficará assim:

