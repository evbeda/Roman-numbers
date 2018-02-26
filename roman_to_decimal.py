
def decimal(roman):
    roma = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
    cadena = list(roman)
    result = 0
    count = 0
    a = ['A', 'B', 'E', 'F', 'G', 'H', 'J', 'K', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'W', 'Y', 'Z']
    if any(x in roman for x in a):
        result = 'Input is not a roman number'
    else:
        for letra in cadena:
            if len(cadena) != count + 1:
                if len(cadena) > 0:
                    if roma[letra] < roma[cadena[count+1]]:
                        result -= roma[letra]
                    else:
                        result += roma[letra]
                else:
                    result += roma[letra]
            else:
                result += roma[letra]
            count += 1
    return result

    
