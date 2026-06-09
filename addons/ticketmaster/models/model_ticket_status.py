from odoo import _, api, fields, models


class TicketStatus(models.Model):
    _name = "ticketmaster.status"
    _description = """Status for support ticket"""

    name = fields.Char(string=_("Status"), required=True)
    color = fields.Char(string=_("HTML Color"), default="#ffffff")
