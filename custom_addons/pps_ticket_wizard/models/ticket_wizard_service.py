from odoo import api, models


class TicketWizardService(models.AbstractModel):
    """Business logic for the ticket wizard, kept independent from
    HTTP/rendering concerns (DOC-050 §4.2) so it can later be exposed
    through a JSON API without duplicating logic."""
    _name = 'pps.ticket.wizard.service'
    _description = 'Ticket Wizard Business Logic'

    @api.model
    def get_contact_prefill(self, user):
        partner = user.partner_id if not user._is_public() else None
        return {
            'name': partner.name if partner else '',
            'company': partner.parent_id.name if partner and partner.parent_id else '',
            'mobile': (getattr(partner, 'mobile', None) or getattr(partner, 'phone', None) or '') if partner else '',
        }

    @api.model
    def get_customer_assets(self, user):
        if user._is_public():
            return self.env['pps.asset']
        commercial_partner = user.partner_id.commercial_partner_id
        return self.env['pps.asset'].sudo().search([('partner_id', '=', commercial_partner.id)])

    @api.model
    def get_asset_info(self, asset_id):
        asset = self.env['pps.asset'].sudo().browse(int(asset_id))
        if not asset.exists():
            return {}

        sla = asset.contract_id.pps_sla_id if asset.contract_id else self.env['pps.sla'].sudo().search(
            [('is_default_fallback', '=', True)], limit=1)

        return {
            'location': asset.pps_location_id.name if asset.pps_location_id else '',
            'sla_name': sla.name if sla else '',
            'sla_response': dict(sla._fields['remote_response_time'].selection).get(
                sla.remote_response_time, '') if sla else '',
            'sla_onsite': dict(sla._fields['onsite_response_time'].selection).get(
                sla.onsite_response_time, '') if sla else '',
        }

    @api.model
    def get_fallback_sla(self):
        return self.env['pps.sla'].sudo().search([('is_default_fallback', '=', True)], limit=1)
