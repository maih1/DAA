def Min(a, b):
	return min(a, b)

def minPalindrom(strs, n):

	table = [[0 for i in range(n)]
				for i in range(n)]
	l, h, gap = 0, 0, 0

	for gap in range(1, n):
		l = 0
		for h in range(gap, n):
			if strs[l] == strs[h]:
				table[l][h] = table[l + 1][h - 1]
			else:
				table[l][h] = (Min(table[l][h - 1],
								table[l + 1][h]) + 1)
			l += 1

	return table[0][n - 1];

if __name__ == '__main__':
	strs = "ab"
	res = minPalindrom(strs, len(strs))
	print('So ky tu can them nho nhat:', res)