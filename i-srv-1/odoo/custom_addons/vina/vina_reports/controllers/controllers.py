# from odoo import http


# class VinaReports(http.Controller):
#     @http.route('/vina_reports/vina_reports', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_reports/vina_reports/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_reports.listing', {
#             'root': '/vina_reports/vina_reports',
#             'objects': http.request.env['vina_reports.vina_reports'].search([]),
#         })

#     @http.route('/vina_reports/vina_reports/objects/<model("vina_reports.vina_reports"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_reports.object', {
#             'object': obj
#         })

