# from odoo import models, fields, api


# class vina_equipment(models.Model):
#     _name = 'vina_equipment.vina_equipment'
#     _description = 'vina_equipment.vina_equipment'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

