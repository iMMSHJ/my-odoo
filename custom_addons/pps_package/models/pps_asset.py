from odoo import fields, models


class PpsAsset(models.Model):
    _inherit = 'pps.asset'

    pps_package_id = fields.Many2one('pps.package', string='Service Package')
