# 🧠 TaskManagerPy — Análise de Algoritmos e Estruturas de Dados  
**Autor:** João Victor Santos  
**Data:** 12/11/2025  

---

## 1️ Introdução

O **TaskManagerPy** é uma aplicação web desenvolvida em **Python (Flask)** com o objetivo de gerenciar tarefas pessoais, permitindo **criar, listar, editar e excluir tarefas** (operações CRUD).  
Além das operações básicas, o sistema realiza **análises estatísticas e cálculos agregados** sobre as tarefas, aplicando conceitos de **algoritmos, estruturas de dados e complexidade computacional** estudados na disciplina *Algoritmos e Complexidades em Aplicações Web/Mobile*.

A aplicação foi hospedada na plataforma **Railway**, utilizando **SQLite** como banco de dados relacional.

---

##  Estruturas de Dados Utilizadas

| Estrutura | Uso no Projeto | Justificativa |
|------------|----------------|----------------|
| **Lista (`list`)** | Armazena as tarefas retornadas do banco antes da ordenação e análise. | Permite percorrer elementos de forma sequencial e aplicar algoritmos de ordenação e busca. |
| **Dicionário (`dict`)** | Utilizado para conversões e manipulações rápidas de dados (ex: `to_dict()`). | Estrutura de acesso rápido com complexidade média **O(1)**. |
| **Banco de Dados SQLite** | Persistência das tarefas e suas propriedades (título, status, prioridade, data). | Estrutura relacional leve e eficiente para CRUD local. |

---

## 3️ Algoritmos Implementados

### 🌀 a) QuickSort (Ordenação por Prioridade)

Foi implementado o algoritmo **QuickSort** para ordenar as tarefas de acordo com sua prioridade (`high > medium > low`).

#### Código:
```python
def quicksort_tasks(tasks, key_func):
    if len(tasks) <= 1:
        return tasks
    pivot = tasks[len(tasks)//2]
    pivot_key = key_func(pivot)
    left = [t for t in tasks if key_func(t) > pivot_key]
    middle = [t for t in tasks if key_func(t) == pivot_key]
    right = [t for t in tasks if key_func(t) < pivot_key]
    return quicksort_tasks(left, key_func) + middle + quicksort_tasks(right, key_func)
    Complexidade:
    Caso	Custo
    Melhor caso	O(n log n)
    Caso médio	O(n log n)
    Pior caso	O(n²)

    O QuickSort foi escolhido por ser eficiente na prática, simples de implementar recursivamente e aplicar diretamente sobre listas Python.

    🔍 b) Busca Linear (Localizar tarefas por ID)

    A busca linear é usada implicitamente ao editar, excluir ou atualizar tarefas.
    O algoritmo percorre a lista até encontrar o item correspondente.

    Complexidade:

    O(n) no pior caso.

    ➕ c) Cálculos Estatísticos e Agregações

    O sistema realiza cálculos agregados e estatísticos para gerar indicadores de produtividade e eficiência.

    Métricas calculadas:

    Total de tarefas

    Quantidade e porcentagem de tarefas concluídas

    Média de prioridade (conversão: low = 1, medium = 2, high = 3)

    Agrupamento de tarefas por data (GROUP BY no SQLAlchemy)

    Complexidade:

    Contagem e média: O(n)

    Agrupamento SQL: O(n) (ou O(log n) com índices)

    Esses cálculos são apresentados de forma visual na rota /stats, utilizando Chart.js para exibir gráficos interativos.

     Equação de Recorrência (QuickSort)

    Para o caso médio:

    T(n) = 2T(n/2) + Θ(n)


    Aplicando o Teorema Mestre:

    T(n) = Θ(n log n)

     Tabela de Complexidades Gerais
    Operação	Estrutura	Algoritmo	Complexidade
    Criar tarefa	Banco/Lista	Inserção	O(1)
    Listar tarefas	Lista	Iteração	O(n)
    Editar tarefa	Banco	Busca + Update	O(n)
    Excluir tarefa	Banco	Busca + Delete	O(n)
    Ordenar tarefas	Lista	QuickSort	O(n log n)
    Calcular estatísticas	Lista	Agregação	O(n)
    Agrupar por data	SQL	GROUP BY	O(n)
     Visualização e Interpretação dos Dados

    Na rota /stats, os dados são processados e exibidos de forma visual:

    Tabela de métricas gerais

    Gráfico de barras (Chart.js) mostrando o número de tarefas criadas por dia

    Isso demonstra a aplicação de agregações, visualização de dados e análise estatística — pontos exigidos pelo roteiro da disciplina.

    Conclusão

    O projeto TaskManagerPy integra teoria e prática de forma eficiente, demonstrando:

    Aplicação de algoritmos clássicos (QuickSort, busca linear);

    Uso de estruturas de dados fundamentais (listas, dicionários);

    Cálculos estatísticos e análise de complexidade;

    Integração com tecnologias web (Flask, SQLite, Chart.js);

    Implantação em ambiente real (Railway).

    