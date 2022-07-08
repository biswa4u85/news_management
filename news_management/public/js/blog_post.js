// Copyright (c) 2022, Hidayatali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Blog Post', {
    blog_category: function(frm) {
        cur_frm.set_query("blog_sub_category", function() {
        return {
        filters: [
                    ["Blog Sub Category","main_category", "in", cur_frm.doc.blog_category]
                ]
        };
        });
    }
});

frappe.ui.form.on('Blog Post', {
    blog_sub_category: function(frm) {
        frm.set_query("blog_sub_to_sub_category", function() {
            return {
                query: 'news.utils.blog_sub_category_table.fetch_data',
                filters: {
                    "blog_sub_category":frm.doc.blog_sub_category
                }
            };
        });
    }

});