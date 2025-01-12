// Copyright (c) 2024, Francisco Adame and contributors
// For license information, please see license.txt

frappe.ui.form.on("ESCALA HAMILTON DEPRESION", {
    refresh(frm) {
        if (frm.doc.__islocal) {
            // Obtener los datos de la tabla "Items EH Ansiedad"
            frappe.db.get_list('ITEMS EH DEPRESION', {
              fields: ['name', 'item', 'sintomas'],
              order_by: 'creation desc'
            }).then(function(data) {
              // Llenar la tabla "eh_ansiedad" con los datos
              frm.set_value('table_mhdv', []);
              data.forEach(function(item) {
                frm.add_child('table_mhdv', {
                  item: item.name,
                  sintomas: item.sintomas,
                });
              });
            });
        }
 	},
     patient: function(frm) {
        // Filtrar el campo encuentro_psicologico según el paciente seleccionado
        frm.set_query('encuentro_psicologico', function() {
          return {
            filters: {
              patient: frm.doc.patient // Filtrar por el paciente seleccionado
            }
          };
        });
     }
});
