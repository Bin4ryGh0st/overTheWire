# rot13 Caesar cipher

ciphered = 'Gur cnffjbeq vf 5Gr8L4qetPEsPk8htqjhRK8XSP6x2RHh'

deCiphered=""

for i in ciphered:
	ascii=ord(i)
	if 122>=ascii>=97:
		deCiphered+=chr(97+(ascii-97+13)%26)
	elif 90>=ascii>=65:
		deCiphered+=chr(65+(ascii-65+13)%26)
	else:
		deCiphered+=i
		
print(deCiphered)
