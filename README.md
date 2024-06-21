### Creador de contraseñas y Caso de Tabla de Decisión

- Interaccion con el usuario de contraseñas, con los parametros de :tw-2714:
1.la contraseña debe estar entre 8 y 10 caracteres.
2.Tiene que tener 2 letras.
3.tiene que tener una letra en mayuscula.
4.tiene que tener un letra en minuscula.
5.tiene que tener 1 caracter de numero.
6.tiene que tener 1 caracter especial.

-Con casos de uso, que se testeo con el comando de cobertura de coverage.:tw-2714:
1. si supero el limite de 10 caracteres.
2. si es menor de 8 caracteres.
3. si esta entre 8 y 10 caracteres.
4. verificar si existe letras mayuscula.
5. verificar si existe alguna letra.
6.verificar que exista un caracter.
7.verificar que exista un numero.
8. verificar que exista letra minuscula.
9. verificar que cumpla todas las condiciones.


# Proyecto de Validación de Hipotecas

Este proyecto implementa una función de validación de hipotecas basada en varios criterios, como la edad del solicitante, sus ingresos mensuales, el precio de la propiedad, la antigüedad en el empleo

## Estructura del Proyecto

El proyecto consiste en dos funciones principales:

1. `validar_hipoteca`: Esta función evalúa si una solicitud de hipoteca es aprobada o rechazada según los criterios especificados.
2. `prueba_caja_negra_hipotecas`: Esta función realiza pruebas de caja negra utilizando varios casos de prueba y muestra los resultados en formato tabular.

## Comandos que vimos para el tema de los testeo en el test_contrase.py

- COVERAGE RUN TEST_CONTRASE.PY:tw-270f:
###Para los reportes este comando.
- COVERAGE REPORT -M:tw-270f:
###Para visualizarlo en html.
- COVERAGE HTML:tw-270f:
