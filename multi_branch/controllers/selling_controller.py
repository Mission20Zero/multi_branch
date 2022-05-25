import json
import frappe
from frappe import _, msgprint, throw
from multi_branch.controllers import base_controller

class SellingController(base_controller.BaseController):
    def validate_doc(self):
        if self.dt == "Sales Invoice":
            self.update_gl()
        elif self.dt == "Payment Entry":
            self.update_pe_gl()

    def update_gl(self):
        frappe.msgprint(_("{0}").format(self.doc.customer))
        if frappe.db.exists("Customer", self.doc.customer, "head_office"):
            head_office = frappe.db.get_value("Customer", self.doc.customer, "head_office")
            gl_entries = frappe.db.get_list("GL Entry", {"voucher_type": "Sales Invoice", "voucher_no": self.doc.name}, "name")
            for gl in gl_entries:
                doc = frappe.get_doc("GL Entry", gl.name)
                new_doc = frappe.copy_doc(doc)
                new_doc.party_type = "Customer"
                new_doc.party = head_office
                new_doc.save(ignore_permissions=True)
                new_doc.submit()

    def update_pe_gl(self):
        if self.doc.party_type == "Customer" and frappe.db.exists("Customer", self.doc.party, "head_office"):
            head_office = frappe.db.get_value("Customer", self.doc.customer, "head_office")
            gl_entries = frappe.db.get_list("GL Entry", {"voucher_type": "Payment Entry", "voucher_no": self.doc.name}, "name")
            for gl in gl_entries:
                doc = frappe.get_doc("GL Entry", gl.name)
                new_doc = frappe.copy_doc(doc)
                new_doc.party_type = "Customer"
                new_doc.party = head_office
                new_doc.save(ignore_permissions=True)
                new_doc.submit()
