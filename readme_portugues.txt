1.Defina uma função principal chamada "sinal" que recebe um parâmetro "sinal" como entrada
podendo ser '+'para somar,'-'para subtrair,'/'para dividir,'*'para multiplicar.
2.Dentro da função "sinal", defina uma função aninhada chamada "calcular" que recebe dois parâmetros, "x" e "y".
3.Dentro da função "calcular", verifique o valor do parâmetro "sinal" passado para a função principal "sinal" e retorne o resultado da operação matemática correspondente entre "x" e "y" (por exemplo, "x-y" para "sinal" = "-"). Se o sinal passado não for reconhecido, retorne uma mensagem de erro.
4.Retorne a função "calcular" ao final da função "sinal".

Exemplo de uso:


sub = sinal("-")
resultado = sub(5,3)
print(resultado)  # Output: 2


Neste exemplo, criamos uma variável chamada "sub" ao chamar a função "sinal" com "-" como argumento. Então usamos a função retornada, "calcular" para realizar a operação de subtração com 5 e 3 e armazenamos o resultado na variável "resultado" e finalmente imprimimos o resultado.
