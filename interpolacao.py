"""Interpolação polinomial: Lagrange e Newton (diferenças divididas).

Exercício: encontrar p de grau <= 2 com p(-1) = -32, p(2) = 1, p(4) = 3.
"""
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

x = np.array([-1.0, 2.0, 4.0])
y = np.array([-32.0, 1.0, 3.0])


def diferencas_divididas(x, y):
    """Devolve os coeficientes c0, c1, ..., cn-1 da forma de Newton."""
    n = len(x)
    tabela = np.zeros((n, n))
    tabela[:, 0] = y
    for j in range(1, n):
        for i in range(n - j):
            tabela[i, j] = (tabela[i + 1, j - 1] - tabela[i, j - 1]) / (x[i + j] - x[i])
    return tabela[0, :]


def newton(x, c, t):
    """Avalia o polinômio de Newton em t (forma encadeada)."""
    resultado = c[-1]
    for k in range(len(c) - 2, -1, -1):
        resultado = c[k] + (t - x[k]) * resultado
    return resultado


def lagrange(x, y, t):
    """Avalia o polinômio de Lagrange em t."""
    total = 0.0
    for i in range(len(x)):
        L = 1.0
        for j in range(len(x)):
            if j != i:
                L *= (t - x[j]) / (x[i] - x[j])
        total += y[i] * L
    return total


if __name__ == "__main__":
    c = diferencas_divididas(x, y)
    print("Coeficientes de Newton:", c)

    xs = np.linspace(-3, 6, 400)
    p_newton = np.array([newton(x, c, t) for t in xs])
    p_lagrange = np.array([lagrange(x, y, t) for t in xs])
    print("Maior diferença entre Newton e Lagrange:", np.max(np.abs(p_newton - p_lagrange)))

    fig, ax = plt.subplots(figsize=(8, 5))
    ax.plot(xs, p_newton, label=r"$p(x) = -2x^2 + 13x - 17$")
    ax.scatter(x, y, color="red", zorder=5, label="pontos dados")
    for xi, yi in zip(x, y):
        ax.annotate(f"({xi:g}, {yi:g})", (xi, yi), textcoords="offset points", xytext=(8, 8))
    ax.axhline(0, color="gray", lw=0.8)
    ax.axvline(0, color="gray", lw=0.8)
    ax.set_title("Interpolação polinomial de Newton e Lagrange")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    ax.grid(alpha=0.3)
    fig.savefig("interpolacao.png", dpi=200)
    print("Gráfico salvo em interpolacao.png")
