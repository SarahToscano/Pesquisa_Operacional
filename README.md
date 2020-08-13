# Modelagem de Fluxo Máximo

## Descrição

A modelagem e resolução de problemas, nos quais é necessário definir de modo quantitativo a distribuição, condução ou coordenação de quaisquer operações ou atividades em instituições pode ser realizada com a utilização da programação linear. Este tipo de programação apresenta diversos métodos para facilitar a modelagem matemática de situações problemas reais através de sistemas de equações/inequações. Os modelos objetivam maximizar ou minimizar o valor da função linear interpretada a restringindo a um determinado conjunto de restrições específicos da situação. 
Na área de programação linear, o conceito “rede” surge como modo de facilitar a representação e ilustração do problema através de um grafo que descreve e indica os componentes do sistema, seus conjunto de custos, demandas, capacidades e fluxos associados ao arcos. Os problemas de rede podem ser divididos em várias categorias, como problema do caminho mais curto, fluxo máximo, custo mínimo, entre outros. Alguns desses métodos possuem uma estrutura mais específica para as aplicações, enquanto outros são mais abrangentes fornecem uma metodologia mais unificada e genérica.
Nesse contexto, o seguinte relatório irá focar na descrição de 2 problemas desses 5, sendo eles o problema de fluxo máximo (PFM) e do problema de fluxo de custo mínimo (PFCM). Também serão realizadas modelagens teóricas e práticas utilizando estes dois métodos em aplicações de situações problemas.

## Definição do Problema de Fluxo Máximo

O Problema do fluxo máximo é um dos casos particulares do problema do fluxo de custo mínimo, os dois são semelhantes por considerarem o fluxo por uma rede com capacidades de arcos limitadas sendo formulado como um problema de programação linear. 
O problema do fluxo máximo trata-se de um problema particular do Problema do fluxo mínimo, ele permite avaliar a capacidade de transporte, ou seja em fluxo através de uma rede. O objetivo é encontrar o fluxo máximo da rede. Dada uma rede, com um nó de entrada e um nó de saída, com capacidades associadas a cada ramo, pretende-se saber qual  é o fluxo máximo, de um certo bem, que se pode enviar da entrada para a saída. 
Definição: De modo geral o fluxo de máximo consiste em enviar a quantidade máxima de fluxo de uma dada origem s para um destino t em uma rede com uma capacidade, ou seja,  Ci< ∞ ∀ i=1,..,m. Dada uma rede, com um nó de entrada e um nó de saıda, com capacidades associadas a cada ramo, pretende-se saber qual é o fluxo máximo, que se pode enviar da entrada para a saída.

Modelando de forma genérica:

	- xij – fluxo que passa no ramo (i, j), de i para j
	- cij – capacidade do ramo (i, j)
	- Nó 1 – Nó  de entrada
	- Nó t – Nó de saída
  
  O objetivo é a maximização do fluxo pela rede. Usando-se a convenção de que os somatórios são considerados apenas sobre arcos existentes, a formulação de programação linear desse problema  com a função objetivo para maximizar o fluxo de uma rede ficará assim:
  
 <p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/1.png">
  </p>
  
  Sujeito a: 
  
  <p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_2.png">
  </p>
  
  A primeira restrição se refere ao equilíbrio de fluxos nos nós, e as restrições de menor e maior igual se refere a restrições de capacidade. 
Utilizando um exemplo do livro 9.4-1* vamos resolver o problema utilizando o metodo do fluxo maximo, para encontrar o padrão de fluxo dado o fluxo máximo da origem ao escoadouro, dado que a capacidade de arco do nó i ao nó j é o número mais próximo ao nó i ao longo do arco entre esses nós. 

  <p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_3.png">
  </p>
  

  Sabendo, o problema do fluxo máximo pode ser descrito como a seguir:

-  Todo o fluxo através de uma rede direcionada e conectada origina-se de um nó, denominado origem e termina em outro nó, chamado escoadouro. (A origem e o escoadouro no problema  são, respectivamente, a entrada do parque no nó 1 e a vista panorâmica no nó 7.)

-  Todos os nós restantes são nós de transbordo. (São eles os nós 2. 3, 4, 5 e 6, neste caso)

-  O fluxo através de um arco é permitido apenas na direção indicada pela seta, em que a quantidade máxima de fluxo é fornecida pela capacidade daquele arco. Na origem, todos os arcos apontam no sentido de se afastarem do nó. No escoadouro, todos eles apontam no sentido de se aproximar do nó.

-  O objetivo é maximizar a quantidade total de fluxo da origem para o escoadouro. Essa quantida- de é medida em qualquer uma das duas maneiras equivalentes, ou seja, a quantidade que sai da origem ou, então, a quantidade que chega ao escoadouro.

  Neste problema vamos mandar o máximo possível de fluxo até que chegue no destino 7. Exemplificando, vamos observar a imagem 1 com um exemplo de tubulação de água. Abrindo a torneira na origem 1 e cada um dos arcos representam uma tubulação e queremos que chegue o máximo de água no destino, ou seja, no grafo 7. Podendo utilizar todos os arcos ou o máximo possível de arcos e cada arco tem uma restrição de fluxo máximo. 

  Por exemplo, no arco de 1 para o 2 tem a restrição de capacidade igual a  6, podendo passar por lá um valor menor ou igual a esta capacidade, ou seja, qualquer número entre 0 e 6 pois está é a capacidade máxima daquele arco. Todos os arcos têm uma capacidade máxima determinada, observando todos os arco vamos descobrir qual é o máximo que chega no destino.

  Primeiro vamos determinar nossa variável de decisão, pois temos que decidir quanto vai passar em cada arco.

 <p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_4.png">
  </p>
  
  A figura 2 exemplifica a quantidade que passa em uma dada origem i a um dado destino j. Vamos definir a quantidade para cada arco a ser utilizado.
Vamos definir o Z a função objetivo como mostrado na figura 3, para isso vamos observar para este caso específico X57 e X67, este são os que chegam diretamente em no destino. Em que cada uma dessas variáveis vai passar o maior valor possível para o vértice 7 para ter o fluxo máximo, dependendo do comportamento do fluxo desde a origem. 


 <p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_5.png">
  </p>
  
  Uma vez definida a função objetivo, vamos definir as restrições. Tomando como exemplo o nó 2 tudo que entra nele vai sair pois é um nó de transbordo. Como mostrado na Figura 4, vamos fazer essa análise para todos os nós as restrições de balanceamento. Vamos também fazer as restrições de fluxo para cada nó de acordo com a capacidade dos arcos.

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_6.png">
  </p>
  
  
  Logo, temos as restrições de balanceamento  dos nós e todas as restrições para cada arco. Para cada nó intermediário temos a restrição do nó 1, 2, 3, 4, 5, 6 e para cada arco temos uma restrição.
Utilizando o Solver  para formular e resolver o problema do fluxo máximo, obtemos a seguinte solução viável: 

 - O fluxo total é igual a 9;
 - Solução viavel:  X12 = 4, X13 = 4, X14 = 1, X25 = 4, X34 = 1, X35  = 0, X36 = 3 , X46 = 2, X57 = 4, X67 = 5. 

Logo, tudo que entra na rede chega no destino.

## Modelagem de um problema de fluxo máximo

  Um PFM consiste na maximização de determinado fluxo entre uma origem e um destino. Para torná-lo um PFCM será necessário aplicar algumas reformulações ao problema. 
Inicialmente, o PFM apresenta uma capacidade máxima e uma ausência de custos em seus arco, então a primeira mudança a ser realizada é que todos os arcos serão configurados com custo igual a zero (cij = 0). 

  A segunda mudança é a escolha do valor limite F, que será o limite superior para o fluxo máximo que irá passar pela rede. Entre os nós da rede esse valor estará presente apenas na origem e no escoadouro, pois esses são os únicos nós que possuem oferta e demanda no nosso problema. 

   E por último, a inclusão de um arco ligando diretamente a origem e o escoadouro. Diferente dos demais arcos, este terá um custo igual a -1 e capacidade ilimitada, essas características são responsáveis por fazer com que o PFCM realize o envio do fluxo com os demais arcos.
   
   O problema do fluxo de custo mínimo enviará o fluxo viável máximo através dos demais arcos, que alcança o objetivo do problema  do fluxo máximo. Aplicando essa formulação resultará  na figura 5, em  que os números dados próximos arcos originais são as capacidades de arco. 

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_7.png">
  </p>
  
  ## Descrição do programa 
  
  Nesta seção será realizada a resolução da letra ‘a’ da questão 9.4.3 disponível em [1]. Tal questão é reescrita abaixo. O programa consiste na resolução desta questão:
  
  O diagrama da Figura 2 representa um sistema de aquedutos que se origina em três rios (nós R1, R2 e R3) e termina em uma cidade importante (nó T), onde os demais nós são pontos de junção nesse sistema. A Tabela I mostra a quantidade máxima de água que pode ser bombeada diariamente por meio de cada aqueduto.

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_8.png">
  </p>
  
  Desse modo o problema propõe a sua formulação como um problema do fluxo máximo, de modo que maximize o fluxo de água para a cidade. A solução da questão deve incluir a identificação da origem, escoadouro e nós de transbordos. Além disso também é requerido o esquemático da rede completa com a capacidade de cada arco.


  ## Lógica de programação
  
  Para a formulação do problema apresentado no exercício como um problema de fluxo máximo serão seguidos os passos para transformação apresentados nos tópicos anteriores. Observando a rede fornecida pelo problema percebe-se que a primeira mudança será em relação às origens. Como foi explicado anteriormente um PFM deve possuir apenas uma origem, então neste caso uma origem “fantasma” é adicionada a rede ligando as três origens originais (R1, R2 e R3) a um único ponto. Desse esse novo vértice possui arcos de ligações com R1, R2 e R3, os quais são nós de transporte. Tais modificações na rede são ilustradas na Figura 3.

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_9.png">
  </p>
  
  
  Em seguida, podemos definir a capacidade dos arcos que saem da origem através da análise da “conservação de fluxo” o qual indica que nenhum fluxo pode ser criado ou destruído pela rede. Desse modo, as demandas dos arcos que saem das suas conexões devem ser iguais aos valores dos arcos que entram no nó. Por exemplo, o R1 possui um fluxo de saída equivalente a 245 (130+115). Assim, como a soma dos valores que entram em um nó devem ser iguais a soma dos valores que saem, tempo que o fluxo que é inserido em R1 deve ter valor máximo de 245. Ou seja, o valor atribuído ao arco que conecta a origem à R1 é equivalente a 245. De modo análogo, o valor do arco  O-R2 é 270 e  O-R3 equivale a  260. A Figura 4 ilustra o esquemático completo da rede com a atribuição dos valores aos arcos que saem da origem. 


<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_10.png">
  </p>
  
  
 ## Instruções para execução do código
 
 O código para  implementação da modelagem descrita anteriormente foi feito com a linguagem Python, com o software de otimização OR-Tools e o solver de programação linear GLOP. Para o uso do código é necessário a instalação do OR-Tools e utilização de algumas de suas bibliotecas para Python, essa etapa pode ser realizada seguindo as instruções encontradas em [2]. 
	Para executar o programa é necessário definir manualmente qual será o arquivo de texto a ser utilizado como instância. Além disso os arquivos das instâncias devem estar na mesma pasta em que o arquivo main.py está localizado. Para alterar o arquivo de instância a ser utilizado, a linha 9 do arquivo main.py deve ser alterada. Troca-se o texto entre aspas simples destacado em amarelo, pelo nome da instância que você deseja utilizar.

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_11.png">
  </p>

Após isso, deve-se compilar o arquivo, através do comando:

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_12.png">
  </p>

Dessa forma será exibida a solução do problema de acordo com o seguinte formato:

<p align="center">
    <img src="https://github.com/SAndradeTC/Pesquisa_Operacional/blob/master/Screenshot_15.png">
  </p>








  

