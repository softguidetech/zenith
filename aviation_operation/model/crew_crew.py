from odoo import models, fields

class CrewCrew(models.Model):
    _name = 'crew.crew'
    _description = 'Crew'
    _rec_name = 'f_name'

    f_name = fields.Char(string='First Name')
    s_name = fields.Char(string='Second Name')
    th_name = fields.Char(string='Third Name')
    l_name = fields.Char(string='Last Name')
    passport_no = fields.Char(string='Passport Number')
    place_of_issue = fields.Char(string='Place of Issue')
    date_of_issue = fields.Date(string='Date of Issue')
    date_of_expiry = fields.Date(string='Date of Expiry')
    dob = fields.Date(string='Date of Birth')
    pob = fields.Many2one('res.country',string='Place of Birth')
    job_id = fields.Many2one('hr.job',string='Job Position')
    department_id = fields.Many2one('hr.department',string='Department')
    department_manager_id = fields.Many2one('hr.employee',string='Department Manager')
    date_of_join = fields.Date(string='Date of Join')
    gender = fields.Selection([('male','Male'),
                               ('female','Female')],default='male',string='Gender')
    nationality_id = fields.Many2one('res.country',sting='Nationality')
    operation_id = fields.Many2one('operation.operation')
