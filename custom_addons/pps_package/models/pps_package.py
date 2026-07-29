from odoo import api, fields, models


class PpsPackage(models.Model):
    _name = 'pps.package'
    _description = 'Service Package (Groups Assets under one Contract)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Name', required=True, tracking=True)
    partner_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    asset_ids = fields.One2many('pps.asset', 'pps_package_id', string='Assets')
    contract_id = fields.Many2one('contract.contract', string='Contract', tracking=True)

    state = fields.Selection([
        ('draft', 'Draft'),
        ('active', 'Active'),
        ('expired', 'Expired'),
    ], string='Status', default='draft', tracking=True, required=True)

    @api.constrains('state', 'contract_id')
    def _check_active_requires_contract(self):
        for rec in self:
            if rec.state == 'active' and not rec.contract_id:
                raise models.ValidationError(
                    'A Package cannot be Active without a linked Contract.'
                )
