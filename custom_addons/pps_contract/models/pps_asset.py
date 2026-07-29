from odoo import fields, models


class PpsAsset(models.Model):
    _inherit = 'pps.asset'

    contract_id = fields.Many2one(
        'contract.contract',
        string='Service Contract',
        tracking=True,
        help='Leave empty if this asset has no active service contract yet.',
    )
