# Copyright (c) 2023, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.model.docstatus import DocStatus

class LibraryTransaction(Document):
	def before_submit(self):
		if self.type == "Issued":
			self.validate_issue()
			# Set the Article status to issued
			article = frappe.get_doc("Article", self.article)
			article.status = "Issued"
			article.save()

		elif self.type == "Return":
			self.validate_return()
			# set the article status to avaliable
			article = frappe.get_doc("Article", self.article)
			article.status = "Avaliable"
			article.save()
	def validate(self):
		self.validate_membership()

	def validate_issue(self):
		self.validate_membership()
		article = frappe.get_doc("Article", self.article)
		# Article cannot be issued if it already issued 
		if article.status  == "Issued":
			frappe.throw("Article is already issued by another member ")
    
	def validate_return(self):
		article = frappe.get_doc("Article", self.article)
		# Article cannot be return if its not issued first 
		if article.status  == "Avaliable":
			frappe.throw("Article cannot be return if its not issued first")
	
	def validate_membership(self):
		validate_membership = frappe.db.exists(
			"Library Membership",
			{
				"library_member":self.library_member,
				"docstatus": DocStatus.submitted(),
				"from_date":("<" , self.date ),
				"to_date":(">", self.date),
			},
		)
		if not validate_membership:
			frappe.throw("The member doesnt have a valid membership")

	def validate_maximum_limit(self):
		max_articles = frappe.db.get_single_value("Library Settings" , "maximum_number_of_issued_article")
		count = frappe.db.count(
			"Library Transactions ",
			{
				"library_member": self.library_member, 
				"type":"Issue", 
				"docstatus": DocStatus.submitted()
				
			},
		)
		if count >= max_articles:
			frappe.throw("Max Limit reached for issuing article")
