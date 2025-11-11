from functools import lru_cache
import json

# Carrega o catálogo de cursos a partir do JSON
with open("courses_reskilling_1.json", "r") as file:
    catalog = json.load(file)

# Listas separadas para impactos (valores) e horas (pesos) de cada curso
CoursesImpact = [i['impact'] for i in catalog]
CoursesHours = [i['hours'] for i in catalog]


def memoization(values, weights, capacity):
    # Verifica se os tamanhos das listas estão corretos
    n = len(values)
    if len(weights) != n:
        exit("Erro: o tamanho de values deve ser o mesmo que o de weights.")

    # Programação dinâmica com memoização (Top-Down)
    @lru_cache(maxsize=None)
    def best(i, cap):
        # Caso base: sem itens restantes ou capacidade esgotada
        if i == n or cap <= 0:
            return 0

        # Opção: não pegar o item i
        res = best(i + 1, cap)

        # Opção: pegar o item i (se couber na mochila)
        if weights[i] <= cap:
            take = values[i] + best(i + 1, cap - weights[i])
            # Escolhe a melhor das duas opções
            if take > res:
                res = take
        return res

    # Obtém o melhor valor possível com a capacidade total
    max_value = best(0, capacity)

    # Reconstrução dos itens escolhidos (trazendo a solução)
    selected = []
    cap = capacity
    for i in range(n):
        if cap <= 0:
            break

        # Valor sem pegar o item atual
        without_i = best(i + 1, cap)
        # Valor pegando o item atual (se possível)
        if weights[i] <= cap:
            with_i = values[i] + best(i + 1, cap - weights[i])
        else:
            with_i = -1

        # Se pegar for melhor → item selecionado
        if with_i >= 0 and with_i > without_i:
            selected.append(i)
            cap -= weights[i]

    return max_value, selected


def tabulation(values, weights, capacity):
    n = len(values)
    if len(weights) != n:
        exit("Erro: o tamanho de values deve ser o mesmo que o de weights.")

    # Criação da tabela dp para programação dinâmica (Bottom-Up)
    # dp[i][w] = melhor valor com primeiros i itens e capacidade w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # Preenchimento da tabela
    for i in range(1, n + 1):
        vi = values[i - 1]
        wi = weights[i - 1]
        for w in range(capacity + 1):
            # Não pegar o item
            dp[i][w] = dp[i - 1][w]
            # Tentar pegar o item (se couber)
            if wi <= w:
                val_with = vi + dp[i - 1][w - wi]
                if val_with > dp[i][w]:
                    dp[i][w] = val_with

    max_value = dp[n][capacity]

    # Reconstrução dos itens da solução
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        # Se o valor mudou, significa que o item foi incluído
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)
            w -= weights[i - 1]
            if w <= 0:
                break

    selected.reverse()
    return max_value, selected


def listCourses():
    # Lista todos os cursos do catálogo
    for i in catalog:
        print(f"{str(i['id']) + ' ' if i['id'] < 10 else i['id']} "
              f"{i['name']} ({i['hours']}h) - Impacto: {i['impact']}")


def listSelectedCourses(selected):
    # Lista apenas cursos selecionados pelo algoritmo
    res = []
    for i in catalog:
        for j in selected:
            # Ajuste: os índices começam do 0
            if i['id'] == j + 1:
                res.append(i)
                print(f"{str(i['id']) + ' ' if i['id'] < 10 else i['id']} "
                      f"{i['name']} ({i['hours']}h) - Impacto: {i['impact']}")
    return res


def main():
    status = 1
    while status != 0:
        # Menu principal
        print("\n1 - Listar cursos\n2 - Calcular melhores cursos\n0 - Sair\n")
        menuInput = int(input("Selecione: "))

        match menuInput:
            case 1:
                # Exibe todo o catálogo
                listCourses()

            case 2:
                statusCourses = 1

                # Entrada da capacidade do usuário
                AvalibleTime = int(
                    input("Informe o seu tempo disponível (horas): "))

                # 1️⃣ Algoritmo com memoização
                print("\nMemoização: ")
                maxMemo, selecMemo = memoization(
                    CoursesImpact, CoursesHours, AvalibleTime)
                print(f"Valor máximo: {maxMemo}")
                bestCourses = listSelectedCourses(selecMemo)

                # 2️⃣ Algoritmo com tabulação
                print("\nTabulação: ")
                maxTabu, selecTabu = tabulation(
                    CoursesImpact, CoursesHours, AvalibleTime)
                print(f"Valor máximo: {maxTabu}")
                listSelectedCourses(selecTabu)

                # Checagem de consistência das soluções
                if selecTabu == selecMemo and maxMemo == maxTabu:
                    print(
                        "\nVerificação: As duas abordagens retornaram a mesma solução.")

                # Submenu: permite ver mais detalhes dos cursos escolhidos
                while statusCourses != 0:
                    print("\nCursos disponíveis: ")
                    for i in bestCourses:
                        print(f"{str(i['id']) + ' ' if i['id']
                              < 10 else i['id']} - {i['name']}")
                    print("0 - Sair\n")

                    statusCourses = int(
                        input("Selecione o curso que deseja conhecer: "))
                    match statusCourses:
                        case 0:
                            break
                        case _:
                            found = False
                            for i in bestCourses:
                                # Se o ID digitado existir, mostra informações completas
                                if i['id'] == statusCourses:
                                    print(f"id: {i['id']}\nnome: {i['name']}\nhoras: {i['hours']}\nimpacto: {i['impact']}"
                                          f"\ncategoria: {i['category']}\ndescrição: {
                                              i['description']}"
                                          f"\npré-requisitos: {i['prerequisites']}\n")
                                    found = True
                            if not found:
                                print("Digite um ID de curso válido!")

            case 0:
                break

            case _:
                print("Opção inválida!")


# Execução principal do programa
if __name__ == "__main__":
    main()
