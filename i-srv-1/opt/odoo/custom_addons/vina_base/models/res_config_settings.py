from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    vina_support_email = fields.Char(
        string="Support Email",
        config_parameter="vina_base.support_email",
    )

    vina_support_phone = fields.Char(
        string="Support Phone",
        config_parameter="vina_base.support_phone",
    )
