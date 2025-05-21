#!/usr/bin/env python
"""mapper.py"""

# Leemos el archivo
import sys

# Archivo de entrada
file_hdfs = open("mensaje.txt", "r", encoding="utf-8")
# Archivo de salida
output_file = open("salida_mapper.txt", "w", encoding="utf-8")

# Procesamos línea por línea
for line in file_hdfs:
    line = line.strip()
    words = line.split()
    for word in words:
        output_file.write(f"{word}\t1\n")

file_hdfs.close()
output_file.close()
print("Mapper terminado. Resultado guardado en salida_mapper.txt.")
