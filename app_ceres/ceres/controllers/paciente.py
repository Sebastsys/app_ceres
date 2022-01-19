from __future__ import unicode_literals
import frappe
 
import random

def generarSecuenciaReceta(doc,method):
    
    doctor = frappe.get_doc("Healthcare Practitioner",doc.practitioner)
    nreceta = doctor.nreceta_siguiente    
    #nrecetaobj = frappe.db.get_single_value('NumeroReceta', 'numero_de_receta')
 
    if not nreceta:
        nreceta = 1 
        
    doc.numero_receta = nreceta    
    doctor.nreceta_siguiente = nreceta + 1
    doctor.save()