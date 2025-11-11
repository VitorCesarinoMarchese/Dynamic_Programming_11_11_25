# Projeto: Otimização de Seleção de Cursos (Knapsack Problem)

Este projeto implementa algoritmos de Programação Dinâmica (Memoização e Tabulação) para selecionar os melhores cursos de acordo com o tempo disponível do usuário, maximizando a soma do impacto total.
O programa lê os dados de um catálogo em JSON e permite ao usuário interagir via menu no terminal.

## Integrantes do Grupo

Vitor Cesarino Marchese - RM 554893
Matheus Hisamoto de Souza - RM 555447
Ali Andrea Mamani Molle - RM 558052

## Vídeo de Apresentação

Link para o YouTube:
[https://youtu.be/WOJhAzwg6sw](https://youtu.be/WOJhAzwg6sw)

## Estrutura do Projeto

### main.py

Lógica principal da aplicação, interação com usuário e execução dos algoritmos

### courses_reskilling_1.json

Catálogo dos cursos com: id, nome, horas, impacto, descrição, pré-requisitos e categoria

## Funcionalidades Implementadas

- Listagem completa dos cursos
- Implementação do Knapsack Problem 0/1 com:
- Memoização (Top-Down)
- Tabulação (Bottom-Up)
- Seleção dos cursos com melhor impacto dentro da carga horária disponível
- Exibição de detalhes dos cursos escolhidos
- Verificação se ambas as implementações retornam a mesma solução
- Tratamento de erros básicos

## Execução do Programa

### Pré-requisitos

- Python 3.10+
- Arquivo `courses_reskilling_1.json` na mesma pasta que `main.py`

### Como executar

```bash
git clone https://github.com/VitorCesarinoMarchese/Dynamic_Programming_11_11_25.git
cd Dynamic_Programming_11_11_25
python3 main.py
```

## Como utilizar

Ao rodar o programa, o menu exibido será:

```bash
1 - Listar cursos
2 - Calcular melhores cursos
0 - Sair
```

Se escolher 2, será solicitado o tempo disponível em horas — o programa irá então:

1. Calcular os cursos com melhor impacto com Memoização
2. Calcular novamente com Tabulação
3. Mostrar os cursos sugeridos
4. Permitir explorar detalhes de cada um
