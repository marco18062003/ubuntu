from openpyxl import load_workbook

# Especifica la ruta del archivo Excel
archivo_excel = 'primer.xlsx'

# Carga el archivo Excel existente
libro = load_workbook(archivo_excel)

# Selecciona la hoja activa (o usa el nombre de la hoja si lo conoces)
hoja = libro.active  # O usa libro['NombreDeLaHoja'] si tienes un nombre específico

# Cambia el valor de la celda A1
hoja['A1'] = input("")

# Guarda los cambios en el archivo
libro.save(archivo_excel)

print('La celda A1 ha sido modificada y el archivo ha sido guardado.')
 