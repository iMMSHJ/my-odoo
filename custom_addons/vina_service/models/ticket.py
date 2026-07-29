from odoo import fields, models


class VinaTicket(models.Model):
    _name = "vina.ticket"
    _description = "Vina Service Ticket"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _order = "id desc"

    name = fields.Char(
        string="Ticket Number",
        required=True,
        copy=False,
        default="New",
        tracking=True,
    )

    subject = fields.Char(
        string="Subject",
        required=True,
        tracking=True,
    )

    description = fields.Text(
        string="Description",
    )

    active = fields.Boolean(
        default=True,
    )
