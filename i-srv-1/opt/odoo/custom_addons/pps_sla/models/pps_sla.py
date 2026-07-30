from odoo import fields, models


class PpsSla(models.Model):
    _name = 'pps.sla'
    _description = 'SLA Template'
    _order = 'name'

    name = fields.Char(string='Name', required=True, help='Commercial tier name, e.g. Bronze / Silver / Gold / Platinum')

    remote_response_time = fields.Selection([
        ('2h', '2 Hours'),
        ('4h', '4 Hours'),
        ('1d', '1 Business Day'),
        ('2d', '2 Business Days'),
        ('5d', '5 Business Days'),
    ], string='Remote Response Time', required=True)

    working_calendar_id = fields.Many2one('resource.calendar', string='Working Calendar')

    remote_support = fields.Selection([
        ('included', 'Included'),
        ('optional', 'Optional'),
        ('not_included', 'Not Included'),
    ], string='Remote Support', required=True, default='included')

    onsite_response_time = fields.Selection([
        ('same_day', 'Same Day'),
        ('1d', '1 Business Day'),
        ('2d', '2 Business Days'),
        ('5d', '5 Business Days'),
        ('not_included', 'Not Included'),
    ], string='Onsite Response Time', required=True)

    spare_parts_commitment = fields.Selection([
        ('included', 'Included'),
        ('chargeable', 'Chargeable'),
        ('best_effort', 'Best Effort'),
    ], string='Spare Parts', required=True, default='chargeable')

    loan_device_commitment = fields.Selection([
        ('included', 'Included'),
        ('optional', 'Optional'),
        ('not_included', 'Not Included'),
    ], string='Loan Device', required=True, default='not_included')

    preventive_maintenance_frequency = fields.Selection([
        ('none', 'None'),
        ('monthly', 'Monthly'),
        ('quarterly', 'Quarterly'),
        ('semi_annual', 'Semi-Annual'),
        ('annual', 'Annual'),
        ('custom', 'Custom'),
    ], string='Preventive Maintenance', required=True, default='none')

    is_default_fallback = fields.Boolean(
        string='Default Fallback (No-Contract Customers)',
        help='Only one SLA record should have this enabled.',
    )

    active = fields.Boolean(default=True)
