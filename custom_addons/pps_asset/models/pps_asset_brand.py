from odoo import fields, models


class PpsAssetBrand(models.Model):
    _name = 'pps.asset.brand'
    _description = 'Asset Brand (Dictionary)'
    _order = 'name'

    name = fields.Char(required=True)
    model_ids = fields.One2many('pps.asset.model', 'brand_id', string='Models')

    _name_uniq = models.Constraint(
        'UNIQUE(name)',
        'Brand name must be unique.',
    )
