#!/usr/bin/env python
"""sorter.py"""

# Leer y ordenar mensaje.txt
with open("salida_mapper.txt", "r", encoding="utf-8") as f:
    lineas_ordenadas = sorted(f)

# Guardar en un nuevo archivo
with open("salida_sorter.txt", "w", encoding="utf-8") as out:
    out.writelines(lineas_ordenadas)

print("✅ Resultado ordenado guardado en 'salida_sorter.txt'")
