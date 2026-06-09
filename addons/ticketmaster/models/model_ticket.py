from odoo import _, api, fields, models

class Ticket(models.Model):
    _name = "ticketmaster.ticket"
    _description = """Support Ticket"""

    title = fields.Char(string=_("Title"), required=True)
    description = fields.Text(string=_("Description"), required=True)
    date = fields.Date(string=_("Date Created"), default=fields.Date.today())

