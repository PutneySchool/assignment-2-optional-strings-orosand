def unique(w):
	count = 0
	if (len(w) == 1):
		return True
	while (count<len(w)):
		count2 = count
		count = count+1
		for x in range(0,len(w)):
			if (search(w,x)==True):
				x = x+1
			else:
				return False
		return True
def search(str,n):
	count = n+1
	while (count<len(str)):
		if (str[count] == str[n]):
			return False
		else:
			count = count + 1
	return True
print(unique('gfkyutfck'))