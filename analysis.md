# Análise de Algoritmos e Estruturas — TaskManagerPy

## Operações principais
- Inserção de tarefa: descrição, complexidade (O(1) no banco), justificativa.
- Listagem: O(n).
- Busca por título: linear O(n); usando índice/dicionário O(1).
- Ordenação por prioridade: QuickSort (implementado) — melhor/caso médio/pior: O(n log n)/O(n log n)/O(n^2).

## Estruturas usadas
- Tabela SQL (tasks) — vantagens.
- Array/lista retornada pelo ORM — usada para QuickSort.
- Dicionário (opcional) para indexação em memória.

## Recorrências (se aplicável)
- QuickSort: T(n) = T(k) + T(n-k-1) + Theta(n) ... (resolver)

## Conclusão
(sua reflexão)
