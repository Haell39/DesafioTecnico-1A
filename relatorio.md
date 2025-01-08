# Relatório de Resultados - Modelo de Classificação com Árvore de Decisão

## Introdução
O objetivo foi construir um modelo de classificação para prever se um cliente realizará uma compra, com base em variáveis fornecidas no dataset. Para isso, utilizamos um modelo de Árvore de Decisão. Este relatório apresenta a interpretação dos resultados, as variáveis mais influentes no modelo e sugestões de melhorias.

---

## Desempenho do Modelo

### Métricas de Avaliação
- **Acurácia**: 65%
- **Matriz de Confusão**:

  |              | Previsto: 0 | Previsto: 1 |
  |--------------|-------------|-------------|
  | **Real: 0** |      22     |      2      |
  | **Real: 1** |      12     |      4      |

- **Relatório de Classificação**:

```
              precision    recall  f1-score   support

           0       0.65      0.92      0.76        24
           1       0.67      0.25      0.36        16

    accuracy                           0.65        40
   macro avg       0.66      0.58      0.56        40
weighted avg       0.65      0.65      0.60        40
```

O modelo apresentou um desempenho moderado, com boa precisão para a Classe 0, mas dificuldade em identificar corretamente a Classe 1.

---

## Importância das Variáveis

A seguir, as variáveis mais relevantes para o modelo:

| Variável            | Importância |
|----------------------|-------------|
| Tempo_scaled         | 0.40        |
| Renda_scaled         | 0.30        |
| Idade_scaled         | 0.20        |
| Genero_encoded       | 0.06        |
| Anuncio_encoded      | 0.04        |

A visualização abaixo reflete o impacto de cada variável no modelo:

![Gráfico de Importância das Variáveis](#)

As variáveis **Tempo no Site** e **Renda Anual** foram as mais influentes no modelo, indicando que são bons preditores para a tomada de decisão.

---

## Propostas de Melhoria

1. **Ajuste de Hiperparâmetros**:
   - Experimentar diferentes valores de `max_depth`, `min_samples_split` e `min_samples_leaf` para reduzir o overfitting ou underfitting.
   - Realizar validação cruzada para selecionar os melhores parâmetros.

2. **Engenharia de Features**:
   - Criar novas variáveis derivadas, como interações entre `Renda` e `Tempo no Site`.
   - Explorar a possibilidade de categorizar a variável `Renda Anual` para identificar grupos mais específicos.

3. **Coleta de Mais Dados**:
   - Um dataset maior e mais balanceado pode ajudar a melhorar o desempenho e a generalização do modelo.

4. **Exploração de Outros Modelos**:
   - Avaliar modelos como Random Forest ou Gradient Boosting, que podem capturar relações mais complexas entre as variáveis.

5. **Normalização Avançada**:
   - Testar técnicas de normalização diferentes, como `RobustScaler`, para lidar com outliers presentes no dataset.

---

## Conclusão
O modelo de Árvore de Decisão apresentou um desempenho moderado, com acurácia de 65%. As variáveis mais influentes foram **Tempo no Site** e **Renda Anual**. As sugestões de melhoria incluem ajustes nos hiperparâmetros, engenharia de features e teste de modelos mais robustos.

Com esses ajustes, espera-se melhorar a precisão e a capacidade preditiva do modelo, tornando-o mais útil para aplicações reais.

