# from odoo import http


# class VinaService(http.Controller):
#     @http.route('/vina_service/vina_service', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_service/vina_service/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_service.listing', {
#             'root': '/vina_service/vina_service',
#             'objects': http.request.env['vina_service.vina_service'].search([]),
#         })

#     @http.route('/vina_service/vina_service/objects/<model("vina_service.vina_service"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_service.object', {
#             'object': obj
#         })

