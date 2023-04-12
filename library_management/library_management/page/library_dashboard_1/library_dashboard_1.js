frappe.pages['library-dashboard-1'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Library DashBoard',
		single_column: true
	});

	frappe.require(['library_dashboard.bundle.js' ,'library_dashboard.bundle.css' ], 
	() =>{
		console.log('Library bundle Loaded');
	})
}