# Copyright (c) 2023, Frappe and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document

class Article(Document):
	def get_title(self):
		return self.article_name