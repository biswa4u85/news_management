import frappe


@frappe.whitelist()
def fetch_data(doctype, txt, searchfield, start, page_len, filters):
  return frappe.db.sql("""
                      select category from `tabBlog Sub Category Table` where parent = "{0}"
                      """.format(filters.get("blog_sub_category")))  
 
#   Sub To Sub To Sub Category Data Filter

@frappe.whitelist()
def fetch_sub_category(doctype, txt, searchfield, start, page_len, filters):
  return frappe.db.sql("""
                      select category from `tabBlog Sub To Sub Category Table` where parent = "{0}"
                      """.format(filters.get("blog_sub_to_category")))  
  



