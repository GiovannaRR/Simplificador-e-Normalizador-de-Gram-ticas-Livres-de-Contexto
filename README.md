# Conversor de Gramática para Forma Normal de Chomsky

Este projeto implementa uma classe `Grammar` em Python que processa gramáticas formais, removendo produções inúteis, produções vazias e unitárias, e convertendo a gramática para a **Forma Normal de Chomsky (FNC)**.

## Funcionalidades

- **Remoção de Símbolos Inacessíveis**: Remove símbolos não alcançáveis a partir do símbolo inicial.
- **Remoção de Produções Vazias**: Substitui produções que levam à cadeia vazia `ε`.
- **Remoção de Produções Unitárias**: Elimina regras do tipo `A → B`, onde `B` é um não terminal.
- **Conversão para Forma Normal de Chomsky**: Modifica a gramática para garantir que todas as regras estejam no formato exigido pela FNC.

## Sobre o Projeto

O código recebe um conjunto de produções de uma gramática e executa transformações para torná-la compatível com a Forma Normal de Chomsky.

### Exemplo de Uso

```python
# Definição das produções
productions = {
    'S': {'aAa', 'bBv'},
    'A': {'a', 'aA'}
}

# Criação do objeto Grammar
grammar = Grammar(productions)

# Aplicação das transformações
grammar.remove_unreachable_symbols()
print("Após remover símbolos inacessíveis:")
print(grammar)

grammar.remove_empty_productions()
print("Após remover produções vazias:")
print(grammar)

grammar.remove_unit_productions()
print("Após remover produções unitárias:")
print(grammar)

grammar.to_chomsky_normal_form()
print("Forma Normal de Chomsky:")
print(grammar)
```

## Estrutura das Transformações

### 1. **Remoção de Símbolos Inacessíveis**
- Inicia a partir do símbolo `S` e marca os símbolos acessíveis.
- Remove regras que contenham símbolos inacessíveis.

### 2. **Remoção de Produções Vazias**
- Identifica símbolos anuláveis (`A → ε`).
- Substitui suas ocorrências nas produções restantes.

### 3. **Remoção de Produções Unitárias**
- Substitui produções do tipo `A → B`, onde `B` é um não terminal, pelas produções de `B`.

### 4. **Conversão para Forma Normal de Chomsky**
- Cria um novo símbolo inicial `S0`.
- Garante que todas as regras tenham no máximo dois símbolos no lado direito.


## Possíveis Melhorias Futuras
- Implementar conversão para **Forma Normal de Greibach**.
- Adicionar suporte para análise e transformação de gramáticas ambíguas.
- Melhorar a detecção de recursão à esquerda para eliminá-la corretamente.

---

