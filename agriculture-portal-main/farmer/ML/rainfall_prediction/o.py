cat = [2,1,2,4,5,3,12]
price = [3,2,4]

cat.sort()
price.sort()

print(cat,price)
res = 0 
min_len = min(len(cat),len(price))
val = 0 
for i in range(0,min_len):
	val = cat[len(cat)-i-1] * price[len(price)-i-1]
	res += val
print(res)