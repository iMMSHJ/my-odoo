# from odoo import models, fields, api


# class vina_contract(models.Model):
#     _name = 'vina_contract.vina_contract'
#     _description = 'vina_contract.vina_contract'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

