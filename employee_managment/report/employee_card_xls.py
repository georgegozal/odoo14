from odoo import models


class IdCardXlsx(models.AbstractModel):
    _name = 'report.employee_managment.report_card_xls'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, lines):
        format1 = workbook.add_format({'font_size':14,'align':'vcenter'})
        sheet = workbook.add_worksheet("Patient Card")
        bold = workbook.add_format({'bold': True})
        sheet.write(0, 0, 'ID',bold)        
        sheet.write(0, 1, 'Name', bold)
        sheet.write(0, 2, 'Last Name',bold)
        sheet.write(0, 3, 'Gender',bold)
        sheet.write(0, 4, 'ID Number',bold)
        sheet.write(0, 5, 'Birth Date',bold)
        sheet.write(0, 6, 'Birth Place',bold)
        sheet.write(0, 7, 'Department',bold)                            
        sheet.write(0, 8, 'Features',bold)        
        
        sheet.write(1, 0, lines.reference)
        sheet.write(1, 1, lines.name)
        sheet.write(1, 2, lines.surname)
        sheet.write(1, 3, lines.sex)
        sheet.write(1, 4, lines.id_no)
        sheet.write(1, 5, lines.birth_date)
        sheet.write(1, 6, lines.birth_place)
        sheet.write(1, 7, lines.department)
        #sheet.write(1, 8, lines.features_ids)
        print('\n\n features_ids>>>',lines.features_ids,'\n\n')
        #print('\n\nfeatures>>>',lines.features,'\n\n')

