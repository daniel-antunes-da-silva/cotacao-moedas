# cotacao-moedas
Esse é um projeto simples de cotação de moedas e conversão (dólar, euro, real e iene japonês), além da flutuação diária de cada uma delas. 
Foi feito através da biblioteca requests do python e também utilizando a Awesome API para solicitar as informações. 
Foi utilizado o datetime para pegar a data atual no momento que roda o código, mostrando que a cotação está atualizada.

Além da cotação, é possível fazer a conversão de uma moeda para a outra, no valor especificado pelo usuário. 
O programa funciona com tratamento de erros, ou seja, se o usuário digitar valores string onde são solicitados números, ou escolher opções que não existam, 
o programa informará que houve erro e será solicitado novamente até que seja digitado da forma correta. Além disso, o usuário pode optar
por encerrar o programa quando não quiser mais utilizar, quebrando assim o loop.
