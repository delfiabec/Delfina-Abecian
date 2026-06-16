#variables

my_variable="My String variable"
print(my_variable)


my_int_variable= 5
print(my_int_variable)

my_bool_variable= True
print(my_bool_variable)

#puedo cambiar un int a un string con str 
my_int_str= str(my_int_variable)
print(my_int_str)


print(my_variable, my_int_variable, my_bool_variable)
print(my_variable, my_int_str, my_bool_variable)


#funciones del sistema
print(len(my_int_str))#1

print(len(my_variable))#18
#len() es la cantidad de caracterese que tiene contando espacios


print("este es el valor de:", my_bool_variable)
#me da el texto: el valro de la variable
print("esta es la longitud:",len(my_variable)) #esta es la longitud:18

#variables en una sola linea
name, surname, alias, age = "delfina", "abecian", "chuchy", 19
print("mi nombre es:", name, surname, alias,"y mi edad es:", age) #mi nombre es: delfina abecian chuchy y mi edad es: 19

pregunta= input("whats your name: ")
print(pregunta)
#con input puedo ahcer preguntas y que el otro me responda



#cambiamos su tipo
name = 19
age = "delfina"
print(name)
print(age)




