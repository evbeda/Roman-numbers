def roman(numero):
    if numero < 1:
        return "Can't convert to roman number!"

    if numero > 3999:
        return "Not a valid number"

    if not isinstance(numero, int):
        return "Only int numbers"
    numeros = {
        1000 :'M',
        900 :'CM',
        500 :'D',
        400 :'CD',
        100 :'C',
        90 : 'XC',
        50 : 'L',
        40 : 'XL',
        10: 'X',
        9 : 'IX',
        5 : 'V',
        4 : 'IV',
        1 : 'I',
    }
    roman = ''

    for key in sorted(numeros.keys(), reverse=True):
        value = numeros[key]
        if numero >= key:
            cant = numero // key
            roman += value * cant
            numero -= cant * key
    return roman