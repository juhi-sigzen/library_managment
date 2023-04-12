# Copyright (c) 2023, Frappe and contributors
# For license information, please see license.txt

# import frappe


def execute(filters=None):
	
	chart = {
		"type":"bar",
		"data":{
			"labels": ["Monday" , "Tuesday" , "Wednesday" , "Thrusday" , "Friday"],
			"datasets": [
				{"name": "Some Data" , "values": [25,40,30,35,8]},
				{"name": "Another set" , "values": [25,50,-10,15,18]},
			],
	 	}
	}
	profit = 20
	report_summary = [
		{"value": 1200, "label": 'Income',"datatype": "Currency", "currency": 'INR'},
		{"type": "separator", "value": "-"},
		{"value": 300, "label": "Expense","datatype": "Currency", "currency": "INR"},
		{"type": "separator", "value": "", "color": "blue"},
		{"value": 1200 - 300, "indicator": "Green" if profit > 0 else "Red", "label": "Profit/Loss", "datatype": "Currency", "currency": "INR"}
		]
	
	columns = [
		{'fieldtypes': 'Data' , 'label': 'Book Name' ,'field name':'book_name','width': 100 },
		{'fieldtypes': 'Data' , 'label': 'Author' ,'field name':'author','width': 100 },		
	]

	result = [
		{'book_name': 'Book 1' , 'author': 'Author-1'},
		{'book_name': 'Book 2' , 'author': 'Author-2'},
		{'book_name': 'Book 3' , 'author': 'Author-3'},
	]

	return columns,result,"Report genrated 3 minutes ago",chart,report_summary