from odoo import http
from odoo.http import request


class PpsTicketWizardController(http.Controller):

    def _service(self):
        return request.env['pps.ticket.wizard.service']

    @http.route('/support/new', type='http', auth='public', website=True, sitemap=False)
    def wizard_start(self, **kwargs):
        user = request.env.user
        is_guest = user._is_public()
        prefill = self._service().get_contact_prefill(user)

        if not is_guest:
            request.session['pps_wizard'] = {'contact': prefill}

        return request.render('pps_ticket_wizard.step_contact', {
            'prefill': prefill,
            'is_guest': is_guest,
        })

    @http.route('/support/new/contact/save', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def wizard_save_contact(self, name=None, company=None, mobile=None, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        wizard_data['contact'] = {'name': name, 'company': company, 'mobile': mobile}
        request.session['pps_wizard'] = wizard_data
        return request.redirect('/support/new/device')

    @http.route('/support/new/device', type='http', auth='public', website=True, sitemap=False)
    def wizard_device(self, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        if not wizard_data.get('contact'):
            return request.redirect('/support/new')

        is_guest = request.env.user._is_public()
        assets = self._service().get_customer_assets(request.env.user)

        return request.render('pps_ticket_wizard.step_device', {'is_guest': is_guest, 'assets': assets})

    @http.route('/support/new/device/info', type='jsonrpc', auth='public', website=True)
    def wizard_device_info(self, asset_id=None, **kwargs):
        if not asset_id:
            return {}
        return self._service().get_asset_info(asset_id)

    @http.route('/support/new/device/save', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def wizard_save_device(self, asset_id=None, brand=None, model=None, serial=None, location=None, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        is_guest = request.env.user._is_public()
        if is_guest:
            wizard_data['device'] = {'mode': 'manual', 'brand': brand, 'model': model, 'serial': serial, 'location': location}
        else:
            wizard_data['device'] = {'mode': 'asset', 'asset_id': int(asset_id) if asset_id else False}
        request.session['pps_wizard'] = wizard_data
        return request.redirect('/support/new/description')
