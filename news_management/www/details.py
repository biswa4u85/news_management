import frappe


def get_context(context):
    # print(f"\n\n\n\n{frappe.form_dict}\n\n\n\n")
    
    # context.detail = frappe.get_doc("Blog Post", frappe.form_dict.docname)
    try:
        docname = frappe.form_dict.docname
        context.detail = frappe.get_doc("Blog Post", frappe.form_dict.docname)

    except Exception as e:
        frappe.local.flags.redirect_location = '/404'
        raise frappe.Redirect

    return context
