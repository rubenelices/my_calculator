class Estudiante:
    def __init__(self, nota: int):
        self.nota = nota
        
    #Función con la que se redondean las notas de los 4 alumnos.
    def notaEstudiantes(self):
        nota = self.nota

        #La nota solo se redondeará cuando sea mayor que 40.
        if nota >= 40:
            next_mult = ((nota // 5) + 1) * 5
            if (next_mult - nota) < 3:
                return next_mult 
            else:
                return nota
        else:
            return nota

print("Las notas de los estudiantes redondeadas son: ") 
"""
La nota del estdiante 1 se redondeará a 75 ya que es mayor que 40 y la diferencia hasta 
el siguiente multiplo de 5 es menor que 3
"""
Est1 = Estudiante(73)


"""
La nota del Estudiante 2 no se redondeará ya que pese a ser mayor que 40, la diferencia
hasta el siguiente múltiplo es mayor que 3
"""
Est2 = Estudiante(67)


"""
La nota del Estudiante 3 no se redondeará ya que es menor que 40 pese a que la diferencia 
hasta el siguiente múltiplo de 5 sea menor que 3
"""
Est3 = Estudiante(38)


"""
La nota del Estudiante 3 no se redondeará ya que es menor que 40 pese a que la diferencia 
hasta el siguiente múltiplo de 5 sea menor que 3
"""
Est4 = Estudiante(33)


"""
La nota del Estudiante 5 se redondeará ya que es mayor que 40 y la diferencia hasta el siguiente
múltiplo de 5 es menor que 3
"""
Est5 = Estudiante(43)


#Imprimo las notas redondeadas de los alumnos aplicando la función notaEstudiantes
print(Est1.notaEstudiantes())
print(Est2.notaEstudiantes())
print(Est3.notaEstudiantes())
print(Est4.notaEstudiantes())
print(Est5.notaEstudiantes())
    