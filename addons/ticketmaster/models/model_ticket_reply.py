from odoo import _, api, fields, models


class TicketReply(models.Model):
    _name = "ticketmaster.reply"
    _description = """Reply to support ticket"""

    master_id = fields.Many2one("ticketmaster.ticket", string=_("Ticket"), required=True)
    user = fields.Many2one("res.users", string=_("User"), required=True)
    date = fields.Date(string=_("Date Created"), default=fields.Date.today())
    description = fields.Text(string=_("Description"), required=True)
