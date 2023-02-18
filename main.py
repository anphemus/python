respuesta = 99999;
def mostrarMenu():
 print('| ------------------------------------------------ |');
 print('| ----------------------MENU---------------------- |');
 print('| 1 - SUMAR                                        |');
 print('| 2 - RESTAR                                       |');
 print('| 3 - MULTIPLICAR                                  |' );
 print('| 4 - DIVIDIR                                      |' );
 print('| 0 - SALIR                                        |' );
 print('| ------------------------------------------------ |');
 
while(respuesta != 0):
    mostrarMenu();
    respuesta = int(input('Qué quieres hacer: '));