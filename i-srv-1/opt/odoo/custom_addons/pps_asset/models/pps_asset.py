from odoo import api, fields, models


class PpsAsset(models.Model):
    _name = 'pps.asset'
    _description = 'Customer Asset (Service-managed Equipment)'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Name', compute='_compute_name', store=True)

    pps_serial_number = fields.Char(string='Serial Number', required=True, tracking=True)
    pps_brand_id = fields.Many2one('pps.asset.brand', string='Brand', required=True, tracking=True)
    pps_model_id = fields.Many2one('pps.asset.model', string='Model', required=True, tracking=True)
    pps_manufacture_date = fields.Date(string='Manufacture Date', help='Leave empty or enter just the year if exact month/day is unknown.')

    partner_id = fields.Many2one('res.partner', string='Customer', required=True, tracking=True)
    pps_location_id = fields.Many2one('res.partner', string='Device Location (Site)')

    pps_condition_grade = fields.Selection([
        ('excellent', 'Excellent'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('needs_review', 'Needs Review'),
    ], string='Condition Grade', help='Applicable for stock/used devices only')
    pps_condition_note = fields.Text(string='Condition Note')

    pps_warranty_period = fields.Integer(string='Warranty Period (months)')
    pps_is_service_asset = fields.Boolean(string='Created from Device Sale', default=False)

    active = fields.Boolean(default=True)

    @api.depends('pps_brand_id', 'pps_model_id', 'pps_serial_number')
    def _compute_name(self):
        for rec in self:
            parts = [rec.pps_brand_id.name or '', rec.pps_model_id.name or '', rec.pps_serial_number or '']
            rec.name = ' - '.join(p for p in parts if p) or 'New Asset'

    @api.onchange('pps_brand_id')
    def _onchange_brand(self):
        if self.pps_model_id and self.pps_model_id.brand_id != self.pps_brand_id:
            self.pps_model_id = False
        return {'domain': {'pps_model_id': [('brand_id', '=', self.pps_brand_id.id)]}}

    _serial_number_uniq = models.Constraint(
        'UNIQUE(pps_serial_number)',
        'Serial number must be unique.',
    )
