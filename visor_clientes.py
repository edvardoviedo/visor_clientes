import pandas as pd

# Carga el CSV
df = pd.read_csv('clientes.csv')

# Mostrar las primeras 5 filas
print("Primeras filas:")
print(df.head())

# Estadísticas: edad promedio
if 'edad' in df.columns:
    edad_promedio = df['edad'].mean()
    print(f"\nEdad promedio: {edad_promedio:.2f} años")

# Total de suscritos
if 'suscrito' in df.columns:
    # Normaliza valores para contar
    df['suscrito'] = df['suscrito'].astype(str).str.lower().str.strip()
    total_suscritos = df['suscrito'].isin(['sí', 'si', 'true', '1']).sum()
    print(f"Total suscritos: {total_suscritos}")

# Limpieza simple: quitar espacios en columnas tipo texto
for col in df.select_dtypes(include='object').columns:
    df[col] = df[col].str.strip()

# Eliminar filas con datos faltantes
df_limpio = df.dropna()

print(f"\nFilas después de limpieza: {len(df_limpio)}")

# Puedes seguir aquí agregando más filtros o vistas

