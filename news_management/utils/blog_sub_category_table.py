import frappe


@frappe.whitelist()
def fetch_data(doctype, txt, searchfield, start, page_len, filters):
  return frappe.db.sql("""
                      select category from `tabBlog Sub Category Table` where parent = "{0}"
                      """.format(filters.get("blog_sub_category")))  
  




