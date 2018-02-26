def roman(numero):
	if numero < 1:
		return None

	numeros = {'1': 'I', '4':'IV', '5' : 'V', '9':'IX', '10': 'X',
	 '40':'XL','50': 'L'}
	

	# if numero == 1 : 
	# 	return 'I' 
	# elif numero == 2 :
	# 	return 'X' 

	# elif numero == 10 :
	# 	return 'X' 
	# elif numero == 845 :
	# 	return 'DCCCXLV'
	# for x in numeros(1,10):
	# 	pass


	#for key, value in numeros.iteritems():
		#if  numero == 1:
		#	return 'I'
	if numero >= 1 and numero < 4:
		return numeros[str(1)] * numero

	if numero == 4:
		return numeros[str(4)]

	#if numero > 5 and numero < 9:







