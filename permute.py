def permute(str1,str2):
	a = sorted(str1)
	b = sorted(str2)
	if a == b:
		return True
	else:
		return False
print permute('bos','ssb')