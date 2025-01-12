// Copyright (c) 2024, Francisco Adame and contributors
// For license information, please see license.txt

frappe.ui.form.on("Escala Hamilton Ansiedad", {
    onload(frm) {
        if (frm.doc.__islocal) {
            // Obtener los datos de la tabla "Items EH Ansiedad"
            frappe.db.get_list('Items EH Ansiedad', {
              fields: ['name', 'item', 'sintomas', 'puntaje'],
              order_by: 'creation desc'
            }).then(function(data) {
              // Llenar la tabla "eh_ansiedad" con los datos
              frm.set_value('eh_ansiedad', []);
              data.forEach(function(item) {
                frm.add_child('eh_ansiedad', {
                  item: item.name,
                  sintomas: item.sintomas,
                  puntaje: item.puntaje
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
