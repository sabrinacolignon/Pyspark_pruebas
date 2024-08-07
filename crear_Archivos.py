import pandas as pd
import numpy as np
import random

nombres_argentinos = {
    'Masculino': ['Juan', 'Carlos', 'José', 'Pedro', 'Luis', 'Miguel', 'Gabriel', 'Santiago',
                 'Diego', 'Marcos', 'Fernando', 'Alejandro', 'Gustavo', 'Daniel', 'Marcelo',
                 'Javier', 'Roberto', 'Eduardo', 'Ricardo', 'Jorge', 'Andrés', 'Martín',
                 'Pablo', 'Gonzalo', 'Facundo', 'Agustín', 'Nicolás', 'Lucas', 'Mateo'],
    'Femenino': ['María', 'Ana', 'Laura', 'Carla', 'Sofía', 'Julia', 'Mónica', 'Silvana',
                 'Natalia', 'Gabriela', 'Andrea', 'Mariana', 'Verónica', 'Patricia',
                 'Elizabeth', 'Claudia', 'Susana', 'Beatriz', 'Mercedes', 'Lorena',
                 'Daniela', 'Vanesa', 'Romina', 'Florencia', 'Camila', 'Sol', 'Ailén',
                 'Martina', 'Luciana']
}

def generar_nombre(genero):
  """Genera un nombre aleatorio según el género."""
  return random.choice(nombres_argentinos[genero])

def generar_nombres(num_rows):
  """Genera una lista de nombres aleatorios."""
  nombres = []
  for _ in range(num_rows):
    genero = random.choice(['Masculino', 'Femenino'])
    nombre = generar_nombre(genero)
    nombres.append(nombre)
  return nombres


# Generar un DataFrame con más de 100,000 filas
num_rows = 100000
data = {
    'Name': generar_nombres(num_rows),
    'Age': np.random.randint(18, 80, size=num_rows),
    'Gender': np.random.choice(['Male', 'Female'], size=num_rows),
    'Height': np.random.uniform(150, 200, size=num_rows),  # Altura en cm
    'Weight': np.random.uniform(50, 100, size=num_rows)   # Peso en kg
}

df = pd.DataFrame(data)

# Guardar el DataFrame en un archivo CSV
csv_path = './data/people_data.csv'
df.to_csv(csv_path, index=False)

# Guardar el DataFrame en un archivo JSON
json_path = './data/people_data.json'
df.to_json(json_path, orient='records', lines=True)

(csv_path, json_path)