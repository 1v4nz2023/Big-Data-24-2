# 1. Cree una sesión de Spark con nombre Cap2 y asegúrese de que emplea todos los cores disponibles 
#    para ejecutar en su ambiente de trabajo.

# 2. Cree dos RDD vacíos, uno de ellos no debe contener particiones y el otro debe tener 5 
#    particiones. Utilice vías diferentes para crear cada RDD.

# 3. Cree un RDD que contenga los números primos que hay entre 1 y 20.

# 4. Cree un nuevo RDD a partir del RDD creado en el ejercicio anterior el cuál solo contenga los 
#    números primos mayores a 10.

# 5. Descargue el archivo de texto adjunto a esta lección como recurso y guárdelo en una carpeta 
#    llamada data en el ambiente de trabajo de Colab.

#       A) Cree un RDD a partir de este archivo de texto en donde todo el documento esté contenido 
#          en un solo registro. ¿Cómo podría saber la dirección donde está guardado el archivo de 
#          texto a partir del RDD creado?

#       B) Si necesitara crear un RDD a partir del archivo de texto cargado previamente en donde 
#          cada línea del archivo fuera un registro del RDD, ¿cómo lo haría?