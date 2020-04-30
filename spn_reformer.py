def reform(toponym_spn):
    a = abs(int(float(toponym_spn['lowerCorner'].split()[0])) - int(float(toponym_spn['upperCorner'].split()[0])))
    b = abs(int(float(toponym_spn['lowerCorner'].split()[1])) - int(float(toponym_spn['upperCorner'].split()[1])))
    return a, b
