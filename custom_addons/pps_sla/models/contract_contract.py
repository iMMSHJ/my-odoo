from odoo import fields, models


class ContractContract(models.Model):
    _inherit = 'contract.contract'

    pps_sla_id = fields.Many2one('pps.sla', string='SLA')
