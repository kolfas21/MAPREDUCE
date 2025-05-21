#!/usr/bin/env python
"""merger.py

Este script lee la salida ordenada de un mapper (salida_sorter.txt),
agrupa las palabras iguales y suma sus ocurrencias.
Guarda el resultado final en nueva_salida.txt.
"""

current_word = None
current_count = 0

# Abrimos el archivo de entrada (ordenado por palabra)
with open("salida_sorter.txt", "r", encoding="utf-8") as f, \
     open("nueva_salida.txt", "w", encoding="utf-8") as out:
    
    for line in f:
        line = line.strip()
        
        # Separar palabra y conteo
        try:
            word, count = line.split('\t', 1)
            count = int(count)
        except ValueError:
            continue  # Saltar líneas inválidas

        # Agrupar y acumular conteos
        if current_word == word:
            current_count += count
        else:
            if current_word:
                out.write(f"{current_word}\t{current_count}\n")
            current_word = word
            current_count = count

    # Escribir la última palabra
    if current_word == word:
        out.write(f"{current_word}\t{current_count}\n")

print("✅ Nueva salida agrupada guardada en 'nueva_salida.txt'")
