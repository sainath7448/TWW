def knapSack(W, wt, val, n):
	if n == 0 or W == 0:
		return 0
	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))

val = [20,5,10,40,15,25]
wt = [1,2,3,8,7,4]
W = 10
n = len(val)
print("K_NUMBER:",knapSack(W, wt, val, n)) 

