# from odoo import http


# class VinaContract(http.Controller):
#     @http.route('/vina_contract/vina_contract', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_contract/vina_contract/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_contract.listing', {
#             'root': '/vina_contract/vina_contract',
#             'objects': http.request.env['vina_contract.vina_contract'].search([]),
#         })

#     @http.route('/vina_contract/vina_contract/objects/<model("vina_contract.vina_contract"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_contract.object', {
#             'object': obj
#         })

