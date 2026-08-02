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

    @api.model
    def save_attachments(self, files):
        """Create standalone ir.attachment records (not linked to any ticket yet).
        Returns list of attachment IDs."""
        attachment_ids = []
        for file_storage in files:
            if not file_storage or not file_storage.filename:
                continue
            content = file_storage.read()
            attachment = self.env['ir.attachment'].sudo().create({
                'name': file_storage.filename,
                'datas': content.encode('base64') if isinstance(content, str) else __import__('base64').b64encode(content),
                'res_model': 'pps.ticket.wizard.service',
                'res_id': 0,
            })
            attachment_ids.append(attachment.id)
        return attachment_ids

    @api.model
    def get_sla_for_wizard(self, device_data):
        if device_data.get('mode') == 'asset' and device_data.get('asset_id'):
            asset = self.env['pps.asset'].sudo().browse(device_data['asset_id'])
            if asset.exists() and asset.contract_id and asset.contract_id.pps_sla_id:
                return asset.contract_id.pps_sla_id
        return self.get_fallback_sla()

    @api.model
    def create_ticket(self, wizard_data, user):
        contact = wizard_data.get('contact', {})
        device = wizard_data.get('device', {})
        issue = wizard_data.get('issue', {})
        is_guest = user._is_public()

        # Build description text combining device info + issue description
        if device.get('mode') == 'asset':
            asset = self.env['pps.asset'].sudo().browse(device.get('asset_id'))
            device_text = f"Device: {asset.name}" if asset.exists() else ''
        else:
            device_text = (
                f"Device Brand: {device.get('brand', '')}\n"
                f"Device Model: {device.get('model', '')}\n"
                f"Serial Number: {device.get('serial', '')}\n"
                f"Location: {device.get('location', '')}"
            )

        description = (
            f"Error Code: {issue.get('error_code', '-')}\n\n"
            f"{issue.get('description', '')}\n\n"
            f"--- Device Info ---\n{device_text}"
        )

        partner = user.partner_id if not is_guest else False
        ticket_vals = {
            'name': f"Service Request - {contact.get('name', 'Guest')}",
            'description': description,
            'partner_name': contact.get('name'),
            'partner_email': contact.get('email', False),
        }
        if partner:
            ticket_vals['partner_id'] = partner.id

        ticket = self.env['helpdesk.ticket'].sudo().create(ticket_vals)

        # Re-link previously saved attachments to this ticket
        attachment_ids = wizard_data.get('attachment_ids', [])
        if attachment_ids:
            self.env['ir.attachment'].sudo().browse(attachment_ids).write({
                'res_model': 'helpdesk.ticket',
                'res_id': ticket.id,
            })

        sla = self.get_sla_for_wizard(device)

        return {
            'ticket_id': ticket.id,
            'tracking_code': f"TCK-{ticket.id:06d}",
            'sla_name': sla.name if sla else '',
            'sla_response': dict(sla._fields['remote_response_time'].selection).get(
                sla.remote_response_time, '') if sla else '',
            'is_guest': is_guest,
        }
