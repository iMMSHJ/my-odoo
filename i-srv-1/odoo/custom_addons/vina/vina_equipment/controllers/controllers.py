# from odoo import http


# class VinaEquipment(http.Controller):
#     @http.route('/vina_equipment/vina_equipment', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vina_equipment/vina_equipment/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('vina_equipment.listing', {
#             'root': '/vina_equipment/vina_equipment',
#             'objects': http.request.env['vina_equipment.vina_equipment'].search([]),
#         })

#     @http.route('/vina_equipment/vina_equipment/objects/<model("vina_equipment.vina_equipment"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vina_equipment.object', {
#             'object': obj
#         })

