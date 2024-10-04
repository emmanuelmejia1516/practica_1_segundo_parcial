# Programa 4: Solicitar calificacion por cada materia y mostrarla.

# Se utiliza la misma lista de materias que en el Programa 2.
materias = ["Pensamiento matematico", "lengua y comunicacion", "Ingles", "ecosistemas", "humanidades", "metodologias de software"]
calificaciones = []

# Se recorre la lista de materias y se solicita la calificacion para cada una.
for materia in materias:
    calificacion = input(f"Introduce la calificacion para {materia}: ")
    calificaciones.append(calificacion)  # Se almacena la calificacion en la lista.

# Se muestran las calificaciones en pantalla.
for materia, calificacion in zip(materias, calificaciones):
    print(f"En {materia} has obtenido {calificacion}")
