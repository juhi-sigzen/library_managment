// Copyright (c) 2023, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Article', {
	refresh: function(frm) {
		frm.add_custom_button('Fetch ISBN ' , () => {
		   frm.call('get_isbn');

		})
	}
});

frappe.ui.form.on('Article Review', {
	reviews_add(frm,cdt,cdn){
		console.log('row added' ,cdt ,cdn);
		let row  = frappe.get_doc(cdt,cdn);
		row.rating = 3 / 5;
		frm.refresh(); 
	},

	reviews_remove(frm,cdt,cdn){
		console.log('row removed' ,cdt ,cdn);

	},

	reviews_move(frm,cdt,cdn){
		console.log('row moved' ,cdt ,cdn);
	},


	form_render(frm,cdt,cdn){
		console.log('row rendered' ,cdt ,cdn);
	},
});
