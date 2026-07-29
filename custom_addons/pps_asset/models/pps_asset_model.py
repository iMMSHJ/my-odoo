from odoo import fields, models


class PpsAssetModel(models.Model):
    _name = 'pps.asset.model'
    _description = 'Asset Model (Dictionary)'
    _order = 'name'

    name = fields.Char(required=True)
    brand_id = fields.Many2one('pps.asset.brand', string='Brand', required=True, ondelete='restrict')

    _name_brand_uniq = models.Constraint(
        'UNIQUE(name, brand_id)',
        'Model name must be unique per brand.',
    )
