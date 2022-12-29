from odoo import _, api, fields, models
from odoo.exceptions import ValidationError


class PayrollSystem(models.Model):
    _name = 'payroll.payrollsystem'
    _inherit = 'hr.employee'
    _description = 'Payroll System'

    category_ids = fields.Many2many(
        'hr.employee.category', 'payrollsystem_category_rel',
        'payrollsystem_id', 'category_id',
        string='Tags')

    @api.onchange('salary', 'hour_rate')
    def change_value(self):
        if self.salary < 0 or self.hour_rate < 0:
            raise ValidationError(_('The number can\'t be negative!'))

    @api.model
    def _default_currency(self):
        return self.env['res.currency'].search([('name', '=', 'USD')], limit=1)

    type_of_wage = fields.Selection([('hourly', 'Hourly'), ('fixed', 'Fixed')], string='Type of wage')
    currency_id = fields.Many2one('res.currency', string='Currency', default=_default_currency)
    salary = fields.Monetary(string='Salary')
    hour_rate = fields.Monetary(string='Hour rate')
    worked_hours = fields.Float(string='Hours worked')
    payment_date = fields.Date(string='Payment date')
