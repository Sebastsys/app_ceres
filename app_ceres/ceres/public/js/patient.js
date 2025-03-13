frappe.ui.form.on('Patient', {
    onload: function(frm) {
        console.log("HHHHHH: ", frappe.session.user);
        // Filtrar el campo médico para mostrar solo el médico del usuario actual
        /*frm.set_query('medico', function() {
            return {
                filters: {
                    'user_id': frappe.session.user // Asegúrate de que el campo 'user' esté presente en el doctype de healthcare practitioner
                }
            };
        });*/
    },
    refresh: function(frm) {
        
    }
});