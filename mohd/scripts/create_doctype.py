import frappe

def create_my_doctype():
    if not frappe.db.exists("DocType", "Auto Created Doc"):
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": "Auto Created Doc",
            "module": "Custom",
            "custom": 1,
            "fields": [
                {"fieldname": "title", "fieldtype": "Data", "label": "Title"},
                {"fieldname": "description", "fieldtype": "Text", "label": "Description"},
                {"fieldname": "date", "fieldtype": "Date", "label": "Date"},
            ],
            "permissions": [
                {
                    "role": "System Manager",
                    "read": 1,
                    "write": 1,
                    "create": 1,
                    "delete": 1
                }
            ],
        })
        doc.insert()
        frappe.db.commit()
        print("Doctype created successfully")
    else:
        print("Doctype already exists")
