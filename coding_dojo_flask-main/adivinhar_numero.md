# Adivinhar o número

O jogo inicia com o sorteio aleatório de um número entre 1 e 100, mantido em segredo pelo computador.

O desafio para o jogador é fazer palpites sobre o número secreto. Após cada palpite, o sistema fornece dicas sobre a posição do palpite em relação ao número secreto, indicando se é "maior" ou "menor".

A iteração continua até o jogador acertar o número, concluindo o jogo com uma mensagem de parabéns.

## Tarefas

1. Precisamos começar gerando um número inteiro aleatório secreto:
   - Pesquise sobre o módulo `random` do Python e como importá-lo no arquivo `adivinhar_numero.py` (veja linha 2).
   - Procure por um comando que gere um número inteiro aleatório dentro do intervalo de 1 a 100 e atribua o resultado dele na variável `numero_secreto` (veja linha 8).
2. Para cada mudança que você fizer no código, tente jogar no navegador. Vamos à lógica do jogo:
   - A variável `palpite` sempre conterá o valor que o jogador digitar no formulário. Descubra o tipo dessa variável, exiba-o no terminal e depois faça sua conversão para o tipo correto (linha 15).
   - Use uma estrutura condicional para comparar `palpite` com `numero_secreto` (linha 18).
     - Se `palpite` for maior que `numero_secreto`, atribua o texto "Tente um número menor" à variável `mensagem`;
     - Se `palpite` for menor que ` numero_secreto`, atribua o texto "Tente um número maior" à variável `mensagem`;
     - Senão, atribua o texto "Parabéns!! Você acertou o número `numero_secreto`" à variável `mensagem`. No lugar de `numero_secreto` nessa mensagem, exiba o número em si.