from unicodedata import category
import frappe

def get_context(context):

    docname = frappe.form_dict.docname
    blog = frappe.db.sql(""" select * from `tabBlog Post` where name = "a-player-who-belongs-to-rohit-sharmas-category-former-india-batter-on-sanju-samson" 
    """, as_dict=True)
    # context.post = post
    context.blog = blog

    return context