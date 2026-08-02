from odoo import http
from odoo.http import request


class PpsTicketWizardController(http.Controller):

    def _service(self):
        return request.env['pps.ticket.wizard.service']

    # ---------- Step 1: Contact Info ----------

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

    # ---------- Step 2: Device Selection ----------

    @http.route('/support/new/device', type='http', auth='public', website=True, sitemap=False)
    def wizard_device(self, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        if not wizard_data.get('contact'):
            return request.redirect('/support/new')

        is_guest = request.env.user._is_public()
        assets = self._service().get_customer_assets(request.env.user)

        assets_info = {}
        for asset in assets:
            assets_info[asset.id] = self._service().get_asset_info(asset.id)

        return request.render('pps_ticket_wizard.step_device', {
            'is_guest': is_guest,
            'assets': assets,
            'assets_info': assets_info,
        })

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

    # ---------- Step 3: Description + Attachments ----------

    @http.route('/support/new/description', type='http', auth='public', website=True, sitemap=False)
    def wizard_description(self, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        import logging
        logging.getLogger('pps_debug').info('ON DESCRIPTION PAGE: %s', wizard_data)
        if not wizard_data.get('device'):
            return request.redirect('/support/new/device')
        return request.render('pps_ticket_wizard.step_description', {})

    @http.route('/support/new/description/save', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def wizard_save_description(self, error_code=None, description=None, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        wizard_data['issue'] = {'error_code': error_code, 'description': description}

        files = request.httprequest.files.getlist('attachments')
        attachment_ids = self._service().save_attachments(files)
        wizard_data['attachment_ids'] = attachment_ids

        request.session['pps_wizard'] = wizard_data
        return request.redirect('/support/new/review')

    # ---------- Step 4: Review + Submit ----------

    @http.route('/support/new/review', type='http', auth='public', website=True, sitemap=False)
    def wizard_review(self, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        if not wizard_data.get('issue'):
            return request.redirect('/support/new/description')

        sla = self._service().get_sla_for_wizard(wizard_data.get('device', {}))

        return request.render('pps_ticket_wizard.step_review', {
            'contact': wizard_data.get('contact', {}),
            'device': wizard_data.get('device', {}),
            'issue': wizard_data.get('issue', {}),
            'sla': sla,
        })

    @http.route('/support/new/submit', type='http', auth='public', website=True, methods=['POST'], csrf=True)
    def wizard_submit(self, **kwargs):
        wizard_data = request.session.get('pps_wizard', {})
        if not wizard_data.get('issue'):
            return request.redirect('/support/new')

        result = self._service().create_ticket(wizard_data, request.env.user)
        request.session['pps_wizard_result'] = result
        request.session.pop('pps_wizard', None)
        return request.redirect('/support/new/confirmation')

    @http.route('/support/new/confirmation', type='http', auth='public', website=True, sitemap=False)
    def wizard_confirmation(self, **kwargs):
        result = request.session.get('pps_wizard_result')
        if not result:
            return request.redirect('/support/new')
        return request.render('pps_ticket_wizard.step_confirmation', {'result': result})
