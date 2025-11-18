# TaskManager  
**Gerenciador de Tarefas Web desenvolvido em Python (Flask)**  

---

## Sobre o Projeto

O **TaskManager** é uma aplicação web desenvolvida em **Python** com o framework **Flask**, criada para **gerenciar tarefas pessoais**.  
O sistema permite **criar, listar, editar e excluir tarefas**, além de **analisar estatísticas** e **gerar gráficos** sobre o progresso do usuário.

Este projeto foi desenvolvido como parte da disciplina **Algoritmos e Complexidades em Aplicações Web/Mobile**, aplicando conceitos de:
- Estruturas de Dados;
- Algoritmos de Ordenação (QuickSort);
- Análise de Complexidade Computacional;
- Cálculos Estatísticos e Agregações de Dados.

---

## Funcionalidades Principais

| Função | Descrição |
|---------|------------|
| ➕ Criar Tarefa | Adiciona novas tarefas com título, prioridade e status. |
| ✏️ Editar Tarefa | Permite alterar título, prioridade ou status. |
| ❌ Excluir Tarefa | Remove uma tarefa permanentemente. |
| 📋 Listar Tarefas | Exibe todas as tarefas armazenadas no banco. |
| ⚡ Ordenar Tarefas | Ordena tarefas por prioridade usando **QuickSort**. |
| 📊 Estatísticas | Mostra métricas como total de tarefas, concluídas e média de prioridade. |
| 📈 Gráfico Interativo | Exibe um gráfico de barras (Chart.js) com o número de tarefas criadas por dia. |

---

##  Algoritmos e Estruturas

O projeto implementa e analisa:

| Tipo | Algoritmo / Estrutura | Complexidade |
|------|-----------------------|---------------|
| Ordenação | QuickSort | O(n log n) |
| Busca | Linear Search | O(n) |
| Estrutura Linear | Lista / Dicionário | O(1) em acesso |
| Banco de Dados | SQLite (relacional) | O(log n) com índices |
| Agregações | COUNT, GROUP BY (SQL) | O(n) |

Mais detalhes sobre a análise teórica estão disponíveis no arquivo [`analysis.md`](./analysis.md).

---

## Tecnologias Utilizadas

- **Python 3.12+**
- **Flask** — framework web principal  
- **Flask-SQLAlchemy** — ORM para persistência de dados  
- **SQLite** — banco de dados leve embutido  
- **Bootstrap 5** — estilização responsiva da interface  
- **Chart.js** — geração de gráficos dinâmicos  
- **Railway** — deploy e hospedagem do sistema  

---

## Deploy Online

A aplicação está hospedada na **Railway** e pode ser acessada em:

👉 [https://taskmanagerpy-production.up.railway.app](https://taskmanagerpy-production.up.railway.app)

---

## 💻 Instalação Local

Caso deseje executar o projeto localmente, siga os passos abaixo:

```bash
# 1️⃣ Clone o repositório
git clone https://github.com/SANT0LA/taskmanagerpy.git
cd taskmanagerpy

# 2️⃣ Crie o ambiente virtual
python -m venv venv
venv\Scripts\activate   # (Windows)

# 3️⃣ Instale as dependências
pip install -r requirements.txt

# 4️⃣ Execute a aplicação
python app.py
Acesse no navegador:
👉 http://127.0.0.1:5000/

```

##  Análise de Algoritmos e Complexidade

O documento analysis.md
 apresenta:

Estruturas de dados utilizadas

Algoritmos aplicados

Cálculos de complexidade (O, Ω, Θ)

Equação de recorrência do QuickSort

Tabela comparativa das operações CRUD

##  Estrutura do Projeto
taskmanagerpy/
│
├── app.py                 # Arquivo principal Flask
├── models.py              # Modelos e estrutura de banco
├── routes.py              # Rotas do CRUD
├── requirements.txt       # Dependências do projeto
├── analysis.md            # Análise de algoritmos e complexidade
├── README.md              # Documentação principal
│
└── templates/             # Páginas HTML (interface)
    ├── base.html
    ├── index.html
    ├── edit.html
    └── stats.html
