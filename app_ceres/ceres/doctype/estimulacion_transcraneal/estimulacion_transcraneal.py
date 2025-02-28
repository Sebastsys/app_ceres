# Copyright (c) 2025, Francisco Adame and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class EstimulacionTranscraneal(Document):
	def before_insert(self):
		# Obtener el último registro para el encuentro_psicologico
		last_record = frappe.get_list('Estimulacion Transcraneal',filters={'encuentro_psicologo': self.encuentro_psicologo},fields={'name','numero_sesion'},order_by='numero_sesion desc',limit=1)
		if last_record and last_record[0].numero_sesion is not None:
			# Incrementar el número de sesión
			self.numero_sesion = int(last_record[0].numero_sesion) + 1
		else:
			# Si no hay registros previos, iniciar en 1
			self.numero_sesion = 1
	
	def before_save(self):
		# Sumar items de la escala
		suma = 0
		for item in self.table_yffy:
			suma += int(item.puntaje)
		
		#self.suma_puntuacion: campo editable para el usuario
		#if suma < 7:
		#	self.suma_puntuacion = str(suma)+': No se detecta depresión'
		#	self.puntos=suma
		#if suma >= 7 and suma <= 17:
		#	self.suma_puntuacion = str(suma)+': Se detecta depresión leve'
		#	self.puntos=suma
		#if suma >= 18 and suma <= 24:
		#	self.suma_puntuacion = str(suma)+': Se detecta depresión moderada'
		#	self.puntos=suma
		#if suma >= 25:
		#	self.suma_puntuacion = str(suma)+': Se detecta depresión severa'
		#	self.puntos=suma
