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
                }

            }
        });
    }
});

frappe.listview_settings['Flash Sports'] = {
    onload: function (listview) {
        listview.page.add_inner_button("Fetch Sports", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchSports",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
        listview.page.add_inner_button("Fetch Data", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchSportsEventsCount",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
    },
};

frappe.listview_settings['Flash Rankings'] = {
    onload: function (listview) {
        listview.page.add_inner_button("Fetch Data", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchRankings",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
    },
};

frappe.listview_settings['Flash Events'] = {
    onload: function (listview) {
        listview.page.add_inner_button("Fetch Data", function () {
            frappe.call({
                method: "news_management.fixtures_api.fetchEvents",
                args: {}
            });
        }).css({ 'color': 'red', 'font-weight': 'bold' });
    },
};