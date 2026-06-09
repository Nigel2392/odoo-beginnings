from odoo import api, fields, models


class Ticket(models.Model):
    _name = "ticketmaster.ticket"
    _description = """Support Ticket"""

    title = fields.Char(string="Title", required=True)
    description = fields.Text(string="Description", required=True)
    date = fields.Date(string="Date Created", default=fields.Date.today())

