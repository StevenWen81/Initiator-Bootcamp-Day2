string = input('Pesan rahasia: ')

i = 0
newString = ''
while i < len(string):
    if (string[i] == 'x'):
        newString += ' '
        i += 1
    elif (string[i] == '%'):
        newString += chr( int(string[i+1] + string[i+2]) + 96 )
        i += 3
    else:
        newString += chr( int(string[i]) + 96 )
        i += 1
                              
print('Arti pesan:', newString)
