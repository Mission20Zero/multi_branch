frappe.ui.form.on("Sales Invoice", {
	setup: function(frm){
		set_customer(frm);
	},

	customer_branch: function(frm){
		set_customer(frm);
	}
});


function set_customer(frm){
	if(frm.doc.customer_branch){
		console.log(frm.doc.customer_branch);
		frm.set_query("customer", function(doc){
			return {
				"filters":[
					['Customer Branch', "customer_branch", "=", doc.customer_branch]
				]
			}
		});
	}
}
