// Copyright (c) 2016, h@ci and contributors
// For license information, please see license.txt

frappe.query_reports["Detailed Profitability of Customer"] = {
	"filters": [
		{
			fieldname: "from_date",
			label: __("From Date"),
			fieldtype: "Date",
			default: frappe.defaults.get_user_default("year_start_date"),
		},
		{
			fieldname:"to_date",
			label: __("To Date"),
			fieldtype: "Date",
			default: get_today()
		},
		{
			fieldname: "cost_center",
			label: __("Customer"),
			fieldtype: "Link",
			options: "Cost Center",
			default: "Main - FR",
		},
	]
}