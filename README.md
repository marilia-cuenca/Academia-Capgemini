# Academia-Capgemini
Desafio de Programação

"A agência Divulga Tudo precisa de um programa para gerenciar os seus anúncios online. O objetivo dos anúncios faz parte de uma campanha nas redes sociais. O sistema de gerenciamento permitirá a gestão do anúncio e o rastreio dos resultados da campanha".

Para atingir esse objetivo, criei um sistema em Python para o cadastro de anúncios, que contém: nome do anúncio, cliente, data de início, data de término e investimento por dia. O sistema retorna o valor total investido, a quantidade máxima de visualizações, a quantidade máxima de cliques e a quantidade máxima de compartilhamentos.

Foram importadas as bibliotecas "datetime", para calcular o intervalo de tempo, e a função "ceil" da biblioteca "math", para retornar o valor máximo. 

Após isso, foram determinadas as variáveis com os dados necessários para os anúncios e, a partir do que o usário digitar nos campos de dia, mês e ano do início do anúncio, e campos dia, mês e ano do término do anúncio, pode-se calcular o intervalo de tempo que o anúncio ficou/ficará no ar, em dias. 

Para o cálculo da quantidade máxima de visualizações, utilizei o código do arquivo "calculadora" e multipliquei pelo intervalo de tempo que o anúncio ficou/ficará no ar. O investimento total é calculado pela multiplicação entre o investimento diário e o intervalo de tempo. Para o cálculo da quantidade máxima de cliques, multiplica-se o investimento diário com a quantidade de pessoas que clicam no anúncio após visualizarem (12%) e o intervalo de tempo. A quantidade máxima de compartilhamentos é calculada pela multiplicação entre o investimento diário, a quantidade de pessoas que compartilham nas redes sociais após clicarem no anúncio (15%) e o intervalo de tempo.

Para a utilização do sistema, pede-se ao usuário digitar o nome do anúncio, cliente, data de início (separados por dia, mês e ano), data de término (separados por dia, mês e ano) e investimento por dia. 
