frappe.ui.form.on('Blog Post', {
    setup: function (frm) {
        frm.set_query('news_category', function (doc) {
            return {
                filters: {
                    'status': "Active"
                }
            }
        });
    }
});