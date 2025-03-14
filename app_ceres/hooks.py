from . import __version__ as app_version

app_name = "app_ceres"
app_title = "CERES"
app_publisher = "Francisco Adame"
app_description = "Sistema para la Gestión Integral de Clinicas y Hospitales"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sebas.franksys@gmail.com"
app_license = "MIT"
app_logo_url = "/assets/app_ceres/img/LogoClamMedical.png"

# Includes in <head>
# ------------------
website_context = {
"favicon": "/assets/app_ceres/img/LogoClamMedical.png",
"splash_image": "/assets/app_ceres/img/LogoClamMedical.png"
}
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/app_ceres/css/app_ceres.css"
# app_include_js = "/assets/app_ceres/js/app_ceres.js"

# include js, css files in header of web template
# web_include_css = "/assets/app_ceres/css/app_ceres.css"
# web_include_js = "/assets/app_ceres/js/app_ceres.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "app_ceres/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
doctype_js = {"Vital Signs" : "public/js/vitalsigns.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "app_ceres.install.before_install"
# after_install = "app_ceres.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "app_ceres.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }


permission_query_conditions = {
    #"patient": "app_ceres.ceres.controllers.paciente.get_permission_query_conditions_usuario",
}



# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }
doc_events = {
    "Patient Encounter": {        
        "before_insert":"app_ceres.ceres.controllers.paciente.generarSecuenciaReceta"
        # "on_update":" "
    } ,
    "Patient":{
		"before_insert":"app_ceres.ceres.controllers.paciente.generarSecuenciaHC"
	}

}


# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"app_ceres.tasks.all"
# 	],
# 	"daily": [
# 		"app_ceres.tasks.daily"
# 	],
# 	"hourly": [
# 		"app_ceres.tasks.hourly"
# 	],
# 	"weekly": [
# 		"app_ceres.tasks.weekly"
# 	]
# 	"monthly": [
# 		"app_ceres.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "app_ceres.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "app_ceres.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "app_ceres.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"app_ceres.auth.validate"
# ]

#website_context = {
#"favicon": "/assets/erpnext/images/erpnext-logo.png",
#"splash_image": "/assets/erpnext/images/erpnext-logo.png"
#}