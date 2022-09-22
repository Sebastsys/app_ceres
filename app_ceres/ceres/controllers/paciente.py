from __future__ import unicode_literals
import frappe
 
 

def generarSecuenciaReceta(doc,method):
    
    doctor = frappe.get_doc("Healthcare Practitioner",doc.practitioner)
    nreceta = doctor.nreceta_siguiente    
    
    #nrecetaobj = frappe.db.get_single_value('NumeroReceta', 'numero_de_receta')
 
    #if not nreceta:
     #   nreceta = 1 
        
    doc.numero_receta = nreceta    
    doctor.nreceta_siguiente = nreceta + 1
    doctor.save()
def generarSecuenciaHC(doc,method):
    
    paciente = frappe.db.sql("""select max(CAST(hc AS UNSIGNED)) as hc from tabPatient""", as_dict=False)
    if paciente:
        nhc = int(paciente[0][0])
    else:
        nhc=0
    nhc=nhc+1
        
    doc.hc = str(nhc)
    #paciente.save()
    
@frappe.whitelist()
def obtenerPercentilCardiaca(paciente,valor):
    edad = """ SELECT TIMESTAMPDIFF(MONTH , (select dob from tabPatient tp where name = '{0}' ) , CURDATE()) as edadmeses""".format(paciente)
    
    res1 = frappe.db.sql(edad, as_dict=True)[0]
    mensage = ""
    if res1["edadmeses"]<=216:
        sql = """ select * from `tabFrecuencia Cardiaca PC` tfcp 
where 
(SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where name = '{0}' ) , CURDATE())  
)
>=  rango_inicial and (SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where name = '{0}' ) , CURDATE())  
) < rango_final  """.format(paciente)
     
        res = frappe.db.sql(sql, as_dict=True)[0]
        mensage = ""
        if int(valor) <= res["1st"]:
            mensage =  "Percentil: 1st"
        if int(valor) > res["1st"] and int(valor) <= res["5th"]:
            mensage =  "Percentil: 5th"
        if int(valor) > res["5th"] and int(valor) <= res["10th"]:
            mensage =  "Percentil: 10th"
        if int(valor) > res["10th"] and int(valor) <= res["50th"]:
            mensage =  "Percentil: 50th"
        if int(valor) > res["50th"] and int(valor) <= res["90th"]:
            mensage =  "Percentil: 90th"
        if int(valor) > res["90th"] and int(valor) <= res["95th"]:
            mensage =  "Percentil: 95th"
        if int(valor) > res["95th"] and int(valor) <= res["99th"]:
            mensage =  "Percentil: 99th"
        if int(valor) > res["99th"]:
            mensage =  "Existe un error en el ingreso de los datos"
    else:
        mensage="-"
    return mensage

@frappe.whitelist()
def obtenerPercentilRespiratoria(paciente,valor):
    edad = """ SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where name = '{0}' ) , CURDATE()) as edadmeses""".format(paciente)
    
    res1 = frappe.db.sql(edad, as_dict=True)[0]
    mensage = ""
    if res1["edadmeses"]<=216:
        sql = """ select * from `tabFrecuenciaRespiratoriaPC` tfrp 
where 
(SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where name = '{0}' ) , CURDATE())  
)
>=  rango_inicial and (SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where name = '{0}' ) , CURDATE())  
) < rango_final  """.format(paciente)
     
        res = frappe.db.sql(sql, as_dict=True)[0]
        
        if int(valor) <= res["1st"]:
            mensage =  "Percentil: 1st"
        if int(valor) > res["1st"] and int(valor) <= res["5th"]:
            mensage =  "Percentil: 5th"
        if int(valor) > res["5th"] and int(valor) <= res["10th"]:
            mensage =  "Percentil: 10th"
        if int(valor) > res["10th"] and int(valor) <= res["50th"]:
            mensage =  "Percentil: 50th"
        if int(valor) > res["50th"] and int(valor) <= res["90th"]:
            mensage =  "Percentil: 90th"
        if int(valor) > res["90th"] and int(valor) <= res["95th"]:
            mensage =  "Percentil: 95th"
        if int(valor) > res["95th"] and int(valor) <= res["99th"]:
            mensage =  "Percentil: 99th"
        if int(valor) > res["99th"]:
            mensage =  "Existe un error en el ingreso de los datos"
    else:
            mensage = "-"
    return mensage



@frappe.whitelist()
def edadmeses(paciente):
    values = {'paciente': paciente}
    fechanac = """ SELECT TIMESTAMPDIFF(MONTH , (select  dob from  tabPatient tp where tp.patient_name = '{0}' ) , CURDATE()) as edadmeses """.format(paciente)
    return  frappe.db.sql(fechanac, as_dict=False)[0]
#frappe.db.sql(""" SELECT dob from tabPatient tp where tp.patient_name = %(paciente)s""", values=values, as_dict=1)


@frappe.whitelist()
def sexo(paciente):
    sexo = """ SELECT tp.sex FROM tabPatient tp WHERE tp.patient_name = '{0}' """.format(paciente)
    return  frappe.db.sql(sexo, as_dict=False)[0]