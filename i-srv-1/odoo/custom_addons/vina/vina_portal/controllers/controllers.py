# from odoo import http


# class VinaPortal(http.Controller):
#     @http.route('/vina_portal/vina_portal', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_portal/vina_portal/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_portal.listing', {
#             'root': '/vina_portal/vina_portal',
#             'objects': http.request.env['vina_portal.vina_portal'].search([]),
#         })

#     @http.route('/vina_portal/vina_portal/objects/<model("vina_portal.vina_portal"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_portal.object', {
#             'object': obj
#         })

