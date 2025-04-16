# IA Problem Solving - UFAL

Atividade prática da disciplina **PPGI008 – Inteligência Artificial** do Programa de Pós-Graduação em Informática da Universidade Federal de Alagoas (UFAL), sob orientação dos professores **Evandro** e **Glauber**.

---

## Descrição

Este projeto resolve o problema de encontrar a **menor rota entre duas cidades** dos Estados Unidos, com base na distância euclidiana entre elas. A conexão entre as cidades é feita considerando um raio `r`, definido pelo usuário.

Foram implementados dois algoritmos de busca:
- **A\***: busca informada clássica (Capítulo 3 do livro).
- **Greedy Best-First Search**: algoritmo mais rápido, porém menos preciso.

---

## Relatório completo

A versão completa do relatório da atividade (com modelagem, explicações teóricas, tabelas, prints e análises comparativas) está disponível no link abaixo:

👉 [Clique aqui para acessar o relatório no Google Docs](https://docs.google.com/document/d/1CT6m4E5T1ENNdhKyNY-AE0WwUh7UqLh0GTlPKUREN3k/edit?usp=sharing)

---

## Modelagem do problema

### PEAS

| Elemento       | Descrição                                                                 |
|----------------|---------------------------------------------------------------------------|
| **P**erformance | Menor distância total do trajeto, com desempate por menor população       |
| **E**nvironment | Mapa das cidades dos EUA com conexões baseadas na distância euclidiana    |
| **A**ctuators   | Algoritmos de busca (A\*, Greedy)                                          |
| **S**ensors     | Distância entre cidades, população e posição atual                        |

### Abstração

- **Estados**: cada cidade representa um estado.
- **Ações**: mover-se de uma cidade para outra conectada.
- **Transições**: determinísticas.
- **Custo**: distância euclidiana entre as cidades.

---

## Cenários de teste

Três cenários foram definidos com base no arquivo `cities.json`:

| Cenário | Raio (r) | Cidade de Origem | Cidade de Destino | Deve ter solução? |
|---------|----------|------------------|--------------------|--------------------|
| A       | 300 km   | Dallas           | Austin             | ✅ Sim             |
| B       | 500 km   | New York         | Philadelphia       | ✅ Sim             |
| C       | 200 km   | New York         | Los Angeles        | ❌ Não             |

---

## Comparação dos algoritmos (dados reais)

| Cenário | Algoritmo | Caminho                      | Distância (km) | Tempo (s) |
|---------|-----------|------------------------------|----------------|-----------|
| A       | A\*       | Dallas → Austin              | 297.69         | 0.0000    |
| A       | Greedy    | Dallas → Austin              | 297.69         | 0.0000    |
| B       | A\*       | New York → Philadelphia      | 153.88         | 0.0000    |
| B       | Greedy    | New York → Philadelphia      | 153.88         | 0.0000    |
| C       | A\*       | NY → ... → Los Angeles       | 619.05         | 0.0025    |
| C       | Greedy    | NY → ... → Los Angeles       | 5962.81        | 0.0000    |

> ⚠️ No cenário C, o algoritmo Greedy foi mais rápido, mas encontrou um caminho significativamente menos eficiente do que o A\*.

---

## ⚙️ Execução

### Pré-requisitos

- Python 3.8+
- Arquivo `cities.json` no mesmo diretório do projeto
- Apenas bibliotecas padrão (`heapq`, `math`, `json`, etc.)

### Como executar

```bash
python ia_problem_solving.py
