## Análise inicial

### **1. Distribuição das Variáveis**
- **Idade**: A distribuição da idade é aproximadamente uniforme, com um leve aumento na frequência para pessoas próximas a 60 anos.
- **Renda Anual**: A maioria dos indivíduos está concentrada em faixas de renda específicas (como $30.000, $50.000, $70.000 e $100.000).
- **Tempo no Site**: A variável apresenta uma distribuição variada, com alguns outliers (valores negativos ou muito baixos) que podem indicar inconsistências nos dados.
- **Gênero**: O dataset parece equilibrado entre os gêneros masculino e feminino.
- **Anúncio Clicado**: Há uma divisão clara entre quem clicou e quem não clicou nos anúncios.
- **Compra (0 ou 1)**: A variável alvo está balanceada, com uma proporção razoável entre compradores e não compradores.

---

### **2. Relações Entre Variáveis e a Variável Alvo (`Compra`)**
- **Idade vs Compra**:
  - Indivíduos mais jovens (18–30 anos) e mais velhos (50–60 anos) têm maior probabilidade de realizar compras.
  - Faixas intermediárias (30–50 anos) apresentam menor taxa de conversão.
  
- **Renda Anual vs Compra**:
  - Indivíduos com rendas mais altas (próximas a $100.000) têm maior probabilidade de realizar compras.
  - Pessoas com rendas mais baixas ($30.000) também têm uma taxa significativa de conversão.

- **Tempo no Site vs Compra**:
  - Indivíduos que passam mais tempo no site (20–30 minutos) tendem a realizar mais compras.
  - Valores negativos ou muito baixos nesta variável indicam possíveis inconsistências nos dados.

- **Anúncio Clicado vs Compra**:
  - Quem clicou em anúncios tem maior probabilidade de realizar uma compra, sugerindo que os anúncios são eficazes para converter usuários.

---

### **3. Problemas Identificados nos Dados**
- Existem valores ausentes em várias colunas, como `Idade`, `Renda Anual`, `Tempo no Site` e `Gênero`.
- Há inconsistências nos dados:
  - Valores negativos na coluna `Tempo no Site` são inválidos e precisam ser corrigidos ou removidos.
  - Registros com valores ausentes devem ser tratados (remoção ou imputação).

---
---

## Análise e sugestões após o resultado dos modelos 


### **Conclusões e Recomendações**
- **Conclusões**:
  - Usuários com mais tempo no site e renda mais alta têm maior probabilidade de comprar.
  - Cliques em anúncios estão fortemente correlacionados com compras.
  - O Random Forest apresentou melhor desempenho geral, mas a árvore de decisão oferece insights claros e interpretáveis.

- **Recomendações**:
  - Investir em anúncios direcionados para usuários com perfis de alta renda.
  - Melhorar a experiência no site para aumentar o tempo de permanência.
  - Criar campanhas de marketing focadas em faixas etárias intermediárias (25-40 anos).

---

### 6. **Próximos Passos**
1. Refinar o modelo utilizando otimização de hiperparâmetros.
2. Realizar análises adicionais para identificar outros padrões de comportamento.
3. Implementar as recomendações e medir o impacto nas vendas futuras.


---


