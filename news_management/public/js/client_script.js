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


frappe.ui.form.on('Blog Post', {
    setup: function (frm) {
        frappe.call({
            method: "frappe.client.get",
            args: {
                doctype: "User",
                filters: { 'name': frappe.session.user },
            },
            callback: function (r) {
                let date = frappe.datetime.nowdate();


                if (r.message.published == 1) {
                    cur_frm.set_value("published_status", 1);
                    cur_frm.set_value("published_on", date);
                    cur_frm.set_value("published", 1);
                    //msgprint("Active");
                }

            }
        });
    }
});


frappe.listview_settings['Live Score Series'] = {
    onload: function (listview) {
        listview.page.add_inner_button("Fetch Data", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchDataSeries",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
    },
};

frappe.listview_settings['Live Score Fixtures'] = {
    onload: function (listview) {
        listview.page.add_inner_button("Fetch Data", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchDataFixtures",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
    },
};