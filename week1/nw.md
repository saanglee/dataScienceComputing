Representation
vector: [0, 1, 9, 4, 7, 2058264048272048237]
title -> 숫자 + thumb -> 숫자

Graph G
node input feature vector: X_A, X_B, … X_F
weight matrices W -> training을 통해 얻어내야 할 parameter
a: aggregator func -> pre-defined param - e.g. sum, min, max, avg, …
b: aggregation weight 집합
N: neighbor embedding vector 집합
z: output vector -> 예측값

```py
init:
- h0_A = X_A
- h0_B = X_B
- …
- h0_F = X_F

for K: -> 몇번 돌릴지. pre-defined param
k = 1
	A:
		h1_N(A) = a_1 (h0_B, h0_C, h0_D, b)
		h1_A = sigma(W1 * concat(h0_A, h1_N(A)))
	B:
		h1_N(B) = a_1 (h0_A, h0_C, b)
		h1_B = sigma(W1 * concat(h0_B, h1_N(B)))
	…
	F: …
k = 2
	A:
		h2_N(A) = a_2 (h1_B, h1_C, h1_D, b)
		h2_A = sigma(W2 * concat(h1_A, h2_N(A))
	…
	F: …
…
k = K
```
