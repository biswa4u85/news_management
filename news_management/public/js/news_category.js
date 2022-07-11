frappe.ui.form.on('News Category', {
	setup: function(frm) {
    frm.set_query('parent_news_category', function(doc) {
        return {
            filters: {
                'is_group': 1
            }
        }
    });
}
});