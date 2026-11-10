# Interpolação polinomial: Lagrange e Newton

Exercício: encontrar o polinômio p de grau no máximo 2 tal que
p(-1) = -32, p(2) = 1 e p(4) = 3.

Resposta: **p(x) = -2x² + 13x - 17**

## Conteúdo

- `interpolacao.py`: implementação de Newton (diferenças divididas) e de Lagrange, com gráfico.
- `interpolacao.png`: gráfico gerado pelo script.

## Como rodar

```bash
pip install -r requirements.txt
python interpolacao.py
```

## Resultado esperado

- Coeficientes de Newton: `[-32, 11, -2]`
- Diferença máxima entre Newton e Lagrange: da ordem de 1e-15 (os dois métodos dão o mesmo polinômio, pela unicidade).

## Verificação

- p(-1) = -32, p(2) = 1, p(4) = 3.
