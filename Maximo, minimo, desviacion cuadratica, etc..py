contar = 0;
suma = 0;
maximo = 0;
cuadrado = 0;
sumacuadrados= 0;
desviacion = 0;
n = input("Introduce valor para ser procesado: ")
minimo = int(n);
while n != '0':
    contar+= 1;
    suma += int(n);
    if int(n) > maximo:
        maximo = int(n);
    if int(n) < minimo:
        minimo = int(n);
    cuadrado = (int(n))**2;
    sumacuadrados += cuadrado;

    
    n = input("Introduce valor para ser procesado: ")

desviacion = (((sumacuadrados)/contar)**(0.5))
print("Se han introducido %s valores." % (contar))
print("La suma total tiene un valor de: %s" % (suma))
print("La media total tiene un valor de: %s" % (suma/contar))
print("El valor maximo es: %s" % (maximo))
print("El valor minimo es: %s" % (minimo))
print("La desviacion cuadratica media es: %s" % (desviacion))

'''
Saludos =)
'''
