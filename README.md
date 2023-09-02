# cotacao-moedas
Esse é um projeto de cotação de moedas e conversão (dólar, euro e real), além da flutuação diária de cada uma delas. 
Foi feito através da biblioteca requests do python e também utilizando a Awesome API para solicitar as informações atualizadas em tempo real. 
Foi utilizado o datetime para pegar a data atual no momento que roda o código, mostrando ao usuário que a cotação está atualizada.

Além da cotação, é possível fazer a conversão de uma moeda para a outra, no valor especificado pelo usuário. 
O programa funciona com tratamento de erros, ou seja, se o usuário digitar valores string onde são solicitados números,
ou escolher opções que não existam, o programa informará que houve erro e será solicitado novamente até que seja 
digitado da forma correta. Além disso, o usuário pode optar por encerrar o programa quando não quiser mais utilizar,
quebrando assim o loop.

Foram adicionadas novas funcionalidades para entrada de valores com vírgula, além da exibição de valores também com vírgulas, tornando mais próximo do formato de moedas no Brasil.

A seguir, uma demonstração de como o programa funciona...

Cotação de moeda:

![cotação de moeda](https://github.com/daniel-antunes-da-silva/cotacao-moedas/assets/132831685/6df0e83b-6570-438f-967a-e061e695972d)


Conversão de moeda: 

![conversão de moeda](https://github.com/daniel-antunes-da-silva/cotacao-moedas/assets/132831685/ee630c7d-083e-4a47-9199-b419eb9a972d)
