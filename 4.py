#!/usr/bin/env python
"""reducer.py"""

current_word = None
current_count = 0
word = None

# Abrir archivo de entrada local ya ordenado
with open("salida_sorter.txt", "r", encoding="utf-8") as file_split1, \
     open("resultado_final.txt", "w", encoding="utf-8") as output_file:
    
    for line in file_split1:
        line = line.strip()

        # Parsear línea
        try:
            word, count = line.split('\t', 1)
            count = int(count)
        except ValueError:
            continue  # Saltar líneas inválidas

        if current_word == word:
            current_count += count
        else:
            if current_word:
                output_file.write(f"{current_word}\t{current_count}\n")
            current_word = word
            current_count = count

    # Última palabra
    if current_word == word:
        output_file.write(f"{current_word}\t{current_count}\n")

print("✅ Resultado del reducer guardado en 'resultado_final.txt'")
