frappe.ui.form.on('Vital Signs', {
	pulse: function(frm) {
		
		buscarPercetilFC();
			
	 },
	respiratory_rate: function(frm){
		buscarPercetilFR();
	}
});


function buscarPercetilFC(){
  	if(cur_frm.doc.pulse!=""){
		frappe.call({
			method: "app_ceres.ceres.controllers.paciente.obtenerPercentilCardiaca",
			freeze: true,
			args: {
				paciente: cur_frm.doc.patient,
				valor:  cur_frm.doc.pulse
			},
			callback: (r) => {
				cur_frm.set_value("percentil_fc",r.message);
				cur_frm.refresh()
			},
		});
  	}else{
		cur_frm.set_value("percentil_fc","");
		cur_frm.refresh()
	  }
}

function buscarPercetilFR(){
	console.log(cur_frm.doc.respiratory_rate);
	if(cur_frm.doc.respiratory_rate!=""){
		frappe.call({
			method: "app_ceres.ceres.controllers.paciente.obtenerPercentilRespiratoria",
			freeze: true,
			args: {
				paciente: cur_frm.doc.patient,
				valor:  cur_frm.doc.respiratory_rate
			},
			callback: (r) => {
				  cur_frm.set_value("percentil_fr",r.message);
				  cur_frm.refresh()
			},
		});
	}else{
		cur_frm.set_value("percentil_fr","");
		cur_frm.refresh()
	}
}