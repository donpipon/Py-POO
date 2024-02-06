def verificar_calificacion(nota1, nota2, nota3):
    promedio = (nota1 + nota2 + nota3) / 3

    if promedio >= 6:
        return "Aprobado"
    else:
        return "Reprobado"

print(verificar_calificacion(6,2,10))



def verificar_calificacion_2(*notas):
    promedio = sum(notas) / len(notas)

    calificacion: str

    if promedio >= 6:
        calificacion = "Aprobado"
    else:
        calificacion = "Reprobado"

    return f'{calificacion} con promedio: {round(promedio,2)}'


print(verificar_calificacion_2(6,2,10))