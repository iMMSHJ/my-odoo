# from odoo import http


# class VinaBase(http.Controller):
#     @http.route('/vina_base/vina_base', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_base/vina_base/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_base.listing', {
#             'root': '/vina_base/vina_base',
#             'objects': http.request.env['vina_base.vina_base'].search([]),
#         })

#     @http.route('/vina_base/vina_base/objects/<model("vina_base.vina_base"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_base.object', {
#             'object': obj
#         })

