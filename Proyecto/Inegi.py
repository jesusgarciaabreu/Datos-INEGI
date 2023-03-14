# -*- coding:utf-8 -*-

##########################################################
# Manejo de Datos
# Proyecto
# Equipo: García Abreu Jesús
#         Cruz Galicia Alma Denisse
##########################################################
import sqlite3

conexion = sqlite3.connect("resumen_inegi.db")
cursor = conexion.cursor()

class Inegi:
	""" Clase Inegi, contiene un archivo tipo csv con datos recabados por el INEGI."""

	##########################################################
	# Método constructor.
	##########################################################
	def __init__(self, name_file):
		self.name_file = name_file
	

	##########################################################
	# Pregunta 1.
	#
	##########################################################
	def poblacion_total_entidad(self):
		""" Calcula la población total para cada entidad.
		:returns: dict, 
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_poblacion_total = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma = 0
		lista_aux = []
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")

			# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
			# es igual a lista auxliar respectivamente en la posición, vamos sumando la población total en una 
			# variable, y modificamos el valor del value del diccionario en esa posición por el de la suma.
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma = int(lista_aux[5])
					diccionario_poblacion_total[lista_entidades[i]] += suma
					break
				
				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración, y cambiamos el
				# valor de suma a 0, para reiniciar el valor para la siguiente entidad.
				elif lista_aux[1] != lista_entidades[i]:
					i += 1
					suma = 0
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_poblacion_total

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_total_femenina(self):
		""" 
		* Calcula la población total femenina para cada entidad.
		:return: dict, un diccionario con la población total femenina de las 32 entidades.
		"""

		# El algoritmo es análogo al anterior
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_femenina = {lista_entidades : 0 for lista_entidades in lista_entidades}
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_femenina = 0
		lista_aux = []
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_femenina = int(lista_aux[6])
					diccionario_poblacion_femenina[lista_entidades[i]] += suma_femenina
					break
				elif lista_aux[1] != lista_entidades[i]:
					i += 1
					suma_femenina = 0
		datos_inegi.close()
		return diccionario_poblacion_femenina

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_total_masculina(self):

		""" Calcula la población total masculina para cada entidad.
		:return: dict, un diccionario con la población total masculina de las 32 entidades.
		"""

		# El algoritmo es análogo al anterior
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_masculina = {lista_entidades : 0 for lista_entidades in lista_entidades}
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_masculina = 0
		lista_aux = []
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_masculina = int(lista_aux[7])
					diccionario_poblacion_masculina[lista_entidades[i]] += suma_masculina
					break
				elif lista_aux[1] != lista_entidades[i]:
					i += 1
					suma_masculina = 0
		datos_inegi.close()
		return diccionario_poblacion_masculina

	##########################################################
	# Pregunta 2.
	#
	##########################################################
	def ditritos_poblacion_indigena(self):
		""" Obtiene los distritos que contienen población indígena de cada entidad.
		:return: dict, un diccionario con la población total de indigenas de las 32 entidades.
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_indigenas = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_indigenas = 0

		# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
		# es igual a lista auxliar respectivamente en la posición, verificamos si en el la columa de población
		# indigena viene escrito "SI" y sumamos uno a la variable de suma_indigenas.
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					if lista_aux[3] == "SI":
						suma_indigenas = 1
						diccionario_indigenas[lista_entidades[i]] += suma_indigenas

				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración.
				else:
					i += 1
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_indigenas

	##########################################################
	# Pregunta 3.
	#
	##########################################################
	def poblacion_total_cero_dos(self):
		""" Calcula la población total de 0 a 2 años de cada entidad.
		:return: dict, un diccionario con la población total de 0 a 2 años de las 32 entidades.
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_poblacion_0a2 = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_0a2 = 0

		# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
		# es igual a lista auxliar respectivamente en la posición, vamos sumando la población total 
		# de niños de 0 a 2 añosen una variable, y modificamos el valor del value del diccionario en esa posición
		# por el de la suma.
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_0a2 = int(lista_aux[8])
					diccionario_poblacion_0a2[lista_entidades[i]] += suma_poblacion_0a2

				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración, y cambiamos el
				# valor de suma_poblacion_0a2 a 0, para reiniciar el valor para la siguiente entidad.
				else:
					i += 1
					suma_poblacion_0a2 = 0
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_poblacion_0a2

	##########################################################
	# Pregunta 4.
	#
	##########################################################
	def poblacion_3_mas_hli(self):
		""" Calcula la población total de 3 años a más que hablan alguna lengua indígena de cada entidad.
		:return: dict, un diccionario con la población total de 3 años y mas que hablan una lengua indígena de todas
		* las entidades.
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_poblacion_3_mas_hli = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_3_mas_hli = 0

		# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
		# es igual a lista auxliar respectivamente en la posición, vamos sumando la población total 
		# de niños de 0 a 2 años en una variable, y modificamos el valor del (value) del diccionario en esa posición
		# por el de la suma.
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_3_mas_hli = int(lista_aux[30])
					diccionario_poblacion_3_mas_hli[lista_entidades[i]] += suma_poblacion_3_mas_hli

				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración, y cambiamos el
				# valor de suma_poblacion_0a2 a 0, para reiniciar el valor para la siguiente entidad.
				else:
					i += 1
					suma_poblacion_3_mas_hli = 0
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_poblacion_3_mas_hli


	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_3_5_nae(self):
		""" Calcula la población total de 3 a 5 años que no asisten a la escuela.
		:return: dict, un diccionario con la población total de 3 años a 5 años que no asisten a la escuela.
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_poblacion_3_5_nae = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_3_5_nae = 0

		# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
		# es igual a lista auxliar respectivamente en la posición, vamos sumando la población total 
		# de niños de 3 a 5 años que no asisten a la escuela, en una variable, y modificamos el valor del (value)
		# del diccionario en esa posición por el de la suma.
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_3_5_nae = int(lista_aux[21])
					diccionario_poblacion_3_5_nae[lista_entidades[i]] += suma_poblacion_3_5_nae

				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración, y cambiamos el
				# valor de suma_poblacion_3_5_nae a 0, para reiniciar el valor para la siguiente entidad.
				else:
					i += 1
					suma_poblacion_3_5_nae = 0
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_poblacion_3_5_nae

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_6_11_nae(self):
		""" Calcula la población total de 6 a 11 años que no asisten a la escuela.
		:return: dict, un diccionario con la población total de 6 años a 11 años que no asisten a la escuela.
		"""

		# El algoritmo es análogo al anterior.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_6_11_nae = {lista_entidades : 0 for lista_entidades in lista_entidades}

		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_6_11_nae = 0
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_6_11_nae = int(lista_aux[24])
					diccionario_poblacion_6_11_nae[lista_entidades[i]] += suma_poblacion_6_11_nae
				else:
					i += 1
					suma_poblacion_6_11_nae = 0
		datos_inegi.close()
		return diccionario_poblacion_6_11_nae	

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_12_14_nae(self):
		""" Calcula la población total de 12 a 14 años que no asisten a la escuela.
		:return: dict, un diccionario con la población total de 12 años a 14 años que no asisten a la escuela.
		"""

		# El algoritmo es análogo al anterior.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_12_14_nae = {lista_entidades : 0 for lista_entidades in lista_entidades}

		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_12_14_nae = 0
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_12_14_nae = int(lista_aux[27])
					diccionario_poblacion_12_14_nae[lista_entidades[i]] += suma_poblacion_12_14_nae
				else:
					i += 1
					suma_poblacion_12_14_nae = 0
		datos_inegi.close()
		return diccionario_poblacion_12_14_nae

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_3_5(self):
		""" Calcula la población total de 3 a 5 años.
		:return: dict, un diccionario con la población total de 3 años a 5 años.
		"""

		# Creamos un diccionario con las 32 entidades.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		# Creamos el diccionario con las entidades.
		diccionario_poblacion_3_5 = {lista_entidades : 0 for lista_entidades in lista_entidades}

		# Abrimos el archivo y lo vamos a recorrer.
		# Creamos una lista auxiliar donde vamos a separar cada elemento por las comas que tiene la linea.
		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_3_5 = 0

		# Recorremos la lista auxiliar y la comparamos con la lista de entidades, si la lista de entidades
		# es igual a lista auxliar respectivamente en la posición, vamos sumando la población total 
		# de niños de 3 a 5 años, en una variable, y modificamos el valor del (value)
		# del diccionario en esa posición por el de la suma.
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_3_5 = int(lista_aux[12])
					diccionario_poblacion_3_5[lista_entidades[i]] += suma_poblacion_3_5

				# Si pasa que el elemento de la lista auxiliar es distinto a la lista de entidades, cambiamos la 
				# posicion a la siguiente de la lista de entidades, y volvemos a hacer la iteración, y cambiamos el
				# valor de suma_poblacion_3_5 a 0, para reiniciar el valor para la siguiente entidad.
				else:
					i += 1
					suma_poblacion_3_5 = 0
		datos_inegi.close()

		# Regresamos el diccionario.
		return diccionario_poblacion_3_5

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_6_11(self):
		""" Calcula la población total de 6 a 11 años.
		:return: dict, un diccionario con la población total de 6 años a 11 años.
		"""

		# El algoritmo es análogo al anterior.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_6_11 = {lista_entidades : 0 for lista_entidades in lista_entidades}

		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_6_11 = 0
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_6_11 = int(lista_aux[15])
					diccionario_poblacion_6_11[lista_entidades[i]] += suma_poblacion_6_11
				else:
					i += 1
					suma_poblacion_6_11 = 0
		datos_inegi.close()
		return diccionario_poblacion_6_11	

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def poblacion_12_14(self):
		""" Calcula la población total de 12 a 14 años.
		:return: dict, un diccionario con la población total de 12 años a 14 años.
		"""

		# El algoritmo es análogo al anterior.
		lista_entidades = ["Aguascalientes", "Baja California", "Baja California Sur", "Campeche", "Coahuila de Zaragoza"
		, "Colima","Chiapas", "Chihuahua", "Ciudad de México", "Durango", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco"
		, "México", "Michoacán de Ocampo", "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro"
		, "Quintana Roo", "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala",
		"Veracruz de Ignacio de la Llave", "Yucatán", "Zacatecas"]

		diccionario_poblacion_12_14 = {lista_entidades : 0 for lista_entidades in lista_entidades}

		datos_inegi = open(self.name_file, "r", encoding = "utf-8")
		suma_poblacion_12_14 = 0
		for line in datos_inegi.readlines():
			lista_aux = line.split(",")
			for i in range(len(lista_entidades)):
				if lista_aux[1] == lista_entidades[i]:
					suma_poblacion_12_14 = int(lista_aux[18])
					diccionario_poblacion_12_14[lista_entidades[i]] += suma_poblacion_12_14
				else:
					i += 1
					suma_poblacion_12_14 = 0
		datos_inegi.close()
		return diccionario_poblacion_12_14

	##########################################################
	# Pregunta 5.
	#
	##########################################################
	def prom_3_14_nae(self):
		""" Calcula la población total de 3 a 14 años que no asisten a la escuela.
		:return: dict, un diccionario con el promedio de la población de 3 a 14 años que no asiste a la escuela.
		"""

		# Creamos una lista con los valores respectivos de población de cada edad, dependiendo si asistieron 
		# o no a una escuela.
		lista_poblacion_3_5 = list(self.poblacion_3_5().values())
		lista_poblacion_6_11 = list(self.poblacion_6_11().values())
		lista_poblacion_12_14 = list(self.poblacion_12_14().values())
		lista_poblacion_3_5nae = list(self.poblacion_3_5_nae().values())
		lista_poblacion_6_11nae = list(self.poblacion_6_11_nae().values())
		lista_poblacion_12_14nae = list(self.poblacion_12_14_nae().values())

		lista_poblacion_3_14 = []
		lista_poblacion_3_14nae = []
		cantidad_nae = 0
		cantidad = 0

		# Creamos dos listas, una donde guardaremos los valores de la población de edades 3 a 14 años, y otra donde
		# guardaremos los valores de la población de edades de 3 a 14 años tal que no asistieron a la escuela.
		for i in range(32):
			cantidad = lista_poblacion_3_5[i] + lista_poblacion_6_11[i] + lista_poblacion_12_14[i]
			cantidad_nae = lista_poblacion_3_5nae[i] + lista_poblacion_6_11nae[i] + lista_poblacion_12_14nae[i]
			lista_poblacion_3_14.append(cantidad)
			lista_poblacion_3_14nae.append(cantidad_nae)

		# Creamos otra lista donde vamos a guardar el valor promedio de la población de 3 a 14 años que no asiste a
		# a la escuela
		lista_promedio = []
		for i in range(32):
			promedio = lista_poblacion_3_14nae[i] / lista_poblacion_3_14[i]
			lista_promedio.append(promedio)
		
		# Lo guardamos en un diccionario y lo regresamos.
		diccionario_promedio = dict(zip(list(self.poblacion_12_14_nae().keys()), lista_promedio ))
		return diccionario_promedio

	##########################################################
	# Agregar datos.
	#
	##########################################################
	def agrega_datos(self):
		""" Lee los datos del archivo csv y los agrega a la tabla 'entidad' de la base de datos. """

		# Tomamos en una lista la poblacion total, poblacion total femenina y poblacion total masculina
		# respectivamente de cada entidad.
		lista_poblacion_total = list(self.poblacion_total_entidad(self.name_file).values())
		lista_poblacion_femenina = list(self.poblacion_total_femenina(self.name_file).values())
		lista_poblacion_masculina = list(self.poblacion_total_masculina(self.name_file).values())
		lista_entidades =  list(self.poblacion_total_entidad(self.name_file).keys())
		
		# Aqui vamos agregando los datos en nuestra base de datos anteriormente creada conforme recorremos cada 
		# uno de los elementos de nuestras listas.
		for i in range(32):
			query = "INSERT INTO entidad VALUES (" + str(i) + ",'" + str(lista_entidades[i]) + "'," + str(lista_poblacion_total[i]) + "," + str(lista_poblacion_femenina[i]) +  "," + str(lista_poblacion_masculina[i]) + ");"
			cursor.execute(query)
			conexion.commit()
		conexion.close()

	##########################################################
	# Función auxiliar.
	#
	##########################################################
	def borra_datos():
		"Borra todos los datos de nuestra base de datos."

		query = "DELETE FROM entidad"
		cursor.execute(query)
		conexion.commit()
		conexion.close()

	##########################################################
	# Consultar datos.
	#
	##########################################################
	def consulta_datos(self, id):
		""" Consulta los datos correspondientes a la entidad correspondiente al id."""

		# Aqui seleccionamos los datos que se nos piden dado el id.
		select_query = f"SELECT nombre, poblacion_total, poblacion_total_fem, poblacion_total_masc FROM entidad WHERE id = {id};"
		result = cursor.execute(select_query)

		# Lo guardamos en una lista.
		lista_bd = result.fetchall()
		lista_entidad = []
		lista_pob_tot = []

		# Recorremos la lista_bd y en una nueva lista guardamos el nombre, y en la otra, guardamos la población
		# total, la población total femenina y la población total masculina.
		for datos in lista_bd:
			lista_entidad.append(datos[0])
			lista_pob_tot.append(datos[1])
			lista_pob_tot.append(datos[2])
			lista_pob_tot.append(datos[3])

		#Lo guardamos en un diccionario y lo regresamos.
		diccionario = dict(zip(lista_entidad,[lista_pob_tot]))
		conexion.close()
		return diccionario

if __name__=="__main__":
	mi_inegi = Inegi("INE_DISTRITO_2020.csv")
	print("PREGUNTA 1:")
	print(mi_inegi.poblacion_total_entidad())
	print("PREGUNTA 2:")
	print(mi_inegi.ditritos_poblacion_indigena())
	print("PREGUNTA 3:")
	print(mi_inegi.poblacion_total_cero_dos())
	print("PREGUNTA 4:")
	print(mi_inegi.poblacion_3_mas_hli())
	print("PREGUNTA 5:")
	print(mi_inegi.prom_3_14_nae())
	print("CONSULTA DATOS:")
	print(mi_inegi.consulta_datos(2))

	# Esta las pongo en comentarios, ya que si se vuelven a mandar, se crean mas datos en la base de datos.

	#print(agrega_datos("INE_DISTRITO_2020.csv"))
	#print(borra_datos())