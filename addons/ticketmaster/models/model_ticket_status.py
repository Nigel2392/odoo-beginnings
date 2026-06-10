from odoo import _, api, fields, models


class TicketStatus(models.Model):
    _name = "ticketmaster.status"
    _description = """Status for support ticket"""

    _sql_constraints = [("code_unique", "unique(code)", "The status code must be unique!")]

    name = fields.Char(
        string=_("Status"),
        required=True,
        translate=True,
    )
    code = fields.Char(
        string=_("Code"),
        required=True,
    )
    color = fields.Char(
        string=_("HTML Color"),
        default="#ffffff",
    )
    ticket_ids = fields.One2many(
        "ticketmaster.ticket",
        "status_id",
        string=_("Tickets"),
    )