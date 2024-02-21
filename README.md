# Laboratorio 0

## areaTrapecio(B, b, h)
Hacer una función llamado areaTrapecio que contenga 3 parámetros de entrada (B, b, h), los tres valores deben ser Enteros y mayores a CERO. 
Deben de calcular el área de un trapecio, para ellos es aplicar la siguiente fórmula
![image](https://github.com/Taller-a-la-Programacion/2022-S1-Laboratorio-0/assets/1167750/a3e0aa1c-fcae-4fc8-84ed-25e18609f79b)

```python
>>> areaTrapecio(10, 5, 5)
37.5
```
## grupoPoblacion(edad)
Implemente una función llamada grupoPoblacion(edad) que retorne el grupo de población que pertenece una persona según su edad.
Tomar en cuenta que:
-	El rango de edades va de 0 a 125
-	Debe ser entero positivo
-	Si el rango de edad es de 0 a 10 su grupo de población es ‘Niños’
-	Si el rango de edad es mayor a 10 a 18 su grupo de población es ‘Adolescentes’
-	Si el rango de edad es mayor de 18 a 50 su grupo de población es ‘Adultos’
-	Si el rango de edad es mayor de 50 a 125 su grupo de población es ‘Ancianos’
-	Si es mayor a 125, retornar el mensaje “Es una edad poco probable, favor consultar”
-	Si es negativo devolver el mensaje respectivo a valores entre 0 a 125

```python
>>>grupoPoblacion(15)
"Adolescentes"
>>>grupoPoblacion(5)
"Niños"
>>>grupoPoblacion(-5)
"Error: El valor debe ser desde 0 hasta 125"
>>>grupoPoblacion(155)
"Error: Es una edad poco probable, favor consultar"
```
## sonImpares(num)
Implemente una función llamada sonImpares(num) que reciba como argumentos un número entero positivo mayor a cero. La función debe retornar **True** si todos los dígitos que lo compone son Impares y **False** si almenos uno de ellos es par

```python
>>> sonImpares (1357)
True
>>> sonImpares (4131) 
False

```
