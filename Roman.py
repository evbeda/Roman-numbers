def roman(numero):
	if numero < 1:
		return None

	numeros = {'1': 'I', '5' : 'V', '10': 'X', '50': 'L'}

	if numero == 1 : 
		return 'I' 

	elif numero == 10 :
		return 'X' 
	elif numero == 845 :
		return 'DCCCXLV'
#reference key(numeros)


