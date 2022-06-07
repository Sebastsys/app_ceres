from __future__ import unicode_literals
import frappe
 
sitemap = 1

def get_context(context):
    context.show_search = True
    context.allow_guest = True
    context.no_breadcrumbs = True

@frappe.whitelist(allow_guest=True)
def pcsignosvitales(name):
    values = {'name': name}
    return frappe.db.sql(""" SELECT edad_meses, (pcninios) as pc
                        FROM dbceres.`tabVital Signs`
                        WHERE patient_name = %(name)s
                         """, values=values, as_dict=0)