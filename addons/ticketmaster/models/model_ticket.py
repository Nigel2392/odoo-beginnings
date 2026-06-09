from odoo import _, api, fields, models
from odoo.exceptions import UserError


class Ticket(models.Model):
    _name = "ticketmaster.ticket"
    _description = """Support Ticket"""

    title = fields.Char(
        string=_("Title"),
        required=True,
    )
    description = fields.Text(
        string=_("Description"),
        required=True,
    )
    date = fields.Date(
        string=_("Date Created"),
        default=fields.Date.today(),
    )
    status_id = fields.Many2one(
        "ticketmaster.status",
        string=_("Status"),
    )

    def action_close_ticket(self):
        for ticket in self:
            if ticket.status_id.code != 'resolved':
                raise UserError(_("You can only close resolved tickets."))