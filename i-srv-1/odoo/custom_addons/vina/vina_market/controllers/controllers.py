# from odoo import http


# class VinaMarket(http.Controller):
#     @http.route('/vina_market/vina_market', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_market/vina_market/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_market.listing', {
#             'root': '/vina_market/vina_market',
#             'objects': http.request.env['vina_market.vina_market'].search([]),
#         })

#     @http.route('/vina_market/vina_market/objects/<model("vina_market.vina_market"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_market.object', {
#             'object': obj
#         })

