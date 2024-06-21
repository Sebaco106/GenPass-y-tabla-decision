def validar_hipoteca(edad, ingresos_mensuales, precio_propiedad, antiguedad_empleo, dti, puntaje_credito):
    if edad < 18:
        return "Rechazado por edad"
    elif ingresos_mensuales < 3000:
        return "Rechazado por ingresos bajos"
    elif precio_propiedad > 500000:
        return "Rechazado por precio alto"
    elif antiguedad_empleo < 1:
        return "Rechazado por falta de antigüedad laboral"
    elif dti > 0.4:
        return "Rechazado por alta relación deuda-ingresos"
    elif puntaje_credito < 600:
        return "Rechazado por puntaje de crédito bajo"
    else:
        return "Aprobado"

def prueba_caja_negra_hipotecas():
    pruebas = [
        (25, 4000, 450000, 2, 0.3, 700),      # Caso 1: Aprobado
        (30, 2500, 300000, 0, 0.5, 550),     # Caso 2: Rechazado por ingresos bajos y dti alto
        (20, 5000, 600000, 1, 0.4, 680),     # Caso 3: Rechazado por precio alto y dti justo al límite
        (35, 6000, 400000, 0, 0.2, 720),     # Caso 4: Aprobado con excelente perfil
        (18, 2000, 350000, 0, 0.4, 580),     # Caso 5: Rechazado por edad y dti alto
        (28, 3500, 550000, 0, 0.3, 650),     # Caso 6: Rechazado por precio alto
        (40, 7000, 480000, 3, 0.25, 750),    # Caso 7: Aprobado con excelente perfil
    ]
    
    resultados = []
    
    for i, (edad, ingresos, precio, antiguedad, dti, puntaje) in enumerate(pruebas, 1):
        resultado = validar_hipoteca(edad, ingresos, precio, antiguedad, dti, puntaje)
        resultados.append({
            "Caso": i,
            "Edad": edad,
            "Ingresos Mensuales": ingresos,
            "Precio de la Propiedad": precio,
            "Antigüedad en el Empleo": antiguedad,
            "DTI": dti,
            "Puntaje de Crédito": puntaje,
            "Salida Obtenida": resultado
        })
    
    # Imprimir resultados en forma de tabla
    print("{:<5} {:<5} {:<20} {:<20} {:<25} {:<10} {:<15} {:<15}".format(
        "Caso", "Edad", "Ingresos Mensuales", "Precio de la Propiedad", "Antigüedad en el Empleo", "DTI", "Puntaje de Crédito", "Resultado"))
    print("-" * 105)
    for resultado in resultados:
        print("{:<5} {:<5} ${:<19,} ${:<19,} {:<24} {:<9.2f} {:<14} {:<15}".format(
            resultado["Caso"], resultado["Edad"], resultado["Ingresos Mensuales"], resultado["Precio de la Propiedad"],
            f"{resultado['Antigüedad en el Empleo']} años", resultado["DTI"], resultado["Puntaje de Crédito"], resultado["Salida Obtenida"]))
    
# Ejemplo de uso mejorado
prueba_caja_negra_hipotecas()
