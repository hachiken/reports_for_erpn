# Copyright (c) 2013, h@ci and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe	
from frappe import _

def execute(filters=None):
	columns = [
		_("Cost Center") + ":Link/Cost Center:140",
#		_("Posting Date") + ":Date:100",
		_("Sales") + ":Currency:100",
		_("Expences") + ":Currency:100",
		_("Profit") + ":Currency:100",
		_("Profit Margin %") + ":Percent:120",]
	data = frappe.db.sql("""
		select
		    cost_center, sum(credit), sum(debit), sum(credit)-sum(debit), (sum(credit)-sum(debit))/sum(credit)*100
		from
		    `tabGL Entry`
		where
		    cost_center IS NOT NULL AND posting_date>"%s" AND posting_date<"%s"
		group by cost_center
			""" % (filters["from_date"], filters["to_date"]))
	
	return columns, data