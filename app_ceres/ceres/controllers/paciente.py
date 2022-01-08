from __future__ import unicode_literals
import frappe
 
import random

def generarSecuenciaReceta(doc,method):
    nrecetaobj = frappe.db.get_single_value('NumeroReceta', 'numero_de_receta')
    nreceta = 0
    if not nrecetaobj:
        nreceta = nrecetaobj
    doc.n_receta = nreceta
    frappe.db.set_value('NumeroReceta', 'numero_de_receta', nreceta+1)