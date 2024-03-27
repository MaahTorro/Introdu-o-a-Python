# Cálculos utulizados na linguagem

Adição, a + b, quando a e b são numéricos;

>>> 1 + 2
3
Concatenação, a + b, quando a e b são sequências;

>>> 'Anderson' + ' ' + 'Woss'
'Anderson Woss'
>>> [1, 2] + [3, 4]
[1, 2, 3, 4]
Contenção, a in b;

>>> 1 in [1, 2, 3, 4]
True
Divisão verdadeira, a / b, que retorna o resultado real;

>>> 5/2
2.5
Divisão com truncamento, a // b, que retorna apenas a parte inteira;

>>> 5//2
2
E binário, a & b;

>>> 1 & 3
1
OU exclusivo binário, a ^ b;

>>> 1 ^ 2
3
Inversão binária, ~a;

>>> ~2
-3
OU binário, a | b;

>>> 1 | 2
3
Exponenciação, a**b;

>>> 2**10
1024
Identidade, a is b;

>>> 1 is None
False
Identidade, a is not b;

>>> 1 is not None
True
Indexação, obj[k];

>>> obj = [1, 2, 3]
>>> obj[1]
2
Atribuição por índice, obj[k] = v;

>>> obj = [1, 2, 3]
>>> obj[2] = 4
>>> obj
[1, 2, 4]
Exclusão por índice, del obj[k];

>>> obj = [1, 2, 3]
>>> del obj[1]
>>> obj
[1, 3]
Deslocamento binário para esquerda, a << b;

>>> 4 << 1
8
Deslocamento binário para direita, a >> b;

>>> 4 >> 1
2
Resto de divisão, a % b;

>>> 5 % 2
1
Multiplicação, a * b;

>>> 2 * 3
6
Multiplicação de matriz, a @ b (versões 3.5+);

Ver PEP 465;

Negação aritmética, -a;

>>> -4
-4
Negação lógica, not a;

>>> not True
False
Positivo, +a;

>>> +4
4
Fatiamento, seq[i:j];

>>> obj = [1, 2, 3, 4, 5]
>>> obj[1:3]
[2, 3]
Atribuição por fatiamento, seq[i:j] = values;

>>> obj = [1, 2, 3, 4, 5]
>>> obj[1:3] = [8, 9]
>>> obj
[1, 8, 9, 4, 5]
Exclusão por fatiamento, del seq[i:j];

>>> obj = [1, 2, 3, 4, 5]
>>> del obj[1:3]
>>> obj
[1, 4, 5]
Formatação de string, s % obj (prefira método format ou f-strings);

>>> 'Olá, %s' % 'mundo'
'Olá, mundo'
Subtração, a - b;

>>> 3 - 1
2
Teste de verdade, if obj: ...;

>>> obj = 3
>>> if obj: print('Ok')
'Ok'
Menor que, a < b;

>>> 1 < 2
True
Menor ou igual a, a <= b;

>>> 1 <= 2
True
Maior que, a > b;

>>> 1 > 2
False
Maior ou igual a, a >= b;

>>> 1 >= 2
False
Entre, não inclusivo, a < v < b;

>>> v = 5
>>> 1 < v < 9
True
Entre, inclusivo, a <= v <= b;

>>> v = 5
>>> 1 <= v <= 9
True
Igualdade, a == b;

>>> 1 == 2
False
Diferença, a != b;

>>> 1 != 2
True
Diferença, a <> b (obsoleto a partir da versão 2.5, removido nas versões 3+);

>>> 1 <> 2
True
