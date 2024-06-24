name = "abel"

name = name.capitalize()

#Muestra el contenido de la variable name
print(name)

#Muestra el contenido de la variable name concatenado con un string
print("Hola, " + name + " ¿Cómo estás?")

#Muestra el contenido de la variable name con la función format simplificada
print(f"Hola, {name} ¿Cómo estás?")

#Muestra el contenido de la variable name con la función format extendida
print("Hola, {name} ¿Cómo estás?".format(name=name))