
# Análise Inicial
---

## Distribuição das Variáveis

**Idade:** A distribuição da idade é quase uniforme, com um aumento suave na frequência de pessoas perto dos 60.

**Renda Anual:** Faixas de renda específicas são o padrão para maioria dos clientes ($30.000, $50.000, $70.000 e $100.000).

**Tempo no Site:** Essa variável parece apresentar algumas inconsistências. A distribuição é variada, e a apresentação de alguns outliers (valores negativos ou muito baixos) denunciam as inconsistências.

**Gênero:** Equilibrado entre masculino e feminino.

**Anúncio Clicado:** Divisão clara entre quem clicou e quem não clicou nos anúncios.

**Compra (0 ou 1):** Essa é a variável alvo e está balanceada, com proporção razoável entre compradores e não compradores.

## Relações Entre Variáveis e a Variável Alvo (Compra)

### Idade vs Compra:
* Indivíduos mais jovens (18–30 anos) e mais velhos (50–60 anos) tendem a ter a maior probabilidade de realizar compras.
* Faixas intermediárias (30–50 anos) têm menos probabilidade de comprarem e apresentam a menor taxa de conversão.

### Renda Anual vs Compra:
* Indivíduos com maior poder aquisitivo (próximas a $100.000), tem maior probabilidade de comprar.
* As pessoas com rendas mais baixas ($30.000), na verdade também têm uma taxa significativa de conversão.

### Tempo no Site vs Compra:
* Indivíduos que demoram mais no site (20–30 minutos) tendem a realizar mais compras.
* Há valores negativos ou muito baixos nesta variavel, pode indicar possíveis inconsistências nos dados.

### Anúncio Clicado vs Compra:
* Quem clicou em anúncios está evidentemente mais inclinado a realizar uma compra do que aqueles que não clicaram, isso sugere que os anúncios são eficazes para converter usuários.

## Problemas Identificados nos Dados
* Tem valores ausentes em várias colunas, como Idade, Renda Anual, Tempo no Site e Gênero.
* Há inconsistências nos dados
* Valores negativos na coluna Tempo no Site são invalidos e não podem permanecer precisam ser tratados ou removidos.
* Registros com valores ausentes devem ser tratados (remoção ou imputação).


# Análise e sugestões após o resultado dos modelos
---

## Conclusões e Recomendações

### Conclusões
* Aqueles usuários que passam mais tempo no site e que possuem uma renda mais alta, são os que possuem a maior probabilidade de compra.
* Os anúncios são bons e os usuários que clicam neles estão fortemente inclinados a realizarem uma compra.
* O Random Forest apresentou um desempenho levemente superior no geral e também ofereceu insights mais claros do que a árvore de decisão, como entender que as variáveis tempo no site e idade são bastante importantes, diferente do modelo da árvore em que apenas considerou tempo no site como variável importante e praticamente ignorou anúncio clicado.

### Recomendações
* Investir em anúncios direcionados a usuários com perfis de mais alta renda.
* Melhorar a experiência no site para aumentar o tempo de permanencia dentro dele.
* Criar campanhas de marketing focadas em faixas etárias intermediárias (30-50) para melhorar a conversão nessa faixa.
* Também criar campanhas focadas em indivíduos mais velhos (50-60) e mais jovens (18-30) pois ambas as faixas têm boa taxa de  conversão.

### Próximos Passos que faria
* Refinaria o modelo utilizando otimização de hiperparâmetros.
* Realizar análises adicionais, assim, identificando outros padrões de comportamento e coletando mais dados.
* Implementar as recomendações e medir o impacto nas vendas futuras.
* Testar outros modelos que possam melhor performar.