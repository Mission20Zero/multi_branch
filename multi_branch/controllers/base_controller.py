import frappe, json
from frappe import _, msgprint, throw
SELLING = ["Sales Invoice", "Payment Entry"]

def validate_controller(doc, method):
    doctype = doc.meta.get("name")
    try:
        if doctype in SELLING:
            from multi_branch.controllers.selling_controller import SellingController
            if method == "on_submit":
                SellingController(doc, doctype, method).validate_doc()
    except Exception as e:
        frappe.throw(e)
        print("----"*10)
        print("----"*10)
        frappe.db.rollback()

'''
        Base controller for validation purpose
'''

class BaseController():
    def __init__(self, doc, doctype, method):
        self.dt = doctype
        self.doc = doc
        self.method = method
