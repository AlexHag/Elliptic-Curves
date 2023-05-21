# Elliptic Curves
An elliptic curve is defined as
$$y^2 = x^3 + ax + b$$
where $a, b \in K$ and $4a^3 + 27b^3 \neq 0$ or $-16(4a^3 + 27b^3) \neq 0$. It has an abelian group structure
$$E(K)=\{(x,y)\in K\times K:y^2=x^3+ax+b\} \cup  \mathcal{O}$$
$K$ is a finite field $\mathbb{F}_p$ where $p$ is a prime number with $p > 3$. $\mathcal{O}$ Can be thought of as the point at infinity.

## Elliptic curve addition algorithm
Let $E$ be an elliptic curve over $\mathbb{F_p}$. Given two points $P,Q \in E$ compute the third point $R = P + Q \in E$.
Elliptic curve addition is done by taking two points, drawing a line through the two point and calculating a third point where the line intersects the elliptic curve and reflecting it over the $x$-axis.
1. If $P = \mathcal{O}$ set $R = Q$ or if $Q = \mathcal{O}$ set $R=P$ and return $R$.
2. If $P_x = Q_x$ and $P_y=-Q_y$ set $R=\mathcal{O}$ and return $R$.
3. Otherwise, if $P \neq Q$ define $\lambda$ by 

$$
\lambda= \frac{Q_y-P_y}{Q_x-P_x}
$$

Github is acting up here and won't show the correct equation. Look at the raw readme if this doesn't make sense.

Else if $P = Q$, then $\lambda$ will be the tangent line of the point

$$
\lambda= \frac{3P_x^2+a}{2P_y} \; \text{ if } \; P = Q
$$

and let
$$x=\lambda ^2 - P_x - Q_x \quad \text{and} \quad y=\lambda(P_x-x)-P_y$$
Then $P+Q=(x,y)=R \in E$.

<b>Inverse modulos</b>

Because $E$ is defined over a finite field $\mathbb{F_p}$ division in the traditional sense is not possible and should instead be done by multiplying with the modular inverse.

Ferma's little theorem tells us that if $p \in \mathbb{N}$ is prime and $x\in\mathbb{N}$ is such that $(x,y)=1$ then $x^{p-1} \equiv 1$ mod $p$.

Collary if $p\in\mathbb{N}$ is prime and $x\in\mathbb{N}$ is such that $(x,y)\equiv 1$ then the mod $p$ inverse of $x$ is
$$x^{-1}\equiv x^{p-1} \quad \text{mod} p$$

```python
def inverse_modp(x, p):
	if x % p == 0:
		return None
	return pow(x, p - 2, p)
```

## Elliptic curve multiplication algorithm
Elliptic curve multiplication can be thought of as repeatedly adding a point with itself $k$ times. The naive aproach would be
```python
def multiply_point(k, P):
	Q = INF_POINT
	for i in range(k):
		Q = add_points(Q, P)
	return Q
```
However if $k$ is large this becomes computationally impossible. Thus we can improve it with

<b>The double and add algorithm</b>

Write $k$ in its binary form
$$k=\sum_{i=0}^{m}b_i2^{i} \quad \text{where} b_i \in \{0,1\}$$
Then because of the associativity of the group operation
$$kP=\sum_{i=0}^{m}b_i2^{i}P$$
Define
$$x_i=2^iP\quad\text{for}i\geq 0$$
We have then
$$kP=\sum_{i=0}^{m}b_ix_i$$
Since $b_i\in\{0,1\}$ we can write this as
$$kP=\sum \{i:b_i=1\}x_i$$
In python
```python
def multiply_point(k, P):
	X = P
	Q = INF_POINT
	if k == 0:
		return INF_POINT
	while k != 0:
		if k & 1 != 0:
			Q = addition(Q, X)
		X = addition(X, X)
		k >>= 1
	return Q
```
