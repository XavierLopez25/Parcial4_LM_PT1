# Parcial4_LM_PT1

Este programa simula una máquina de Turing. Una máquina de Turing es un modelo matemático de computación que define una máquina abstracta que manipula símbolos en una cinta de acuerdo con un conjunto de reglas. Este programa permite definir una máquina de Turing mediante un archivo de especificación y ejecutarla con una cadena de entrada.

## Instrucciones

### Archivo `machine_spec.txt`

El archivo `machine_spec.txt` debe contener la especificación de la máquina de Turing en el siguiente formato:

- **States**: Lista de estados separados por comas.
- **Input Alphabet**: Alfabeto de entrada separado por comas.
- **Tape Alphabet**: Alfabeto de la cinta separado por comas.
- **Initial State**: Estado inicial de la máquina.
- **Accept State**: Estado de aceptación de la máquina.
- **Reject State**: Estado de rechazo de la máquina.
- **Transitions**: Lista de transiciones en el formato `estado_actual,símbolo_lectura->estado_siguiente,símbolo_escritura,dirección_movimiento`.
- **Input String**: Cadena de entrada para la máquina de Turing.

Ejemplo de `machine_spec.txt`:

```plaintext
# States
q0,q1,q2,qaccept,qreject,qloop

# Input Alphabet
a,b

# Tape Alphabet
a,b,_

# Initial State
q0

# Accept State
qaccept

# Reject State
qreject

# Transitions
q0,a->q1,a,R
q0,b->qreject,b,R
q0,_->qreject,_,R
q1,a->qloop,a,R
q1,b->q0,b,R
q1,_->qaccept,_,R
qloop,a->qloop,a,R
qloop,b->qreject,b,R
qloop,_->qloop,_,R

# Input String
```

### Archivo `output.txt`

El archivo `output.txt` contiene el resultado de la ejecución de la máquina de Turing. Incluye las configuraciones de la cinta en cada paso y el resultado final (Accepted, Rejected o Loop).

Ejemplo de `output.txt`:

```plaintext
Config:
_ |qqreject |_ |_ |_ |_ |_ |_ |_ |_
Cadena: Rejected
```

## Ejecución

Para ejecutar el programa, simplemente ejecute el script `main.py`. El programa leerá la especificación de la máquina de Turing desde `machine_spec.txt`, ejecutará la máquina con la cadena de entrada especificada y escribirá el resultado en `output.txt`.

### Ejemplos

#### Ejemplo 1: Cadena `aaaaa` (Loop)

Archivo `machine_spec.txt`:

```plaintext
# States
q0,q1,q2,qaccept,qreject,qloop

# Input Alphabet
a,b

# Tape Alphabet
a,b,_

# Initial State
q0

# Accept State
qaccept

# Reject State
qreject

# Transitions
q0,a->q1,a,R
q0,b->qreject,b,R
q0,_->qreject,_,R
q1,a->qloop,a,R
q1,b->q0,b,R
q1,_->qaccept,_,R
qloop,a->qloop,a,R
qloop,b->qreject,b,R
qloop,_->qloop,_,R

# Input String
aaaaa
```

Archivo `output.txt`:

```plaintext
Config:
a |qloop a |a |a |a |a |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |qloop a |a |a |a |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |qloop a |a |a |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |a |qloop a |a |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |a |a |qloop a |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |a |a |a |qloop _ |_ |_ |_ |_ |_ |_ |_ |_ |_
Cadena: Loop
```

#### Ejemplo 2: Cadena `aaab` (Rejected)

Archivo `machine_spec.txt`:

```plaintext
# States
q0,q1,q2,qaccept,qreject,qloop

# Input Alphabet
a,b

# Tape Alphabet
a,b,_

# Initial State
q0

# Accept State
qaccept

# Reject State
qreject

# Transitions
q0,a->q1,a,R
q0,b->qreject,b,R
q0,_->qreject,_,R
q1,a->qloop,a,R
q1,b->q0,b,R
q1,_->qaccept,_,R
qloop,a->qloop,a,R
qloop,b->qreject,b,R
qloop,_->qloop,_,R

# Input String
aaab
```

Archivo `output.txt`:

```plaintext
Config:
a |q1 a |a |a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |qloop a |a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |qloop a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |a |a |qreject b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
Cadena: Rejected
```

#### Ejemplo 3: Cadena `ababab` (Accepted)

Archivo `machine_spec.txt`:

```plaintext
# States
q0,q1,q2,qaccept,qreject,qloop

# Input Alphabet
a,b

# Tape Alphabet
a,b,_

# Initial State
q0

# Accept State
qaccept

# Reject State
qreject

# Transitions
q0,a->q1,a,R
q0,b->qreject,b,R
q0,_->qreject,_,R
q1,a->qloop,a,R
q1,b->q0,b,R
q1,_->qaccept,_,R
qloop,a->qloop,a,R
qloop,b->qreject,b,R
qloop,_->qloop,_,R

# Input String
ababab
```

Archivo `output.txt`:

```plaintext
Config:
a |q1 b |a |b |a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |q0 b |b |a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
a |a |b |qreject b |a |b |_ |_ |_ |_ |_ |_ |_ |_ |_ |_
Cadena: Rejected
```
