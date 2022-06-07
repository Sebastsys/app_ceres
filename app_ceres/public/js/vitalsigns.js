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

frappe.ui.form.on("Vital Signs", "bp_diastolic", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var a = (parseInt(d.bp_systolic) + (2*parseInt(d.bp_diastolic)))/3;
    frappe.model.set_value(cdt, cdn, "presion_arterial_media", a); 
    
});
frappe.ui.form.on("Vital Signs", "glasgow_motora", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var a = parseInt( d.glasgow_ocular)  + parseInt( d.glasgow_verbal) + parseInt( d.glasgow_motora);
    frappe.model.set_value(cdt, cdn, "glasgow_total", a); 
    
});
frappe.ui.form.on("Vital Signs", "glasgow_verbal", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var a = parseInt( d.glasgow_ocular)  + parseInt( d.glasgow_verbal) + parseInt( d.glasgow_motora);
    frappe.model.set_value(cdt, cdn, "glasgow_total", a); 
    
});
frappe.ui.form.on("Vital Signs", "glasgow_ocular", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    var a = parseInt( d.glasgow_ocular)  + parseInt( d.glasgow_verbal) + parseInt( d.glasgow_motora);
    frappe.model.set_value(cdt, cdn, "glasgow_total", a); 
    
});
frappe.ui.form.on("Vital Signs", "patient_name", function(frm, cdt, cdn) {
    var d = locals[cdt][cdn];
    frappe.call({
		method:"app_ceres.ceres.controllers.paciente.edadmeses",
		args: {paciente: d.patient_name}
	}).done((r)=>{
		console.log(r.message[0]);
		//console.log(moment(now));
        //var total_days = moment(now).diff(r.message[0], "days");
        //var edadcalculada = Math.floor((total_days).toFixed(2) / 365.25);
        frappe.model.set_value(cdt, cdn, 'edad_meses',r.message[0]);
	})
    
});

frappe.ui.form.on("Vital Signs", "estatura_vs_edad", function(frm, cdt, cdn){
    var d = locals[cdt][cdn];
	let sexo;
	console.log(d.patient_name);
    frappe.call({
		method:"app_ceres.ceres.controllers.paciente.sexo",
		args: {paciente: d.patient_name}
	}).done((r)=>{
		sexo=r.message[0];
		if(sexo ==="Male"){
			var myWin = window.open('http://192.168.100.174:82/leninios?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
		}else if(sexo ==="Female"){
			var myWin = window.open('http://192.168.100.174:82/leninias?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
		}
	})
            
    
});

frappe.ui.form.on("Vital Signs", "pc_vs_edad", function(frm, cdt, cdn){
    var d = locals[cdt][cdn];
	let sexo;
	console.log(d.patient_name);
    frappe.call({
		method:"app_ceres.ceres.controllers.paciente.sexo",
		args: {paciente: d.patient_name}
	}).done((r)=>{
		sexo=r.message[0];
		if(sexo ==="Male"){
			var myWin = window.open('http://192.168.100.174:82/pcninios?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
		}else if(sexo ==="Female"){
			var myWin = window.open('http://192.168.100.174:82/pcninias?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
		}
	})
            
    
});


frappe.ui.form.on("Vital Signs", "peso_vs_edad", function(frm, cdt, cdn){
    var d = locals[cdt][cdn];
	let sexo;
	console.log(d.patient_name);
    frappe.call({
		method:"app_ceres.ceres.controllers.paciente.sexo",
		args: {paciente: d.patient_name}
	}).done((r)=>{
		sexo=r.message[0];
		if(sexo ==="Male"){
			if(locals[cdt][cdn].edad_meses<=24){
				var myWin = window.open('http://192.168.100.174:82/peninios?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
			}else{
				var myWin = window.open('http://192.168.100.174:82/peninios2-20?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
			}
			
		}else if(sexo ==="Female"){
			if(locals[cdt][cdn].edad_meses<=24){
				var myWin = window.open('http://192.168.100.174:82/peninias?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
			}else{
				var myWin = window.open('http://192.168.100.174:82/peninias2-20?codigovitalsign='+cur_frm.doc.patient_name+'&_lang=en');
			}
		}
	})
            
    
});