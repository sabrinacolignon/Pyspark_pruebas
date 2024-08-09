import pandas as pd
import numpy as np
import random
from faker import Faker
import csv

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

fake = Faker()

departments = [101, 102, 103, 104, 105]

with open('./data/employees.csv', 'w', newline='') as csvfile:
    fieldnames = ['employee_id', 'name', 'age', 'gender', 'department_id', 'monthly_salary', 'birth_date']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for i in range(1, num_rows + 1):
        writer.writerow({
            'employee_id': i,
            'name': fake.name(),
            'age': random.randint(18, 65),
            'gender': random.choice(['M', 'F']),
            'department_id': random.choice(departments),
            'monthly_salary': random.randint(2000, 8000),
            'birth_date': fake.date_of_birth(minimum_age=18, maximum_age=65).strftime('%Y-%m-%d')
        })

# Define the number of departments you want to generate
departments = [
    (101, 'IT'),
    (102, 'Sales'),
    (103, 'Engineering'),
    (104, 'Marketing'),
    (105, 'HR')
]

with open('./data/departments.csv', 'w', newline='') as csvfile:
    fieldnames = ['id', 'department_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for dept in departments:
        writer.writerow({
            'id': dept[0],
            'department_name': dept[1]
        })

# Guardar el DataFrame en un archivo CSV
csv_path = './data/people_data.csv'
df.to_csv(csv_path, index=False)

# Guardar el DataFrame en un archivo JSON
json_path = './data/people_data.json'
df.to_json(json_path, orient='records', lines=True)

# Generar datos de ejemplo
data = {
    'id': np.arange(1, num_rows + 1),
    'name': np.random.choice(['Alice', 'Bob', 'Charlie', 'David'], num_rows),
    'age': np.random.randint(20, 60, num_rows),
    'city': np.random.choice(['New York', 'Los Angeles', 'Chicago', 'Houston'], num_rows),
    'salary': np.random.randint(30000, 100000, num_rows)
}

df = pd.DataFrame(data)

# Guardar en formato CSV
df.to_csv('./data/data.csv', index=False)

# Guardar en formato Parquet
df.to_parquet('./data/data.parquet', index=False)

(csv_path, json_path)