from docxtpl import DocxTemplate

doc = DocxTemplate("INVOICE.docx")

doc.render({})

doc.save("new_invoice.docx")