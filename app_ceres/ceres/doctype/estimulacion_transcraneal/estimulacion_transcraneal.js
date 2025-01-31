// Copyright (c) 2025, Francisco Adame and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Estimulacion Transcraneal", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Estimulacion Transcraneal", {
    refresh(frm) {
        if (frm.doc.__islocal) {
            // Obtener los datos de la tabla "Items EH Ansiedad"
            frappe.db.get_list('Items Estimulacion Transcraneal', {
              fields: ['name', 'item', 'sintomas'],
              order_by: 'creation desc'
            }).then(function(data) {
              // Llenar la tabla "eh_ansiedad" con los datos
              frm.set_value('table_yffy', []);
              data.forEach(function(item) {
                frm.add_child('table_yffy', {
                  item: item.name,
                  sintomas: item.sintomas,
                });
              });
            });
        }
 	},
     patient: function(frm) {
        // Filtrar el campo encuentro_psicologico según el paciente seleccionado
        frm.set_query('encuentro_psicologo', function() {
          return {
            filters: {
              patient: frm.doc.patient // Filtrar por el paciente seleccionado
            }
          };
        });
     }
});

