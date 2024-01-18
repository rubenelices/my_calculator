### MULTIPLOS ###
def pedir_numeros():
    print("Escriba 3 numeros crecientes \n Le indicare si son multiplos entre ellos")
    num1 = int(input("El primer número es: "))
    num2 = int(input("El segundo numero es: "))

    if num1 >= num2:
        print("Por favor que los numeros vayan creciendo")
        num2 = int(input("El segundo numero es: "))
    num3 = int(input("El tercer numero es: "))

    if num2 >= num3:
        print("Por favor que los numeros vayan creciendo")
        num3 = int(input("El tercer numero es: "))
    
    if num3 % num2 == 0:
        print("El",num3,"es multiplo de",num2)

    if num2 % num1 == 0:
        print("El",num2,"es multiplo de",num1)
    
    if num3 % num1 == 0:
        print("El",num3,"es multiplo de",num1)

    else:
        print("Estos numeros no son multiplos entre ellos")
    
if __name__=="__main__":
    pedir_numeros()