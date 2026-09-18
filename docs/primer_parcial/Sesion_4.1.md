# Sesión 4 - Control de motores CC
## 2026/09/11
## Mauro Guzmán Morales
# Sesión 4 - Motores CC
## Qué deberíamos lograr hoy

Identificar el funcionamiento de los motores CC, además de conocer sus características básicas y, por último, lograr realizar una simulación de un circuito básico.

* **Objetivo:**
Configurar y controlar motores de corriente continua mediante Arduino y el controlador L293D, comprendiendo su funcionamiento y la forma en que permiten controlar el movimiento de un vehículo.

---

## Qué usamos

* Arduino UNO
* Controlador L293D
* Motores CC
* Servomotores
* Computadora

---

## Qué hice y qué pasó

En este primer circuito se buscó controlar el movimiento de los motores e identificar la dirección en la que giraban.

![Diagrama del sistema](../recursos/imgs/Motor_CC.jpeg)

### Código de la primera imagen

```cpp
void setup()
{
  pinMode(7, OUTPUT); // declaramos el pin 7 como salida
  pinMode(4, OUTPUT); // declaramos el pin 4 como salida
}

void secuencia() // función que realiza la secuencia de movimiento del motor
{
  digitalWrite(7, HIGH);
  digitalWrite(4, LOW);
  delay(5000);

  digitalWrite(7, LOW);
  digitalWrite(4, LOW);
  delay(2000);

  digitalWrite(7, LOW);
  digitalWrite(4, HIGH);
  delay(5000);

  digitalWrite(7, LOW);
  digitalWrite(4, LOW);
  delay(2000);
}

void loop()
{
  analogWrite(5, 255);
  secuencia();
}
```

Como segunda imagen, contamos con un circuito compuesto por dos motores CC y un servomotor. Los motores cuentan con funciones para ir hacia adelante y hacia atrás, además de girar hacia la derecha y hacia la izquierda. De igual manera, el servomotor realiza giros en diferentes ángulos: 0°, 90° y 180°.

![Diagrama del sistema](../recursos/imgs/Motores_servo.jpeg)

### Código del segundo circuito

```cpp
// C++ code

#include <Servo.h>

Servo MGM;

void adelante()
{
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(10, HIGH);
  digitalWrite(9, LOW);
}

void atras()
{
  digitalWrite(7, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
}

void der()
{
  digitalWrite(6, HIGH);
  digitalWrite(7, LOW);
  digitalWrite(9, HIGH);
  digitalWrite(10, LOW);
}

void izq()
{
  digitalWrite(7, HIGH);
  digitalWrite(6, LOW);
  digitalWrite(10, HIGH);
  digitalWrite(9, LOW);
}

void setup()
{
  // servo
  MGM.attach(8);

  pinMode(6, OUTPUT);
  pinMode(7, OUTPUT);
  pinMode(2, OUTPUT);
  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);
  pinMode(12, OUTPUT);

  digitalWrite(2, HIGH);
  digitalWrite(12, HIGH);
}

void loop()
{
  MGM.write(0);
  adelante();
  delay(1000);

  atras();
  delay(1000);

  MGM.write(90);
  der();
  delay(1000);

  MGM.write(180);
  izq();
  delay(1000);
}
```

---

## Qué falló y cómo se resolvió

Durante la realización de los circuitos no hubo casi errores, más que algunos errores de código en Arduino. Para solucionarlos, se fue modificando el código de acuerdo con los diferentes funcionamientos y necesidades de la práctica.

Estas modificaciones se realizaron bajo el apoyo y revisión del profesor, hasta conseguir que los motores realizaran los movimientos correspondientes y que el servomotor pudiera girar en los diferentes ángulos establecidos.

---
## Que aprendi 
En esta sesión aprendí a controlar motores de corriente continua utilizando Arduino y el controlador L293D (puente H). Comprendí cómo invertir el sentido de giro de los motores manipulando los estados lógicos (HIGH y LOW) en los pines de salida, lo cual es fundamental para lograr que un vehículo avance, retroceda o gire hacia los lados. Además, aprendí a integrar un servomotor usando la librería Servo.h, logrando posicionarlo en ángulos exactos (0°, 90° y 180°). Finalmente, mejoré mis habilidades de programación al estructurar el código mediante funciones para cada movimiento y reafirmé la importancia de depurar la lógica paso a paso con el apoyo del profesor hasta obtener el resultado deseado en la simulación.
