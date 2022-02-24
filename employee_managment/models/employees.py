from odoo import fields, models , api, _
from odoo.exceptions import ValidationError



class IdDepartment(models.Model):
    _name ='id.department'
    _rec_name = 'department'

    department = fields.Char(string ='Department',required=True,unique=True)
    department_members = fields.One2many(comodel_name='id.card',inverse_name='department_id',string='Department Members')
    _sql_constraints = [
        ('department_unique',
        'unique(department)',
        'Choose another value - it has to be unique!')
    ]
    department_count = fields.Integer(string='Department count',compute='_compute_department_count')
    
    all_employees = fields.Integer(string='All Employees count', compute='_compute_all_employees')
    
    def _compute_department_count(self):
        for rec in self:
            department_count = self.env['id.card'].search_count([('department_id','=',rec.id)])
            rec.department_count = department_count
        
    def _compute_all_employees(self):
        all_employees = self.env['id.card'].search_count([])
        self.all_employees = all_employees


class EmployeeFeatures(models.Model):
    _name = 'id.features'
    _rec_name = 'features'

    features = fields.Char(string ='Features')
    #_rec_name = 'features'

class EmployeeIdData(models.Model):
    _name = "id.card"
    _description = 'Identity information'
    _inherit = ['mail.thread','mail.activity.mixin']


    name = fields.Char(string="First name", default="Jimmy",required=True,tracking=True)
    surname = fields.Char(string="Last name", default='Page',required=True,tracking=True)
    id_no = fields.Char(string='ID Number',required=True,tracking=True)
    sex = fields.Selection([('male','Male'),('female','Female')],required=True)
    birth_place = fields.Char(string="Birth place",required=True,tracking=True)
    birth_date = fields.Date(string="Birth Date",required=True,tracking=True)
    #photo = fields.Image(string="Photo",required=False,tracking=True,)
    #                            max_width=480,max_height=680)
    image = fields.Binary(string="Photo",required=False,tracking=True)
    department_id = fields.Many2one(comodel_name='id.department',delegate=True,ondelete='restrict', select=True,
                                    string='Department')

    features_ids = fields.Many2many('id.features',string='Features',ondelete='restrict')

    reference = fields.Char(string='Order Reference', required=True,copy=False,
                            readonly=True, default=lambda self: _('New'))

    @api.constrains('id_no')
    def id_no_check(self):
        if self.id_no.isdigit():
                if len(self.id_no) ==11:
                    return True
                else:
                    raise ValidationError('ID Number should be 11 numbers')
        else:
            raise ValidationError("ID Number should be only numbers")


    # override create function
    @api.model
    def create(self, values):

        if values.get('reference', _('New')) == _('New'):
            values['reference'] = self.env['ir.sequence'].next_by_code('id.card') or _('New')

        res = super(EmployeeIdData, self).create(values)

        return res
