# Tarea 3 - Procesamiento de Datos con Big Data

## Descripción de la solución

En este proyecto se implementa un sistema de procesamiento de datos utilizando herramientas del ecosistema Big Data, específicamente con Apache Spark y Apache Kafka.

Estas herramientas, desarrolla un procesamiento en batch mediante Apache Spark, donde se analizan datos simulados relacionados con accidentes de tránsito en Colombia. A través de estructuras tipo DataFrame, se realizan operaciones de agregación, filtrado y análisis estadístico que permiten identificar patrones como el número de accidentes por ciudad, promedio de heridos y comportamiento de los eventos en función del tipo de vehículo, fecha y hora.

De tal manera se implementa un sistema de procesamiento en tiempo real utilizando Apache Kafka y Spark Streaming, en el cual se simulan datos de sensores que son enviados de manera continua y procesados en tiempo real, permitiendo visualizar el flujo de datos y su análisis dinámico.

Este enfoque permite evidenciar el uso combinado de procesamiento batch y streaming, cumpliendo con los requerimientos de análisis de datos en entornos Big Data.

## Archivos del proyecto

- kafka_producer.py: Genera datos simulados (sensores) y los envía a Kafka.
- spark_streaming_consumer.py: Consume y procesa los datos en tiempo real utilizando Spark Streaming.
- tarea3.py: Realiza el procesamiento en batch utilizando Apache Spark para el análisis de accidentes de tránsito.

## Instrucciones de ejecución

Para ejecutar correctamente este proyecto se requiere un entorno previamente configurado con Apache Spark, Apache Kafka y sistema operativo Linux.

1. Iniciar el servicio de ZooKeeper.
2. Iniciar el servidor de Kafka.
3. Ejecutar el archivo kafka_producer.py para generar los datos en tiempo real.
4. Ejecutar el archivo spark_streaming_consumer.py para procesar los datos en streaming.
5. Ejecutar el archivo tarea3.py para realizar el análisis en batch con Apache Spark.

Nota: Este proyecto fue ejecutado en una máquina virtual configurada con las herramientas mencionadas, por lo que su funcionamiento depende de dicho entorno.

## Tecnologías utilizadas

- Apache Spark
- Apache Kafka
- Python
- Linux
