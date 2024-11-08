class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, transitions, initial_state, accept_state, reject_state):
        # Inicializa los atributos de la máquina de Turing
        self.states = states  # Lista de estados
        self.input_alphabet = input_alphabet  # Alfabeto de entrada
        self.tape_alphabet = tape_alphabet  # Alfabeto de la cinta
        self.transitions = transitions  # Diccionario de transiciones
        self.current_state = initial_state  # Estado inicial
        self.accept_state = accept_state  # Estado de aceptación
        self.reject_state = reject_state  # Estado de rechazo
        self.tape = []  # Cinta de la máquina
        self.head_position = 0  # Posición del cabezal en la cinta
        self.configurations_seen = {}  # Configuraciones vistas para detección de bucles
        self.underscore_count = 0  # Contador de símbolos de subrayado

    def load_tape(self, input_string):
        # Carga la cinta con la cadena de entrada y añade 10 símbolos de subrayado al final
        self.tape = list(input_string) + ['_'] * 10

    def step(self):
        # Realiza un paso de la máquina de Turing
        if self.head_position >= len(self.tape):
            self.tape.append('_')  # Añade un símbolo de subrayado si el cabezal está fuera de la cinta

        current_symbol = self.tape[self.head_position]  # Obtiene el símbolo actual en la posición del cabezal
        current_config = self.get_configuration()  # Obtiene la configuración actual de la cinta

        if current_symbol == '_':
            self.underscore_count += 1  # Incrementa el contador de subrayados
            if self.underscore_count > 5:
                return "Loop"  # Detecta un bucle si hay más de 5 subrayados consecutivos

        if current_config in self.configurations_seen:
            self.configurations_seen[current_config] += 1  # Incrementa el contador de la configuración actual
            if self.configurations_seen[current_config] >= self.loop_detection_threshold:
                return "Loop"  # Detecta un bucle si la configuración se ha visto demasiadas veces
        else:
            self.configurations_seen[current_config] = 1  # Añade la configuración actual a las vistas

        if (self.current_state, current_symbol) in self.transitions:
            # Si hay una transición definida para el estado y símbolo actuales
            next_state, write_symbol, move_dir = self.transitions[(self.current_state, current_symbol)]
            self.tape[self.head_position] = write_symbol  # Escribe el nuevo símbolo en la cinta
            self.current_state = next_state  # Cambia al siguiente estado
            if move_dir == 'R':
                self.head_position += 1  # Mueve el cabezal a la derecha
            elif move_dir == 'L' and self.head_position > 0:
                self.head_position -= 1  # Mueve el cabezal a la izquierda

        return None

    def get_configuration(self):
        # Obtiene una representación de la configuración actual de la cinta
        tape_copy = self.tape[:]  # Copia la cinta
        tape_copy[self.head_position] = f"{self.current_state}"  # Marca la posición del cabezal con el estado actual
        return ' |'.join(tape_copy)  # Devuelve la configuración como una cadena

    def run(self, input_string):
        # Ejecuta la máquina de Turing con la cadena de entrada
        self.load_tape(input_string)  # Carga la cinta
        configurations = []  # Lista para almacenar las configuraciones vistas
        while self.current_state not in [self.accept_state, self.reject_state]:
            result = self.step()  # Realiza un paso
            if result == "Loop":
                return configurations, "Loop"  # Devuelve "Loop" si se detecta un bucle
            configurations.append(self.get_configuration())  # Añade la configuración actual a la lista
            if self.current_state in [self.accept_state, self.reject_state]:
                break  # Termina si se alcanza un estado de aceptación o rechazo
        return configurations, "Accepted" if self.current_state == self.accept_state else "Rejected"  # Devuelve el resultado final

def parse_machine_specification(filepath):
    # Parsea el archivo de especificación de la máquina de Turing
    with open(filepath, 'r') as file:
        lines = file.readlines()  # Lee todas las líneas del archivo
    
    machine_specs = {}
    section = None
    for line in lines:
        line = line.strip()
        if line.startswith('#'):
            section = line[1:].strip().lower().replace(' ', '_')  # Identifica la sección actual
            machine_specs[section] = []
        elif line and section:
            machine_specs[section].append(line)  # Añade la línea a la sección correspondiente
    
    states = machine_specs['states'][0].split(',')  # Parsea los estados
    input_alphabet = machine_specs['input_alphabet'][0].split(',')  # Parsea el alfabeto de entrada
    tape_alphabet = machine_specs['tape_alphabet'][0].split(',')  # Parsea el alfabeto de la cinta
    initial_state = machine_specs['initial_state'][0]  # Parsea el estado inicial
    accept_state = machine_specs['accept_state'][0]  # Parsea el estado de aceptación
    reject_state = machine_specs['reject_state'][0]  # Parsea el estado de rechazo
    transitions = {tuple(transition.split('->')[0].split(',')): tuple(transition.split('->')[1].split(',')) 
                   for transition in machine_specs['transitions']}  # Parsea las transiciones
    input_string = machine_specs['input_string'][0] if 'input_string' in machine_specs and machine_specs['input_string'] else ''  # Parsea la cadena de entrada y verifica si está vacía

    return TuringMachine(states, input_alphabet, tape_alphabet, transitions, initial_state, accept_state, reject_state), input_string  # Devuelve la máquina de Turing y la cadena de entrada

def main():
    # Función principal
    tm, input_string = parse_machine_specification('machine_spec.txt')  # Parsea la especificación de la máquina
    configurations, result = tm.run(input_string)  # Ejecuta la máquina de Turing
    with open('output.txt', 'w') as file:
        file.write("Config:\n")
        file.write("\n".join(configurations) + "\n")  # Escribe las configuraciones en el archivo de salida
        file.write(f"Cadena: {result}\n")  # Escribe el resultado final en el archivo de salida

if __name__ == "__main__":
    main()  # Ejecuta la función principal si el script se ejecuta directamente
