import json

# Abrir y cargar el archivo JSON
with open("mock.json", "r", encoding="utf-8") as json_file:
    json_data = json.load(json_file)

# Convertir el diccionario a una cadena JSON válida y formateada
json_formateado = json.dumps(json_data, ensure_ascii=False, indent=4)

# Imprimir el JSON formateado
print(json_formateado)
