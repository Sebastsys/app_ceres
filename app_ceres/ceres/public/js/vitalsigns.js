frappe.ui.form.on('Vital Signs', {
	 pulse: function(frm) {
        llamar();   
	  }
});


function llamar(){
   
    frappe.call({
        method: "app_ceres.ceres.controllers.paciente.obtenerPercentilCardiaca",
        args: {
            paciente: cur_frm.patient,
            valor:  cur_frm.pulse
        },
        callback: (r) => {
              console.log(r.message);
        },
    });

}