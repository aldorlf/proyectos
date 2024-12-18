def obtener_numero_estudiantes():
    """Pide al usuario el número de estudiantes y valida que sea un entero positivo."""
    while True:
        try:
            num = int(input("Ingresa el número de estudiantes: "))
            if num > 0:
                return num
            else:
                print("Por favor, ingresa un número mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def obtener_nombre_estudiante():
    """Pide al usuario el nombre del estudiante."""
    while True:
        nombre = input("Ingresa el nombre del estudiante: ").strip()
        if nombre:
            return nombre
        else:
            print("El nombre no puede estar vacío. Inténtalo de nuevo.")

def obtener_numero_asignaturas():
    """Pide al usuario el número de asignaturas y valida que sea un entero positivo."""
    while True:
        try:
            num = int(input("Ingresa el número de asignaturas: "))
            if num > 0:
                return num
            else:
                print("Por favor, ingresa un número mayor que cero.")
        except ValueError:
            print("Entrada no válida. Por favor, ingresa un número entero.")

def obtener_calificaciones(num_asignaturas):
    """
    Pide al usuario el nombre y la calificación para cada asignatura.
    Devuelve una lista de tuplas con (nombre_asignatura, calificación).
    """
    calificaciones = []
    for i in range(num_asignaturas):
        while True:
            nombre_asignatura = input(f"Ingresa el nombre de la asignatura {i + 1}: ").strip()
            if not nombre_asignatura:
                print("El nombre de la asignatura no puede estar vacío.")
                continue

            try:
                calificacion = float(input(f"Ingrese la calificación para {nombre_asignatura}: "))
                if 0 <= calificacion <= 10:
                    calificaciones.append((nombre_asignatura, calificacion))
                    break
                else:
                    print("La calificación debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número.")
    return calificaciones

def calcular_promedio(calificaciones):
    """Calcula y devuelve el promedio de las calificaciones."""
    return sum(cal[1] for cal in calificaciones) / len(calificaciones)

def determinar_estado(promedio):
    """Determina si el estudiante ha aprobado o reprobado basándose en el promedio."""
    return "Aprobado" if promedio >= 6.0 else "Reprobado"

def imprimir_resumen(estudiantes):
    """Imprime un resumen con el nombre de los estudiantes, sus asignaturas, calificaciones, promedio y estado."""
    print("\nResumen de calificaciones:")
    print("-" * 40)
    for estudiante in estudiantes:
        print(f"Nombre: {estudiante['nombre']}")
        print(f"Promedio: {estudiante['promedio']:.2f}")
        print(f"Estado: {estudiante['estado']}")
    print("-" * 40)

# Programa principal
def main():
    num_estudiantes = obtener_numero_estudiantes()
    estudiantes = []

    for _ in range(num_estudiantes):
        nombre = obtener_nombre_estudiante()
        num_asignaturas = obtener_numero_asignaturas()
        calificaciones = obtener_calificaciones(num_asignaturas)
        promedio = calcular_promedio(calificaciones)
        estado = determinar_estado(promedio)

        estudiantes.append({
            'nombre': nombre,
            'calificaciones': calificaciones,
            'promedio': promedio,
            'estado': estado
        })

    imprimir_resumen(estudiantes)

# Ejecutar el programa principal
if __name__ == "__main__":
    main()