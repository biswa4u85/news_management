from unicodedata import category
import frappe

def get_context(context):

    
    post = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 order by creation DESC LIMIT 1 OFFSET 0 
    """, as_dict=True)
    context.post = post

# 2 Post     
    post2 = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 order by creation DESC LIMIT 1 OFFSET 1 
    """, as_dict=True)
    context.post2 = post2

# 3 Post     
    post3 = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 order by creation DESC LIMIT 1 OFFSET 2 
    """, as_dict=True)
    context.post3 = post3


# 4 Post     
    post4 = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 order by creation DESC LIMIT 1 OFFSET 3 
    """, as_dict=True)
    context.post4 = post4

# cricket category

    cricket = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 AND blog_category = "cricket" order by creation DESC LIMIT 4
    """, as_dict=True)
    context.cricket = cricket

# cricket1 category

    cricket1 = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 AND blog_category = "cricket" order by creation DESC LIMIT 1 OFFSET 3
    """, as_dict=True)
    context.cricket1 = cricket1

# cricket2 category

    cricket2 = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 AND blog_category = "cricket" order by creation DESC LIMIT 3
    """, as_dict=True)
    context.cricket2 = cricket2

# politics category

    politics = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 AND blog_category = "politics" order by creation DESC LIMIT 4
    """, as_dict=True)
    context.politics = politics

# Featured Post

    featured = frappe.db.sql(""" select * from `tabBlog Post` where published = 1 AND most_popular = 1 order by creation DESC LIMIT 4
    """, as_dict=True)
    # context.post = post
    context.featured = featured  

# Logo & Favicon & website Title

    logo = frappe.db.sql(""" select * from `tabSite Setting`
    """, as_dict=True)
    context.logo = logo    



# Trending Now:

    tre = frappe.db.sql(""" select * from `tabBlog Post` where published = 1
    """, as_dict=True)
    # context.post = post
    context.tre = tre

    return context

    