# python3.5
# -*- coding: utf-8 -*-
# 杨辉三角
def triangles(num=10):
	Ln = []
	n = 0
	while n < num:
		i = 0
		Lm = []
		Lm.insert(0, 1)
		Lm.insert(-1, 1)
		for e in Ln:
			i = i + 1
			if i == len(Ln) and len(Ln) == 1:
				yield Ln
			elif i == len(Ln):
				continue
			s = Ln[i - 1] + Ln[i]
			Lm.insert(i, s)
		n = n + 1
		Ln = Lm.copy()
		yield Lm


g = triangles()

for t in g:
	print(t)
