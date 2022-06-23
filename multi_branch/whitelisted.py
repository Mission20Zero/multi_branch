import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
@frappe.validate_and_sanitize_search_inputs
def get_customer(doctype, txt, searchfield, start, page_len, filters):
    customer_branch = filters.get('customer_branch')
    sql = """ select customer from `tabCustomer Branch` where branch_name = '{0}' or customer like '%%{1}%%' """.format(customer_branch, '%s' % txt)
    return frappe.db.sql(sql)
