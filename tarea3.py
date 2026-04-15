from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum, avg, desc

# Crear sesión de Spark
spark = SparkSession.builder \
    .appName("AnalisisTransitoColombia") \
    .getOrCreate()

# Datos simulados de tránsito
data = [
    ("Bogotá", "Cundinamarca", "2024-05-10", "08:30", "Moto", 120, 95, 12),
    ("Medellín", "Antioquia", "2024-06-12", "14:20", "Carro", 85, 70, 8),
    ("Cali", "Valle", "2024-07-15", "22:10", "Moto", 78, 60, 10),
    ("Barranquilla", "Atlántico", "2024-08-01", "18:45", "Carro", 52, 41, 5),
    ("Cartagena", "Bolívar", "2024-09-05", "11:00", "Moto", 47, 36, 4),
    ("Bucaramanga", "Santander", "2024-10-10", "07:15", "Carro", 39, 28, 3),
    ("Bogotá", "Cundinamarca", "2025-01-12", "09:00", "Moto", 132, 101, 14),
    ("Medellín", "Antioquia", "2025-02-20", "16:30", "Carro", 90, 74, 9),
    ("Cali", "Valle", "2025-03-18", "20:40", "Moto", 81, 63, 11),
    ("Barranquilla", "Atlántico", "2025-04-22", "13:10", "Carro", 58, 46, 6)
]

columns = ["Ciudad", "Departamento", "Fecha", "Hora", "Tipo_Vehiculo", "Accidentes", "Heridos", "Fallecidos"]

# Crear DataFrame
df = spark.createDataFrame(data, columns)

print("\n=== DATOS DE TRÁNSITO ===")
df.show()

print("\n=== TOTAL DE ACCIDENTES POR CIUDAD ===")
df.groupBy("Ciudad") \
    .agg(sum("Accidentes").alias("Total_Accidentes")) \
    .orderBy(desc("Total_Accidentes")) \
    .show()

print("\n=== PROMEDIO DE HERIDOS POR TIPO DE VEHÍCULO ===")
df.groupBy("Tipo_Vehiculo") \
    .agg(avg("Heridos").alias("Promedio_Heridos")) \
    .show()

print("\n=== TOTAL DE FALLECIDOS POR AÑO ===")
df.groupBy("Fecha") \
    .agg(sum("Fallecidos").alias("Total_Fallecidos")) \
    .show()

print("\n=== ACCIDENTES EN HORAS PICO (DESPUÉS DE 18:00) ===")
df.filter(col("Hora") > "18:00").show()

# Cerrar Spark
spark.stop()