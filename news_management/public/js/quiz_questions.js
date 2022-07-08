// Copyright (c) 2022, Hidayatali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Quiz Questions', {
    published(frm) {
        frm.set_value("date", frappe.datetime.now_datetime());
    }
})