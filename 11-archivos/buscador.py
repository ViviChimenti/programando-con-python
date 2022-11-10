
paises = open("BDpaises.txt","r") #abrir el archivo con el que voy a trabajar, y vamos a tener que recorrerlo linea por linea. 


# "Argentina 33900 95 25.6 3408\n" 
# ["Argentina",33900, 95, 25.6, 3408] -- pais
filtro = input("Pais ? ")
for p in paises: #p es una cadena de texto
  pais= p.replace("\n","") #"Argentina,33900,95,25.6,3408" --- replace reemplaza a \n por ""  nada
  pais = pais.split(",")  # ["Argentina","33900", "95", "25.6", "3408"]  .split hace una lista
                                                                            #ctrl + h para buscar y reemplazar                                                                        
  pais[1] = int(pais[1])
  pais[2] = int(pais[2])
  pais[3] = float(pais[3])
  pais[4] = int(pais[4]) # ["Argentina",33900, 95, 25.6, 3408]

  if filtro.lower() in pais[0].lower():  #lower es un metodo de la cadena para pasar todo a minusculas
    print(f"{pais[0]:20} tiene {pais[1]*1000:15,} habitantes") # :20 muestra el dato en 20 caracteres , va formando una especie de tabla.
 # probando
 
print("FIN") #testigo de que termina el programa
paises.close() #cerrar y liberar memoria


